"""Run golden requests for one group on opencode and score which skill it loaded.

Usage: run_opencode.py GROUP N_TRIALS OUT_CSV [--limit K] [--retry-errors]
--retry-errors reruns only trials marked "error" in an existing OUT_CSV and merges the results.
Each cluster's skills are installed in a fresh git repo under .opencode/skills/<name>/SKILL.md
(real name + description, stub body). The chosen skill is read from command_execution events.
"""
import os, csv, json, re, subprocess, sys, tempfile, shutil, pathlib
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL = os.environ.get("OPENCODE_MODEL", "opencode/deepseek-v4.1-flash-free")
BODY = "Stub skill for an evaluation. Reply with the single line 'done' and do nothing else.\n"

group, n, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None

tasks = [t for t in map(json.loads, open(ROOT / "data/golden.jsonl")) if t["group"] == group]
if limit: tasks = tasks[:limit]
skills = {}
for r in csv.DictReader(open(ROOT / "data/selected200.csv")):
    skills.setdefault(r["group"], []).append(r)

def workdir(cluster):
    d = pathlib.Path(tempfile.mkdtemp(prefix=f"codex_{cluster}_"))
    for s in skills[cluster]:
        p = d / ".opencode/skills" / s["name"]
        p.mkdir(parents=True)
        desc = s["description"].replace('"', '\\"').replace("\n", " ")
        (p / "SKILL.md").write_text(f'---\nname: {s["name"]}\ndescription: "{desc}"\n---\n\n{BODY}')
    subprocess.run(["git", "init", "-q"], cwd=d, check=True)
    return d

def run(job):
    t, trial, d = job
    for attempt in range(2):
        # own data dir per trial: opencode's shared sqlite db locks under parallel runs
        data = tempfile.mkdtemp(prefix="oc_data_")
        try:
            pr = subprocess.run(["opencode", "run", "-m", MODEL, "--format", "json", t["request"]],
                                capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL, cwd=d,
                                env={**os.environ, "PWD": str(d), "XDG_DATA_HOME": data})
            chosen, err_ev = [], ""
            for line in pr.stdout.splitlines():
                try: ev = json.loads(line)
                except ValueError: continue
                p = ev.get("part", {})
                if ev.get("type") == "tool_use" and p.get("tool") == "skill":
                    chosen.append(p["state"]["input"].get("name", ""))
                if ev.get("type") == "error": err_ev = str(ev)[:200]
            err = err_ev or ("" if pr.returncode == 0 else pr.stderr[-200:])
        except subprocess.TimeoutExpired:
            chosen, err = [], "timeout"
        finally:
            shutil.rmtree(data, ignore_errors=True)
        if "database is locked" not in err: break
    first = chosen[0] if chosen else ""
    ok = {*t["gold_names"], *t["acceptable_names"]}
    outcome = "error" if err and not chosen else "correct" if first in ok else "wrong" if first else "no_skill"
    return dict(id=t["id"], cluster=t["cluster_id"], tier=t["tier"], trial=trial, request=t["request"],
                gold="|".join(t["gold_names"]), acceptable="|".join(t["acceptable_names"]),
                chosen_first=first, all_loaded="|".join(dict.fromkeys(chosen)), outcome=outcome, error=err)

dirs = {c: workdir(c) for c in {t["cluster_id"] for t in tasks}}
jobs = [(t, i + 1, dirs[t["cluster_id"]]) for t in tasks for i in range(n)]
prev = {}
if "--retry-errors" in sys.argv:
    prev = {(r["id"], int(r["trial"])): r for r in csv.DictReader(open(out))}
    jobs = [j for j in jobs if prev[(j[0]["id"], j[1])]["outcome"] == "error"]
    print(f"retrying {len(jobs)} errored trials")
with ThreadPoolExecutor(6) as ex: new = list(ex.map(run, jobs))
for r in new: prev[(r["id"], r["trial"])] = r
rows = list(new) if not prev else [prev[(t["id"], i + 1)] for t in tasks for i in range(n)]
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for d in dirs.values(): shutil.rmtree(d, ignore_errors=True)
from collections import Counter
print(Counter(r["outcome"] for r in rows))

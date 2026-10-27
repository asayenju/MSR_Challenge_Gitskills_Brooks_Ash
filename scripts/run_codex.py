"""Run golden requests for one group on Codex CLI and score which skill it loaded.

Usage: run_codex.py GROUP N_TRIALS OUT_CSV [--limit K]
Each cluster's skills are installed in a fresh git repo under .agents/skills/<name>/SKILL.md
(real name + description, stub body). The chosen skill is read from command_execution events.
"""
import csv, json, re, subprocess, sys, tempfile, shutil, pathlib
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL = "gpt-5.6-terra"
BODY = "Stub skill for an evaluation. Reply with the single line 'done' and do nothing else.\n"
SKILL_RE = re.compile(r"skills/([\w.-]+)/SKILL\.md")

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
        p = d / ".agents/skills" / s["name"]
        p.mkdir(parents=True)
        desc = s["description"].replace('"', '\\"').replace("\n", " ")
        (p / "SKILL.md").write_text(f'---\nname: {s["name"]}\ndescription: "{desc}"\n---\n\n{BODY}')
    subprocess.run(["git", "init", "-q"], cwd=d, check=True)
    return d

def run(job):
    t, trial, d = job
    try:
        pr = subprocess.run(["codex", "exec", "-m", MODEL, "--json", "--ephemeral", "-s", "read-only", "-C", str(d), t["request"]],
                            capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL)
        chosen = []
        for line in pr.stdout.splitlines():
            try: ev = json.loads(line)
            except ValueError: continue
            it = ev.get("item", {})
            if it.get("type") == "command_execution":
                chosen += SKILL_RE.findall(it.get("command", ""))
        err = "" if pr.returncode == 0 else pr.stderr[-200:]
    except subprocess.TimeoutExpired:
        chosen, err = [], "timeout"
    first = chosen[0] if chosen else ""
    ok = {*t["gold_names"], *t["acceptable_names"]}
    outcome = "error" if err and not chosen else "correct" if first in ok else "wrong" if first else "no_skill"
    return dict(id=t["id"], cluster=t["cluster_id"], tier=t["tier"], trial=trial, request=t["request"],
                gold="|".join(t["gold_names"]), acceptable="|".join(t["acceptable_names"]),
                chosen_first=first, all_loaded="|".join(dict.fromkeys(chosen)), outcome=outcome, error=err)

dirs = {c: workdir(c) for c in {t["cluster_id"] for t in tasks}}
jobs = [(t, i + 1, dirs[t["cluster_id"]]) for t in tasks for i in range(n)]
with ThreadPoolExecutor(6) as ex: rows = list(ex.map(run, jobs))
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for d in dirs.values(): shutil.rmtree(d, ignore_errors=True)
from collections import Counter
print(Counter(r["outcome"] for r in rows))

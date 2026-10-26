import csv, json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from qa import QA; from qb import QB; from qc import QC, D; from qe import QE, QN
src = open(os.path.join(os.path.dirname(__file__),'draft_pilot.py')).read()
ns = {}; exec(src[src.index('Q = ['):src.index('def toks')], ns)
rows = list(csv.DictReader(open('data/selected200.csv')))
cl = {}
for r in rows: cl.setdefault(r['group'], []).append(r)
by = {(r['group'], r['name']): r for r in rows}
items = []   # (cluster, gold|'*'|None, tier, request, note, acc)
for c,g,t,q,n in ns['Q']: items.append((c,g,t,q,n,[]))
items += QA+QB+QC+QE
for c,qs in D.items():
    for q in qs: items.append((c,'*','clear',q,'any copy is correct',[]))
for c,q,n in QN: items.append((c,None,'clear',q,'negative: '+n,[]))
def toks(s): return re.findall(r'[a-z0-9]+', s.lower())
def ng(t,n): return {tuple(t[i:i+n]) for i in range(len(t)-n+1)}
out=[]; cnt={}
for c,g,tier,req,note,acc in items:
    neg = g is None
    grp = 'N' if neg else c[0]
    cnt[grp]=cnt.get(grp,0)+1
    rid=f"{grp}-{c}-{cnt[grp]:03d}"
    if neg: gold=[];names=[]
    elif g=='*': gold=[r['file_sha'] for r in cl[c]]; names=[r['name']+' ('+r['repo']+')' for r in cl[c]]
    else:
        assert (c,g) in by, (c,g); gold=[by[(c,g)]['file_sha']]; names=[g]
    accsha=[]
    for a in acc:
        assert (c,a) in by,(c,a); accsha.append(by[(c,a)]['file_sha'])
    flags=[]
    for r in cl[c]:
        if g!='*' and r['name'].lower() in req.lower(): flags.append('name:'+r['name'])
    for gs in gold:
        d=[r for r in cl[c] if r['file_sha']==gs][0]['description']
        ov=ng(toks(req),4)&ng(toks(d),4)
        if ov: flags.append('4gram:'+' '.join(sorted(ov)[0]))
    out.append(dict(id=rid,group=grp,cluster_id=c,request=req,gold=gold,gold_names=names,acceptable=accsha,acceptable_names=acc,tier=tier,
      should_trigger=not neg,drafter_model='claude-sonnet-5-5',blind_labels=[],status='draft',notes=note,lint=flags))
ids=[o['id'] for o in out]; assert len(ids)==len(set(ids))
reqs=[o['request'] for o in out]; assert len(reqs)==len(set(reqs)),[r for r in reqs if reqs.count(r)>1]
print({g:cnt[g] for g in sorted(cnt)}, 'total',len(out))
exp={'A':48,'B':48,'C':48,'D':48,'E':56,'N':25}
assert cnt==exp,(cnt,exp)
# every skill covered at least once as gold (non-D) / per-skill counts
from collections import Counter
for g in 'ABCE':
    gc=Counter(n for o in out if o['group']==g for n in o['gold_names'])
    sk={(r['name']) for r in rows if r['group'][0]==g}
    miss=sk-set(gc); print(g,'skills without a question:',miss or 'none')
os.makedirs('data/golden',exist_ok=True)
with open('data/golden.jsonl','w') as f:
    for o in out: f.write(json.dumps(o)+'\n')
for p in ('data/golden_pilot.jsonl','docs/golden-pilot-review.md'):
    if os.path.exists(p): os.remove(p)
os.makedirs('docs/golden-review',exist_ok=True)
titles={'A':'A. Cross-repo rivals','B':'B. Same-pack siblings','C':'C. Template families','D':'D. Fork variants','E':'E. Isolated controls','N':'N. Negatives (no skill should load)'}
for grp in 'ABCDEN':
    clusters=sorted({o['cluster_id'] for o in out if o['group']==grp},key=lambda s:(s[0],int(s[1:])))
    md=[f"# {titles[grp]}: review sheet\n","Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.\n",
        "Mark each row **Agree** (gold is right), **Alt** (another installed skill also acceptable: name it) or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.\n"]
    for c in clusters:
        md.append(f"\n## {c}\n\nInstalled skills:\n")
        for r in cl[c]: md.append(f"- **{r['name']}** ({r['repo']}): {' '.join(r['description'].split())}")
        md.append("\n| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |\n|---|---|---|---|---|---|---|")
        for o in out:
            if o['cluster_id']==c and o['group']==grp:
                gold='NONE' if not o['should_trigger'] else ('any of the 4 copies' if len(o['gold'])>1 else o['gold_names'][0])
                md.append(f"| {o['id']} | {o['request']} | {gold} | {', '.join(o['acceptable_names']) or ''} | {o['tier']} | {', '.join(o['lint']) or 'ok'} | |")
    open(f'docs/golden-review/{grp}.md','w').write('\n'.join(md)+'\n')
print('lint flags:'); 
for o in out:
    if o['lint'] and o['group']!='D': print(' ',o['id'],o['lint'])
print('tiers',Counter((o['group'],o['tier']) for o in out))

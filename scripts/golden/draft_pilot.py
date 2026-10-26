import csv, json, re
rows = list(csv.DictReader(open('data/selected200.csv')))
by = {(r['group'], r['name']): r for r in rows}
cl = {}
for r in rows: cl.setdefault(r['group'], []).append(r)

# (cluster, gold name or "*" for all copies / None for negative, tier, request, note)
Q = [
 ("A1","analysis-api-create-cherry-pick-issue","boundary","I just fixed a bug in the Kotlin Analysis API and it has to be backported to the IntelliJ branch. Can you file the ticket that tracks getting it over there?","decoys: release tracker, QA table"),
 ("A1","qa-cherry-picks","clear","We're moving our polkadot-sdk fork to the next stable branch. Go through the table of patches we carry and check which ones are already upstream and which still need applying.",""),
 ("A1","release-create-tracker-issue","boundary","Turn this PyTorch release announcement into the issue where we'll track everything that lands on the release branch.","decoys: Kotlin tracker issue, QA table"),
 ("A1","cherry-pick-release","clear","We're getting ready to go live: branch off main, bring across just the approved commits from the test branch, and confirm the result matches what test had.",""),
 ("B1","dca","clear","Put $25 into each of these five coins every week, but stop topping up any coin once it hits its limit.",""),
 ("B1","whale-watcher","clear","Notify me when a large holder dumps a coin I'm following, and sell my position automatically if it happens.",""),
 ("B1","watchlist","boundary","Let me know whenever any coin I'm following passes a $10M market cap.","decoys: whale-watcher, trend-sniper"),
 ("B1","trend-sniper","boundary","Whenever a brand-new coin starts going viral, buy a small amount of it for me right away, within a fixed budget.","decoys: dca, watchlist"),
 ("C1","fret-workstream-lifecycle","clear","I paused a big refactor effort last week. Pick it back up and re-check what's still true before touching anything.",""),
 ("C1","fret-workstream-lifecycle","clear","This line of work is finished. Write the wrap-up notes so nobody accidentally reopens its scope.",""),
 ("C1","fret-mobile-real-device-debug","clear","The rendering glitch only reproduces on my Pixel and an iPhone. Get the smallest build running on both and collect logs I can attach to the design record.",""),
 ("C1","fret-mobile-real-device-debug","boundary","Check that our GPU backend assumptions actually hold on physical phones, not simulators.","decoy: boundary-checks"),
 ("C1","fret-boundary-checks","clear","Before I start restructuring code that spans several crates, make sure the platform windowing library hasn't leaked into the portable core.",""),
 ("C1","fret-boundary-checks","clear","Did my last change break any crate layering rules? Report any drift.",""),
 ("C1","fret-repo-orientation","clear","I'm new to this codebase. Where should a keyboard-shortcut feature live, and what's the quickest demo to try it in?",""),
 ("C1","fret-repo-orientation","boundary","Which crate owns text input, and what's the fastest thing I can run to iterate on it?","decoy: boundary-checks"),
 ("D1","*","clear","Ship the new version: run the checks, publish to npm, create the GitHub release, smoke test it, and send word to everyone afterwards.",""),
 ("D1","*","clear","Leadership wants this version out today. Take it from final verification all the way through to announcing it.",""),
 ("D1","*","clear","Do the full release for this package: test it, publish it, and make sure the published build actually works.",""),
 ("D1","*","clear","We're cutting a release; coordinate everything from CI checks to the npm publish to the post-release comms.",""),
 ("D1","*","clear","Version 2.4 is approved. Handle the whole rollout, including smoke-testing what ends up on the registry.",""),
 ("D1","*","clear","I need this release to go out end to end: checks, registry, GitHub, and telling people about it.",""),
 ("D1","*","clear","Time to ship: get this tagged build verified, released, and announced.",""),
 ("D1","*","clear","Walk the release through every stage after merge: verify, publish to npm, GitHub release page, smoke test, comms.",""),
 ("E1","messageprotocol-core","clear","My serializer throws an InvalidCastException when I dispatch a message through the generic registration path in the runtime library. Help me track it down.",""),
 ("E1","spec-guide","clear","Turn this feature description into the repo's runnable implementation spec doc, checked against what's actually in src first.",""),
 ("E1","hal-and-abstractions","clear","I'm adding a new settings screen to the firmware. Make sure it goes through the hardware abstraction and theming layers rather than calling the SDK directly.",""),
 ("E1","catalyst-changelog-sync","clear","Review the recently archived changes in the sibling repos, decide which deserve a customer-facing changelog entry, and draft English and Spanish text.",""),
 ("A1",None,"clear","What does cherry-picking mean in git, and when is it a bad idea?","negative: conceptual question, no action"),
 ("B1",None,"clear","What is market capitalization and how is it calculated?","negative: conceptual question"),
 ("D1",None,"clear","What version number should this release get: is it a minor or a patch bump?","negative: skill says not merely discussing versioning"),
 ("C1",None,"clear","Rename the variable tmp to buffer throughout this file.","negative: unrelated edit"),
 ("E1",None,"clear","Explain the difference between TCP and UDP.","negative: unrelated"),
]
def toks(s): return re.findall(r'[a-z0-9]+', s.lower())
def ngrams(t,n): return {tuple(t[i:i+n]) for i in range(len(t)-n+1)}
out=[]; n=0
for c,g,tier,req,note in Q:
    n+=1
    if g is None: gold=[];names=[]
    elif g=="*": gold=[r['file_sha'] for r in cl[c]]; names=[r['name']+' ('+r['repo']+')' for r in cl[c]]
    else: gold=[by[(c,g)]['file_sha']]; names=[g]
    gid=c[0]; neg=g is None
    rid=f"{'N' if neg else gid}-{c}-{n:03d}"
    # leakage check vs gold description(s) and names
    flags=[]
    for r in cl[c]:
        if r['name'].lower() in req.lower(): flags.append('name:'+r['name'])
    for gs in (gold or []):
        d=[r for r in cl[c] if r['file_sha']==gs][0]['description']
        ov=ngrams(toks(req),3)&ngrams(toks(d),3)
        if ov: flags.append('3gram:'+' '.join(sorted(ov)[0]))
    out.append(dict(id=rid,group=gid if not neg else 'N',cluster_id=c,request=req,gold=gold,gold_names=names,acceptable=[],tier=tier,
        should_trigger=not neg,drafter_model='claude-sonnet-5-5',blind_labels=[],status='draft',notes=note,lint=flags))
with open('data/golden_pilot.jsonl','w') as f:
    for o in out: f.write(json.dumps(o)+'\n')
# review sheet
md=["# Golden pilot: review sheet\n","Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.\n",
"For each row, mark **Agree** (gold is right), **Alt** (another installed skill is also acceptable: say which), or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.\n"]
for c in ['A1','B1','C1','D1','E1']:
    md.append(f"\n## {c}\n\nInstalled skills and descriptions:\n")
    for r in cl[c]: md.append(f"- **{r['name']}** ({r['repo']}): {r['description'].strip()}")
    md.append("\n| ID | Request | Gold | Tier | Lint | Your verdict |\n|---|---|---|---|---|---|")
    for o in out:
        if o['cluster_id']==c:
            gold='NONE (negative)' if not o['should_trigger'] else ('any of the 4 copies' if len(o['gold'])>1 else o['gold_names'][0])
            md.append(f"| {o['id']} | {o['request']} | {gold} | {o['tier']} | {', '.join(o['lint']) or 'ok'} | |")
open('docs/golden-pilot-review.md','w').write('\n'.join(md)+'\n')
print(len(out),'questions;', sum(1 for o in out if o['lint']),'with lint flags')
for o in out:
    if o['lint']: print(o['id'],o['lint'])

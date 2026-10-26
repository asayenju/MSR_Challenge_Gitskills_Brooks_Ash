import re, json, duckdb, numpy as np, pandas as pd
c=duckdb.connect(); c.execute("INSTALL httpfs; LOAD httpfs;")
repos=c.execute("select full_name, stars, is_fork, license, language from read_parquet('hf://datasets/mvaccargiu/gitskills/data/repos/*.parquet')").df()
df=pd.read_parquet('data/sample100k.parquet').merge(repos,left_on='repo_full_name',right_on='full_name',how='left')
df['stars']=df.stars.fillna(0).astype(int)
nbr=np.load('data/nbr.npy'); sim=np.load('data/sim.npy')
assert len(df)==len(nbr)
repo=df.repo_full_name.astype(object).values; nm=df.name.astype(object).values; ds=df.description.astype(object).values
st=df.stars.values
tok=lambda s:set(re.findall(r'[a-z0-9]+',s.lower()))
ntok=[tok(x) for x in nm]
def samename(i,j):
    a,b=ntok[i],ntok[j]
    if not a or not b: return False
    return len(a&b)/len(a|b)>=0.5 or a<=b or b<=a
startswith_use_when=lambda d: False
bad=lambda i: bool(re.search(r'cluster[-_ ]?\d|cli-anything|^skill$|test',nm[i].lower())) or len(ds[i])<60 or 'symbols across' in ds[i] or 'fixture' in ds[i].lower() or startswith_use_when(ds[i])
used=set(); out=[]
def take(group,gid,label):
    for i in group: used.add(i)
    out.append(dict(group=gid,type=label,members=[int(i) for i in group]))
# A: cross-repo rivals
def rivals(i):
    r=[];seenr={repo[i]};seenn=[i]
    for k in range(sim.shape[1]):
        j=int(nbr[i,k]); s=sim[i,k]
        if j in used or bad(j) or not(0.33<=s<=0.75) or repo[j] in seenr: continue
        if any(samename(j,q) for q in seenn): continue
        r.append(j);seenr.add(repo[j]);seenn.append(j)
    return r
seeds=[i for i in np.argsort(-st) if st[i]>=20 and not bad(i)]
nA=0;topics=[]
for i in seeds:
    if nA>=6: break
    if i in used: continue
    r=rivals(i)
    if len(r)>=3:
        g=[i]+r[:3]
        words=set().union(*[ntok[x] for x in g])
        if any(len(words&t)>=2 for t in topics): continue
        topics.append(words); take(g,f'A{nA+1}','cross_repo_rivals'); nA+=1
# B: same-repo siblings
nB=0
for i in seeds:
    if nB>=6: break
    if i in used: continue
    r=[];sn=[i]
    for k in range(sim.shape[1]):
        j=int(nbr[i,k]);s=sim[i,k]
        if j in used or bad(j) or repo[j]!=repo[i] or not(0.3<=s<=0.7) or any(samename(j,q) for q in sn): continue
        r.append(j);sn.append(j)
    if len(r)>=3:
        take([i]+r[:3],f'B{nB+1}','same_pack_siblings'); nB+=1
# C: template families (same repo, shared 3-word description prefix, many members)
df['pre']=[' '.join(re.findall(r'[a-z]+',d.lower())[:3]) for d in ds]
cnt=df.groupby(['repo_full_name','pre']).size().reset_index(name='n').query('n>=8').sort_values('n',ascending=False)
nC=0
for _,row in cnt.iterrows():
    if nC>=3: break
    if len(row.pre.split())<3 or row.pre.startswith('use this'): continue
    m=df[(df.repo_full_name==row.repo_full_name)&(df.pre==row.pre)].index.tolist()
    m=[x for x in m if x not in used and not bad(x)][:4]
    if len(m)==4: take(m,f'C{nC+1}','template_family'); nC+=1
# D: fork variants (same name, different repos, sim>=0.6)
nD=0
for i in seeds:
    if nD>=3: break
    if i in used: continue
    r=[];seenr={repo[i]}
    for k in range(sim.shape[1]):
        j=int(nbr[i,k])
        if j in used or bad(j) or sim[i,k]<0.6 or repo[j] in seenr or not samename(i,j): continue
        r.append(j);seenr.add(repo[j])
    if len(r)>=3: take([i]+r[:3],f'D{nD+1}','fork_variants'); nD+=1
# E: isolated random controls
rng=np.random.default_rng(1)
iso=[i for i in rng.permutation(len(df)) if sim[i,0]<0.12 and not bad(i) and i not in used and len(ds[i])>=80]
pool=[];rs=set()
for i in iso:
    if repo[i] in rs: continue
    pool.append(i);rs.add(repo[i])
    if len(pool)==28: break
for g in range(7): take(pool[g*4:g*4+4],f'E{g+1}','isolated_control')
rows=[]
for g in out:
    for i in g['members']:
        rows.append(dict(group=g['group'],type=g['type'],idx=i,repo=repo[i],path=df.path[i],name=nm[i],stars=int(st[i]),license=df.license[i],description=ds[i],file_sha=df.file_sha[i]))
sel=pd.DataFrame(rows); sel.to_parquet('data/selected100.parquet'); sel.to_csv('data/selected100.csv',index=False)
print(sel.groupby('type').size())
for g,d in sel.groupby('group',sort=False):
    print(f"\n== {g} {d.type.iloc[0]}")
    for _,r in d.iterrows(): print(f"  [{r.stars}★ {r.repo}] {r['name']}: {r.description[:110]}")

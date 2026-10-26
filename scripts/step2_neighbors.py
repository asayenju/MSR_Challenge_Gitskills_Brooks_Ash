import duckdb, numpy as np, pandas as pd, scipy.sparse as sp, pickle
from sklearn.feature_extraction.text import TfidfVectorizer
c = duckdb.connect()
# English-ish, standard-ish, cap 20/repo, dedup normalized description, random 100K
df = c.execute("""
WITH f AS (
  SELECT *, lower(trim(description)) nd FROM 'data/skills_clean.parquet'
  WHERE NOT regexp_matches(description,'[^\\x00-\\x7F]') AND length(description) BETWEEN 40 AND 600
    AND name IS NOT NULL
), d AS (SELECT *, row_number() OVER (PARTITION BY nd ORDER BY hash(repo_full_name||path)) rn_d FROM f),
r AS (SELECT *, row_number() OVER (PARTITION BY repo_full_name ORDER BY hash(path||'x')) rn_r FROM d WHERE rn_d=1)
SELECT * EXCLUDE (rn_d, rn_r) FROM r WHERE rn_r<=20 ORDER BY hash(repo_full_name||path||'s') LIMIT 100000
""").df()
print(len(df), df.repo_full_name.nunique())
txt = (df.name.fillna('') + ' ' + df.description).tolist()
vec = TfidfVectorizer(lowercase=True, stop_words='english', ngram_range=(1,2), min_df=3, max_df=0.05, sublinear_tf=True)
X = vec.fit_transform(txt).astype(np.float32).tocsr()
print(X.shape)
K=10; n=X.shape[0]; nbr=np.zeros((n,K),dtype=np.int32); sim=np.zeros((n,K),dtype=np.float32)
XT = X.T.tocsc()
for s in range(0,n,2000):
    M = (X[s:s+2000] @ XT).toarray()
    for i in range(M.shape[0]): M[i, s+i] = -1
    idx = np.argpartition(-M, K, axis=1)[:, :K]
    v = np.take_along_axis(M, idx, 1)
    o = np.argsort(-v, 1)
    nbr[s:s+2000] = np.take_along_axis(idx,o,1); sim[s:s+2000] = np.take_along_axis(v,o,1)
df.to_parquet('data/sample100k.parquet'); np.save('data/nbr.npy',nbr); np.save('data/sim.npy',sim)
print(np.percentile(sim[:,0],[10,25,50,75,90,99]))

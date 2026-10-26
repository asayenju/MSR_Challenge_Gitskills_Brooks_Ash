import sys, duckdb
out = sys.argv[1]
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
src = "hf://datasets/mvaccargiu/gitskills/data/artifacts/*.parquet"
con.execute(f"""
COPY (
  SELECT repo_full_name, path, filename, location_class, file_sha, name, description,
         body_chars, has_scripts, has_references, commit_count, sibling_count
  FROM read_parquet('{src}')
  WHERE dedup_primary=1 AND frontmatter_valid=1
    AND description IS NOT NULL AND length(trim(description))>=20
) TO '{out}' (FORMAT parquet)
""")
print(con.execute(f"select count(*), count(distinct repo_full_name) from read_parquet('{out}')").fetchall())

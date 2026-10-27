"""pass@k / pass^k from a results CSV. Usage: metrics.py RESULTS_CSV"""
import csv, sys
from math import comb
from collections import defaultdict

by = defaultdict(list)
for r in csv.DictReader(open(sys.argv[1])):
    by[r["id"]].append(r["outcome"] == "correct")
n = min(len(v) for v in by.values())
print(f"{len(by)} tasks, n={n} trials each")
for k in range(1, n + 1):
    at = sum(1 - comb(n - sum(v[:n]), k) / comb(n, k) for v in by.values()) / len(by)
    hat = sum(comb(sum(v[:n]), k) / comb(n, k) for v in by.values()) / len(by)
    print(f"k={k}: pass@k={at:.3f}  pass^k={hat:.3f}")

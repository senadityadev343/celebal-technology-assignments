from itertools import groupby
import sys

def encode(s: str) -> str:
    p = []
    for d, g in groupby(s):
        c = sum(1 for _ in g)
        p.append(f"({c}, {d})")
    return " ".join(p)

for l in sys.stdin:
    print(encode(l.strip()))

from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import os
from heapq import heappush, heappop

adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))
adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def lmap(f, it):
    return list(map(f, it))


def ints(txt):
    return lmap(int, txt)


def make_indexer(lst, default=None):
    def get(*indices):
        cur = lst
        for i in indices:
            if 0 <= i < len(cur):
                cur = cur[i]
            else:
                return default
        return cur

    return get


def solve(input):
    M = 10 ** 9

    parts = input.split("\n\n")
    xs = ints(parts[0].split(","))
    boards = [
        [ints(lines[i].split()) for i in range(5)]
        for lines in map(lambda p: p.split("\n"), parts[1:])
    ]

    last_ans = 0
    for x in xs:
        nxt = []
        for b in boards:
            for i, j in itertools.product(range(5), repeat=2):
                if b[i][j] == x:
                    b[i][j] = M
            good = any(row.count(M) == 5 for row in b) or any(
                col.count(M) == 5 for col in zip(*b)
            )
            if good:
                last_ans = sum(v for v in itertools.chain(*b) if v != M) * x
            else:
                nxt.append(b)

        boards = nxt
        if not boards:
            break
    return last_ans


cur_dir = os.path.dirname(os.path.realpath(__file__))

print("SAMPLE OUTPUT")
with open(os.path.join(cur_dir, "sample.txt")) as f:
    print(solve(f.read()))

print("---")

print("OUTPUT")
with open(os.path.join(cur_dir, "input.txt")) as f:
    print(solve(f.read()))

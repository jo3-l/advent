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
    lies_on = defaultdict(int)
    for l in input.split("\n"):
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", l))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lies_on[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                lies_on[x, y1] += 1
    return sum(1 for v in lies_on.values() if v >= 2)


cur_dir = os.path.dirname(os.path.realpath(__file__))

print("SAMPLE OUTPUT")
with open(os.path.join(cur_dir, "sample.txt")) as f:
    print(solve(f.read().strip()))

print("---")

print("OUTPUT")
with open(os.path.join(cur_dir, "input.txt")) as f:
    print(solve(f.read().strip()))

from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import os
import statistics
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


def get_completion_points(s):
    open, close = "([{<", ")]}>"
    stk = []
    for c in s:
        if c in open:
            stk.append(close[open.index(c)])
        elif not stk or stk.pop() != c:
            return 0
    score = 0
    for c in reversed(stk):
        score *= 5
        score += close.index(c) + 1
    return score


def solve(input):
    return statistics.median(
        filter(bool, (get_completion_points(s) for s in input.split()))
    )


cur_dir = os.path.dirname(os.path.realpath(__file__))

print("SAMPLE OUTPUT")
with open(os.path.join(cur_dir, "sample.txt")) as f:
    print(solve(f.read().strip()))

print("---")

print("OUTPUT")
with open(os.path.join(cur_dir, "input.txt")) as f:
    print(solve(f.read().strip()))

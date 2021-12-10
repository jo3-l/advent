import re
from collections import defaultdict


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    lies_on = defaultdict(int)
    for l in input.split("\n"):
        x1, y1, x2, y2 = ints(re.findall(r"\d+", l))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lies_on[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                lies_on[x, y1] += 1
    return sum(1 for v in lies_on.values() if v >= 2)

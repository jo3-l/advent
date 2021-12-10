import re
from collections import defaultdict


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def points_on_line(x1, y1, x2, y2):
    if x1 == x2:
        yield from ((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
    elif y1 == y2:
        yield from ((y1, x) for x in range(min(x1, x2), max(x1, x2) + 1))
    else:
        dx = 1 if x1 < x2 else -1
        dy = 1 if y1 < y2 else -1
        yield from zip(range(x1, x2 + dx, dx), range(y1, y2 + dy, dy))


def solve(input):
    lies_on = defaultdict(int)
    for l in input.split("\n"):
        for x, y in points_on_line(*ints(re.findall(r"\d+", l))):
            lies_on[x, y] += 1
    return sum(1 for v in lies_on.values() if v >= 2)

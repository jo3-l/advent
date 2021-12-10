import re
from functools import cache


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


@cache
def F(d, s):
    reset_at = d - s - 1
    if reset_at < 0:
        return 1
    return F(reset_at, 6) + F(reset_at, 8)


def solve(input):
    return sum(F(8, x) for x in ints(re.findall(r"-?\d+", input)))

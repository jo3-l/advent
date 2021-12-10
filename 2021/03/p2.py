from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import sys
import operator


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


with open(sys.argv[1]) as f:
    input = f.read()


def solve(input):
    l = len(input.split()[0])
    xs = lmap(lambda x: int(x, 2), input.split())

    def calc(choose, pref):
        selected = xs
        i = l - 1
        while i >= 0 and len(selected) > 1:
            cnt = [0, 0]
            for x in selected:
                cnt[(x >> i) & 1] += 1
            f = pref if cnt[0] == cnt[1] else int(choose(cnt[1], cnt[0]))
            selected = [x for x in selected if ((x >> i) & 1) == f]
            i -= 1
        return selected[0]

    return calc(operator.gt, 1) * calc(operator.lt, 0)


print(solve(input.rstrip("\n")))

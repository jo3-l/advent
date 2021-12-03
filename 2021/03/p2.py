from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import sys
import operator


def lmap(f, it):
    return list(map(f, it))


def ints(txt):
    return lmap(int, txt)


with open(sys.argv[1]) as f:
    input = f.read()


def solve(input):
    l = len(input.split()[0])
    xs = lmap(lambda x: int(x, 2), input.split())

    def calc(choose, pref):
        selected = xs
        for i in range(l - 1, -1, -1):
            cnt = [0, 0]
            for x in selected:
                cnt[(x >> i) & 1] += 1
            f = 0
            if choose(cnt[1], cnt[0]):
                f = 1
            elif choose(cnt[0], cnt[1]):
                f = 0
            else:
                f = pref
            selected = [x for x in selected if ((x >> i) & 1) == f]
            if len(selected) == 1:
                return selected[0]

    return calc(operator.gt, 1) * calc(operator.lt, 0)


print(solve(input.rstrip("\n")))

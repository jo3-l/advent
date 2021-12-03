from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import sys


def lmap(f, it):
    return list(map(f, it))


def ints(txt):
    return lmap(int, txt)


with open(sys.argv[1]) as f:
    input = f.read()


def solve(input):
    l = len(input.split()[0])
    xs = lmap(lambda x: int(x, 2), input.split())
    a = b = 0
    for i in range(l):
        cnt = [0, 0]
        for x in xs:
            cnt[(x >> i) & 1] += 1
        if cnt[1] > cnt[0]:
            a |= 1 << i
        else:
            b |= 1 << i

    return a * b


print(solve(input.rstrip("\n")))

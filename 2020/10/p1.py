from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    xs = list(map(int, input.split()))
    xs.append(0)
    xs.sort()
    xs.append(xs[-1] + 3)
    ctr = defaultdict(int)
    for a, b in zip(xs, xs[1:]):
        ctr[b - a] += 1
    return ctr[1] * ctr[3]


print(solve(input.rstrip("\n")))

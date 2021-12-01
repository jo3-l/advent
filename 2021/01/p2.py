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
    cnt = 0
    for i in range(len(xs) - 3):
        window = sum(xs[i : i + 3])
        nxt = sum(xs[i + 1 : i + 4])
        if nxt > window:
            cnt += 1
    return cnt


print(solve(input.rstrip("\n")))

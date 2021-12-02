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
    h_pos = depth = aim = 0
    for inst in input.split("\n"):
        typ, n = inst.split()
        n = int(n)
        if typ == "forward":
            h_pos += n
            depth += aim * n
        elif typ == "down":
            aim += n
        else:
            aim -= n
    return h_pos * depth


print(solve(input.rstrip("\n")))

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
    ...


print(solve(input.rstrip("\n")))

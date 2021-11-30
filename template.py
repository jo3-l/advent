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
    ...


print(solve(input.rstrip("\n")))

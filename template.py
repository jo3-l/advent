import itertools
import math
import os
import re
from collections import Counter, defaultdict, deque
from functools import cache
from heapq import heappop, heappush

ONLY_SAMPLE = False

adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))
adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def solve(data: str):
    ...


cur_dir = os.path.dirname(os.path.realpath(__file__))


def normalize_input(data):
    # splitlines will get rid of unwanted trailing spaces.
    return "\n".join(data.splitlines())


print("SAMPLE OUTPUT")
with open(os.path.join(cur_dir, "sample.txt")) as file:
    data = normalize_input(file.read())
    print(solve(data))

if not ONLY_SAMPLE:
    print("---")

    print("OUTPUT")
    with open(os.path.join(cur_dir, "input.txt")) as file:
        data = normalize_input(file.read())
        print(solve(data))

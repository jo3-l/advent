# ruff: noqa: F401
import itertools
import math
import os
import re
import sys
import pyperclip
import z3
from collections import Counter, defaultdict, deque
from functools import cache
from heapq import heappop, heappush

sys.setrecursionlimit(100000)

####################
### UTILS BEGIN ####
####################

adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))
adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def paras(s: str):
    return s.split("\n\n")


class Bounds:
    """
    ```python
    bounds = Bounds.for2d(grid)
    (i, j) in bounds
    ```
    """

    def __init__(self, *dims: int):
        self.dims = dims

    def __contains__(self, idxs):
        assert len(idxs) == len(self.dims)
        for i, bound in zip(idxs, self.dims):
            if i < 0 or i >= bound:
                return False
        return True

    @staticmethod
    def for1d(arr):
        return Bounds(len(arr))

    @staticmethod
    def for2d(arr):
        return Bounds(len(arr), len(arr[0]))

    @staticmethod
    def for3d(arr):
        return Bounds(len(arr), len(arr[0]), len(arr[0][0]))


def ints(s: str):
    return list(map(int, re.findall(r"-?\d+", s)))


class Rx:
    r"""
    ```python
    n, items = input >> Rx(r"Monkey (.+): Starting items: (.+)", int, ints)
    ```
    """

    def __init__(self, rgx, *parsers):
        self.rgx = re.compile(rgx)
        self.parsers = parsers

    def __rrshift__(self, inp):
        m = self.rgx.match(inp)
        assert m, f"didn't match regex {self.rgx}"
        grps = m.groups()
        parsed = []
        for grp, parser in itertools.zip_longest(grps, self.parsers, fillvalue=str):
            parsed.append(parser(grp))
        return parsed


#######################
### SOLUTION BEGIN ####
#######################

r"""
adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))
adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))

paras(s)
ints(s)

bounds = Bounds.for2d(grid)
(i, j) in bounds

n, items = input >> Rx(r"Monkey (.+): Starting items: (.+)", int, ints)
"""

ONLY_SAMPLE = False
# ONLY_SAMPLE = True

### ^ uncomment to only run sample ###
######################################


def solve(data: str):
    lines = data.splitlines()
    for line in lines:
        pass

    return None


####################
### RUNNER BEGIN ###
####################

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

    print("OUTPUT [copied to clipboard]")
    with open(os.path.join(cur_dir, "input.txt")) as file:
        data = normalize_input(file.read())
        print(ans := solve(data))
        pyperclip.copy(ans)

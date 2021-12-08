from collections import defaultdict, Counter, deque
from functools import cache, reduce
import math
import re
import itertools
import os
from heapq import heappush, heappop

adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))
adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def lmap(f, it):
    return list(map(f, it))


def ints(txt):
    return lmap(int, txt)


def make_indexer(lst, default=None):
    def get(*indices):
        cur = lst
        for i in indices:
            if 0 <= i < len(cur):
                cur = cur[i]
            else:
                return default
        return cur

    return get


def solve(input):
    good = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]
    n = 0
    for l in input.split("\n"):
        observed, _, out = l.partition(" | ")
        observed = observed.split()
        for conf in itertools.permutations("abcdefg", 7):
            trans = str.maketrans(dict(zip(conf, "abcdefg")))
            if all("".join(sorted(w.translate(trans))) in good for w in observed):
                n += int(
                    "".join(
                        str(good.index("".join(sorted(w.translate(trans)))))
                        for w in out.split()
                    )
                )
    return n


cur_dir = os.path.dirname(os.path.realpath(__file__))

print("SAMPLE OUTPUT")
with open(os.path.join(cur_dir, "sample.txt")) as f:
    print(solve(f.read().strip()))

print("---")

print("OUTPUT")
with open(os.path.join(cur_dir, "input.txt")) as f:
    print(solve(f.read().strip()))

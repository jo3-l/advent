import os
from collections import defaultdict
from functools import cache

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    children = defaultdict(list)
    for l in input.split("\n"):
        n, _, c = l.partition(" contain ")
        parent = n.removesuffix(" bags")
        for xs in c.split(", "):
            amt, *child, _ = xs.split()
            if amt != "no":
                children[parent].append((int(amt), " ".join(child)))

    @cache
    def go(x):
        cnt = 1
        for n, c in children[x]:
            cnt += n * go(c)
        return cnt

    return go("shiny gold") - 1


print(solve(input.rstrip("\n")))

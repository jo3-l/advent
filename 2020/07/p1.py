import os
from collections import defaultdict

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    par = defaultdict(list)
    for l in input.split("\n"):
        n, _, c = l.partition(" contain ")
        parent = n.removesuffix(" bags")
        for child in c.split(", "):
            par[" ".join(child.split()[1:-1])].append(parent)

    seen = set()
    def go(x):
        for p in par[x]:
            if p not in seen:
                seen.add(p)
                go(p)

    go("shiny gold")
    return len(seen)


print(solve(input.rstrip("\n")))

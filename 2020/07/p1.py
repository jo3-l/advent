from collections import defaultdict


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

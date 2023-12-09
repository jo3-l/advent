import re


def solve(data: str):
    path, mapping = data.split("\n\n")
    graph = {}
    for line in mapping.splitlines():
        m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        assert m
        graph[m.group(1)] = (m.group(2), m.group(3))

    def dist_between(src: str, dst: str) -> int:
        cur = src
        nsteps = 0
        while cur != dst:
            dir = path[nsteps % len(path)]
            cur = graph[cur][dir == "R"]
            nsteps += 1
        return nsteps

    return dist_between("AAA", "ZZZ")

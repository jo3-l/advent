import re
import math


def solve(data: str):
    path, mapping = data.split("\n\n")
    graph = {}
    for line in mapping.splitlines():
        m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        assert m
        graph[m.group(1)] = (m.group(2), m.group(3))

    def dist_to_z(src: str) -> int:
        cur = src
        nsteps = 0
        while not cur.endswith("Z"):
            dir = path[nsteps % len(path)]
            cur = graph[cur][dir == "R"]
            nsteps += 1
        return nsteps

    lcm = 1
    for v in graph.keys():
        if v.endswith("A"):
            lcm = math.lcm(lcm, dist_to_z(v))
    return lcm

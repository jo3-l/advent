from collections import defaultdict


def solve(input):
    adj = defaultdict(list)
    for l in input.split("\n"):
        u, _, v = l.partition("-")
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u, vis):
        if u == "end":
            return 1
        n = 0
        for v in adj[u]:
            if v != "start":
                if v.islower():
                    if v not in vis:
                        n += dfs(v, {*vis, v})
                else:
                    n += dfs(v, vis)
        return n

    return dfs("start", set())


with open("input.txt") as f:
    print(solve(f.read().strip()))

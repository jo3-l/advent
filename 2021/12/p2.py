from collections import defaultdict, Counter


def solve(input):
    adj = defaultdict(list)
    for l in input.split("\n"):
        u, _, v = l.partition("-")
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u, ctr):
        if u == "end":
            return 1
        twice = any(v == 2 for k, v in ctr.items() if k.islower())
        n = 0
        for v in adj[u]:
            if v != "start":
                if v.islower():
                    lim = 1 if twice else 2
                    if ctr[v] < lim:
                        nxt = ctr.copy()
                        nxt[v] += 1
                        n += dfs(v, nxt)
                else:
                    n += dfs(v, ctr)
        return n

    return dfs("start", Counter())


with open("input.txt") as f:
    print(solve(f.read().strip()))

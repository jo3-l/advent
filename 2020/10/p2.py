from collections import defaultdict


def solve(input):
    xs = list(map(int, input.split()))
    xs.append(0)
    xs.sort()
    xs.append(xs[-1] + 3)

    dp = [0] * (len(xs) + 1)
    aux = defaultdict(int)
    aux[0] = dp[0] = 1
    for i in range(1, len(xs) + 1):
        dp[i] = sum(aux[xs[i - 1] - d] for d in range(1, 4))
        aux[xs[i - 1]] += dp[i]
    return dp[len(xs)]

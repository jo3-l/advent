from collections import defaultdict


def solve(input):
    xs = list(map(int, input.split()))
    xs.append(0)
    xs.sort()
    xs.append(xs[-1] + 3)
    ctr = defaultdict(int)
    for a, b in zip(xs, xs[1:]):
        ctr[b - a] += 1
    return ctr[1] * ctr[3]

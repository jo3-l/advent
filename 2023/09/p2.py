import itertools


def iterated_differences(initial: list[int]):
    hist = [initial]
    while any(v != 0 for v in hist[-1]):
        hist.append([b - a for a, b in itertools.pairwise(hist[-1])])
    return hist


def extrapolate_left(hist: list[list[int]]):
    diff = 0
    for seq in reversed(hist):
        diff = seq[0] - diff
    return diff


def solve(data: str):
    ans = 0
    for line in data.splitlines():
        nums = list(map(int, line.split()))
        hist = iterated_differences(nums)
        ans += extrapolate_left(hist)
    return ans

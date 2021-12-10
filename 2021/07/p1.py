import re


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    xs = ints(re.findall(r"\d+", input))
    lo, hi = min(xs), max(xs)

    def F(pos):
        return sum(abs(x - pos) for x in xs)

    while lo < hi:
        mid = (lo + hi + 1) // 2
        if F(mid) < F(mid - 1):
            lo = mid
        else:
            hi = mid - 1
    return F(lo)

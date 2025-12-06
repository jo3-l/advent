def isrepeat(n: int, k: int):
    s = str(n)
    return len(s) % k == 0 and s == s[: len(s) // k] * k


def solve1(s: str):
    ans = 0
    for range_ in s.split(","):
        lo, hi = map(int, range_.split("-"))
        for n in range(lo, hi + 1):
            if isrepeat(n, 2):
                ans += n
    return ans


def solve2(s: str):
    ans = 0
    for range_ in s.split(","):
        lo, hi = map(int, range_.split("-"))
        for n in range(lo, hi + 1):
            if any(isrepeat(n, k) for k in range(2, len(str(n)) + 1)):
                ans += n
    return ans

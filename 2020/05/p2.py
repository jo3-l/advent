import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def calc(cs, lo, hi, lc):
    for c in cs:
        mid = (lo + hi + 1) // 2
        if c == lc:
            hi = mid
        else:
            lo = mid
    return lo


def solve(input):
    ids = set()
    for p in input.split():
        r, c = calc(p[:7], 0, 127, "F"), calc(p[7:], 0, 7, "L")
        ids.add(r * 8 + c)
    return next(i + 1 for i in ids if i + 1 not in ids and i + 2 in ids)


print(solve(input.rstrip("\n")))

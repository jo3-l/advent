import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    xs = list(map(int, input.split()))
    xs.sort()
    for i, x in enumerate(xs):
        if i == 0 or i == len(xs) - 1:
            continue

        lo, hi = 0, len(xs) - 1
        while lo < i and i < hi:
            s = xs[lo] + xs[hi] + x
            if s > 2020:
                hi -= 1
            elif s == 2020:
                return xs[lo] * xs[hi] * x
            else:
                lo += 1


print(solve(input.rstrip("\n")))

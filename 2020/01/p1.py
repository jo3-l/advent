import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    seen = set()
    for x in map(int, input.split()):
        c = 2020 - x
        if c in seen:
            return c * x
        seen.add(x)


print(solve(input.rstrip("\n")))

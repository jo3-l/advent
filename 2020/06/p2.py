import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    ans = 0
    for g in input.split("\n\n"):
        x = (1 << 26) - 1
        for a_s in g.split("\n"):
            y = 0
            for c in a_s:
                y |= 1 << (ord(c) - ord("a"))
            x &= y
        ans += bin(x).count("1")
    return ans


print(solve(input.rstrip("\n")))

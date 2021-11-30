import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    ans = 0
    for g in input.split("\n\n"):
        b = 0
        for c in g:
            if c.isalpha():
                b |= 1 << (ord(c) - ord("a"))
        ans += bin(b).count("1")
    return ans


print(solve(input.rstrip("\n")))

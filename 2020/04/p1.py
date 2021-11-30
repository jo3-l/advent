import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    cnt = 0
    for p in input.split("\n\n"):
        seen = set()
        for l in p.split("\n"):
            for f in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):
                if l.count(f) > 0:
                    seen.add(f)
        if len(seen) == 7:
            cnt += 1
    return cnt


print(solve(input.rstrip("\n")))

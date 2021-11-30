import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    insts = input.split()
    seen = set()
    inst = 0
    acc = 0
    while inst not in seen:
        seen.add(inst)
        op, _, by = insts[inst].partition(" ")
        if op == "nop":
            inst += 1
        elif op == "acc":
            acc += int(by)
            inst += 1
        else:
            inst += int(by)
    return acc


print(solve(input.rstrip("\n")))

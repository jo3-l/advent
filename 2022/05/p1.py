import re


def find_ints(txt: str):
    return map(int, re.findall(r"\d+", txt))


def parse(drawing: list[str]):
    stack_count = max(find_ints(drawing[-1]))
    stacks = [[] for _ in range(stack_count)]
    for lvl in drawing[-2::-1]:
        for i, c in enumerate(lvl[1::4]):
            if c != " ":
                stacks[i].append(c)
    return stacks


def solve(data: str):
    drawing, insts = map(str.splitlines, data.split("\n\n"))
    stacks = parse(drawing)

    for inst in insts:
        cnt, src, dst = find_ints(inst)
        for _ in range(cnt):
            stacks[dst - 1].append(stacks[src - 1].pop())
    print("".join(stack[-1] for stack in stacks))

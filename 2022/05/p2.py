import re


def solve(data):
    drawing, insts = map(str.splitlines, data.split("\n\n"))
    max_stack = max(map(int, re.findall(r"\d+", drawing[-1])))
    stacks = [[] for _ in range(max_stack)]
    for level in drawing[-2::-1]:
        pos = 1
        stack = 0
        while pos < len(level):
            if level[pos] != " ":
                stacks[stack].append(level[pos])
            pos += len("] [") + 1
            stack += 1

    for inst in insts:
        cnt, src, dst = map(int, re.findall(r"\d+", inst))
        stacks[dst - 1].extend(stacks[src - 1][-cnt:])
        del stacks[src - 1][-cnt:]
    print("".join(stack[-1] for stack in stacks))

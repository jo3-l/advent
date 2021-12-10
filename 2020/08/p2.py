def run(insts):
    seen = set()
    inst = 0
    acc = 0
    while inst not in seen and 0 <= inst < len(insts):
        seen.add(inst)
        op, by = insts[inst]
        if op == "nop":
            inst += 1
        elif op == "acc":
            acc += by
            inst += 1
        else:
            inst += by
    return acc, inst >= len(insts)


def solve(input):
    insts = [
        [op, int(by)]
        for op, _, by in map(lambda l: l.partition(" "), input.split("\n"))
    ]
    for inst in insts:
        op = inst[0]
        if op not in ("nop", "jmp"):
            continue
        inst[0] = "jmp" if op == "nop" else "nop"
        acc, ok = run(insts)
        if ok:
            return acc
        inst[0] = op

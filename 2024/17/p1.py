import re

register_re = re.compile(r"Register [ABC]: (-?\d+)")

A, B, C = 0, 1, 2


def solve(data: str):
    reg_data, prog = data.split("\n\n")
    regs = [int(n) for n in register_re.findall(reg_data)]
    prog = list(map(int, prog.removeprefix("Program: ").split(",")))

    out = []
    ip = 0
    while 0 <= ip < len(prog):
        opcode = prog[ip]
        operand = prog[ip + 1]
        ip += 2

        def combo(o):
            match o:
                case 0 | 1 | 2 | 3:
                    return o
                case 4 | 5 | 6:
                    return regs[o - 4]
                case _:
                    assert False, f"unexpected combo operand {o}"

        match opcode:
            case 0:
                numer = regs[A]
                denom = 1 << combo(operand)
                regs[A] = numer // denom
            case 1:
                regs[B] ^= operand
            case 2:
                regs[B] = combo(operand) % 8
            case 3:
                if regs[A] != 0:
                    ip = operand
            case 4:
                regs[B] ^= regs[C]
            case 5:
                out.append(combo(operand) % 8)
            case 6:
                numer = regs[A]
                denom = 1 << combo(operand)
                regs[B] = numer // denom
            case 7:
                numer = regs[A]
                denom = 1 << combo(operand)
                regs[C] = numer // denom
    return ",".join(map(str, out))

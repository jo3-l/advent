import math
import re
from dataclasses import dataclass
from typing import Protocol, Tuple


class Op(Protocol):
    _incr_op_pat = re.compile(r"new = old \+ (\d+)")
    _mul_op_pat = re.compile(r"new = old \* (\d+)")

    def apply(old: int) -> int:
        ...

    @staticmethod
    def from_equation(eq: str):
        if m := Op._incr_op_pat.match(eq):
            return IncrOp(int(m.group(1)))
        elif m := Op._mul_op_pat.match(eq):
            return MulOp(int(m.group(1)))
        else:
            return SquareOp()


class IncrOp:
    def __init__(self, incr_by: int):
        self.incr_by = incr_by

    def apply(self, old: int):
        return old + self.incr_by


class MulOp:
    def __init__(self, multiplier: int):
        self.multiplier = multiplier

    def apply(self, old: int):
        return old * self.multiplier


class SquareOp:
    def apply(self, old: int):
        return old * old


@dataclass
class Monkey:
    items: list[int]
    op: Op
    div_by: int
    targets: Tuple[int, int]


digits_pat = re.compile(r"\d+")


def find_ints(txt: str):
    return map(int, digits_pat.findall(txt))


ROUNDS = 20


def solve(data: str):
    monkeys: list[Monkey] = []

    # 0  Monkey X:
    # 1    Starting items: ...
    # 2    Operation: ...
    # 3    Test: ...
    # 4       If true: ...
    # 5       If false: ...
    for lines in map(str.splitlines, data.split("\n\n")):
        starting_items = list(find_ints(lines[1]))

        op = Op.from_equation(lines[2].strip().removeprefix("Operation: "))

        div_by = next(find_ints(lines[3]))
        if_divisible = next(find_ints(lines[4]))
        if_indivisible = next(find_ints(lines[5]))

        monkeys.append(
            Monkey(starting_items, op, div_by, (if_divisible, if_indivisible))
        )

    num_inspected = [0] * len(monkeys)
    for _ in range(ROUNDS):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items:
                new_item = monkey.op.apply(item) // 3
                if new_item % monkey.div_by == 0:
                    monkeys[monkey.targets[0]].items.append(new_item)
                else:
                    monkeys[monkey.targets[1]].items.append(new_item)
            num_inspected[i] += len(monkey.items)
            monkey.items.clear()
    return math.prod(sorted(num_inspected)[-2:])

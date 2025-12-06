from functools import reduce
import operator
from itertools import pairwise


def solve1(s: str):
    lines = s.splitlines()
    ops = [operator.add if op == "+" else operator.mul for op in lines[-1].split()]
    columns = [[] for _ in range(len(ops))]
    for line in lines[:-1]:
        nums = list(map(int, line.split()))
        for column, num in zip(columns, nums, strict=True):
            column.append(num)
    return sum(reduce(op, column) for op, column in zip(ops, columns))


def solve2(s: str):
    lines = s.splitlines()
    rulers = []
    ops = []
    for i, c in enumerate(lines[-1]):
        if c == "+" or c == "*":
            ops.append(operator.add if c == "+" else operator.mul)
            rulers.append(i)
    rulers.append(len(lines[-1]) + 1)

    columns = [[] for _ in range(len(ops))]
    for line in lines[:-1]:
        for column, (rstart, rend) in zip(columns, pairwise(rulers), strict=True):
            column.append(line[rstart : rend - 1])

    def asnum(digits):
        n = 0
        for d in digits:
            n = n * 10 + d
        return n

    def interpret(column):
        width = len(column[0])
        out = []
        for i in range(width):
            digits = (int(row[i]) for row in column if row[i].isdigit())
            out.append(asnum(digits))
        return out

    return sum(reduce(op, interpret(column)) for op, column in zip(ops, columns))

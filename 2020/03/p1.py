import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    matrix = input.split("\n")
    m, n = len(matrix), len(matrix[0])
    i, j = 0, 0
    cnt = 0
    while i < m:
        if matrix[i][j % n] == "#":
            cnt += 1
        i += 1
        j += 3
    return cnt


print(solve(input.rstrip("\n")))

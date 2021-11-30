import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    matrix = input.split("\n")
    m, n = len(matrix), len(matrix[0])
    p = 1
    for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        i, j = 0, 0
        cnt = 0
        while i < m:
            if matrix[i][j % n] == "#":
                cnt += 1
            i += dy
            j += dx
        p *= cnt
    return p


print(solve(input.rstrip("\n")))

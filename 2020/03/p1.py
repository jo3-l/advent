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

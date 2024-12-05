adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def solve(data: str):
    matrix = data.splitlines()
    R, C = len(matrix), len(matrix[0])

    def match_word(w, i, j, d_i, d_j):
        for c in w:
            if 0 <= i < R and 0 <= j < C and matrix[i][j] == c:
                i += d_i
                j += d_j
            else:
                return False
        return True

    ans = 0
    for i in range(R):
        for j in range(C):
            for d_i, d_j in adj8:
                ans += match_word("XMAS", i, j, d_i, d_j)
    return ans

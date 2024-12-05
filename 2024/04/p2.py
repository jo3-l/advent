def down(i=0):
    return i + 1


def up(i=0):
    return i - 1


def left(j=0):
    return j - 1


def right(j=0):
    return j + 1


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
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if matrix[i][j] == "A":
                # fmt: off
                main_ok = (match_word("MAS", down(i), left(j), up(), right())
                    or match_word("SAM", down(i), left(j), up(), right()))

                # fmt: off
                secondary_ok = (match_word("MAS", up(i), left(j), down(), right())
                        or match_word("SAM", up(i), left(j), down(), right()))

                ans += main_ok and secondary_ok
    return ans

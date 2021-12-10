adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def make_indexer(lst, default=None):
    def get(*indices):
        cur = lst
        for i in indices:
            if 0 <= i < len(cur):
                cur = cur[i]
            else:
                return default
        return cur

    return get


def solve(input):
    matrix = lmap(ints, input.split())
    get = make_indexer(matrix, 9)
    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if all(matrix[i][j] < get(i + dy, j + dx) for dx, dy in adj4):
                k += matrix[i][j] + 1
    return k

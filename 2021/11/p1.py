adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


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
    matrix = [ints(l) for l in input.split()]
    r, c = len(matrix), len(matrix[0])

    def run_step():
        nonlocal matrix
        for i in range(r):
            for j in range(c):
                matrix[i][j] += 1

        get = make_indexer(matrix, 0)

        def flash(i, j):
            flashes = 1
            for dx, dy in adj8:
                n_i, n_j = i + dy, j + dx
                if get(n_i, n_j):
                    matrix[n_i][n_j] += 1
                    if matrix[n_i][n_j] > 9:
                        matrix[n_i][n_j] = 0
                        flashes += flash(n_i, n_j)
            return flashes

        total_flashes = 0
        while True:
            flashes = 0
            for i in range(r):
                for j in range(c):
                    if matrix[i][j] > 9:
                        matrix[i][j] = 0
                        flashes += flash(i, j)
            total_flashes += flashes
            if not flashes:
                return total_flashes

    return sum(run_step() for _ in range(100))

import itertools

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
    grid = [ints(l) for l in input.split()]

    def run_step():
        nonlocal grid
        grid = [[x + 1 for x in r] for r in grid]

        get = make_indexer(grid)

        def flash(i, j):
            flashes = 1
            for dx, dy in adj8:
                n_i, n_j = i + dy, j + dx
                if get(n_i, n_j):
                    grid[n_i][n_j] += 1
                    if grid[n_i][n_j] > 9:
                        grid[n_i][n_j] = 0
                        flashes += flash(n_i, n_j)
            return flashes

        while True:
            flashes = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] > 9:
                        grid[i][j] = 0
                        flashes += flash(i, j)
            if not flashes:
                return

    step = 0
    while sum(itertools.chain(*grid)):
        run_step()
        step += 1
    return step

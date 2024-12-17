dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def solve(data: str):
    warehouse, moves = data.split("\n\n")

    warehouse = [list(row) for row in warehouse.splitlines()]
    moves = "".join(moves.splitlines())

    i, j = next(
        (i, j) for i, row in enumerate(warehouse) for j, c in enumerate(row) if c == "@"
    )

    def move_to(ti, tj):
        nonlocal i, j
        assert warehouse[ti][tj] == ".", "new location not free"
        warehouse[i][j], warehouse[ti][tj] = warehouse[ti][tj], warehouse[i][j]
        i, j = ti, tj

    for m in moves:
        dy, dx = dirs[m]
        ni, nj = i + dy, j + dx
        match warehouse[ni][nj]:
            case "#":
                pass  # noop
            case ".":
                move_to(ni, nj)
            case "O":
                # shift to make space
                freei, freej = ni, nj
                while warehouse[freei][freej] == "O":
                    freei += dy
                    freej += dx
                if warehouse[freei][freej] == ".":
                    warehouse[ni][nj], warehouse[freei][freej] = (
                        warehouse[freei][freej],
                        warehouse[ni][nj],
                    )
                    move_to(ni, nj)

    def score(i, j):
        return 100 * i + j

    return sum(
        score(i, j)
        for i, row in enumerate(warehouse)
        for j, c in enumerate(row)
        if c == "O"
    )

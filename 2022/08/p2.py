from collections.abc import Iterator
from typing import Tuple


def zeroed_matrix(rows: int, cols: int):
    return [[0] * cols for _ in range(rows)]


def solve(data: str):
    grid = [list(map(int, line)) for line in data.splitlines()]
    rows, cols = len(grid), len(grid[0])

    def scan(viewing_distance: list[list[int]], trees: Iterator[Tuple[int, int]]):
        init_r, init_c = next(trees)
        monostack = [(init_r, init_c)]  # invariant: trees are decreasing in height
        viewing_distance[init_r][init_c] = 0
        for r, c in trees:
            # find closest tree blocking view, if any
            while monostack:
                cand_r, cand_c = monostack[-1]
                if grid[cand_r][cand_c] >= grid[r][c]:
                    break
                monostack.pop()

            if monostack:
                # farthest tree we can see
                blocking_r, blocking_c = monostack[-1]
                viewing_distance[r][c] = abs(r - blocking_r) + abs(c - blocking_c)
            else:
                # nothing blocking our view
                viewing_distance[r][c] = abs(r - init_r) + abs(c - init_c)
            monostack.append((r, c))

    view_rightward = zeroed_matrix(rows, cols)
    for r in range(rows):
        scan(view_rightward, ((r, c) for c in range(cols)))

    view_leftward = zeroed_matrix(rows, cols)
    for r in range(rows - 1, -1, -1):
        scan(view_leftward, ((r, c) for c in range(cols - 1, -1, -1)))

    view_downward = zeroed_matrix(rows, cols)
    for c in range(cols):
        scan(view_downward, ((r, c) for r in range(rows)))

    view_upward = zeroed_matrix(rows, cols)
    for c in range(cols - 1, -1, -1):
        scan(view_upward, ((r, c) for r in range(rows - 1, -1, -1)))

    max_score = 0
    for r in range(rows):
        for c in range(cols):
            score = (
                view_rightward[r][c]
                * view_leftward[r][c]
                * view_downward[r][c]
                * view_upward[r][c]
            )
            max_score = max(
                max_score,
                score,
            )
    return max_score

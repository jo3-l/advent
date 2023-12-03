import re
from dataclasses import dataclass
from typing import Tuple, Iterator


@dataclass(frozen=True)
class PartNumber:
    val: int

    row: int
    start_col: int
    end_col: int  # exclusive


def iter_part_numbers(matrix: list[str]) -> Iterator[PartNumber]:
    for i, line in enumerate(matrix):
        for m in re.finditer(r"\d+", line):
            yield PartNumber(
                val=int(m.group(0)), row=i, start_col=m.start(), end_col=m.end()
            )


adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def iter_adjacent(r: int, c: int, bounds: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    for d_r, d_c in adj8:
        n_r = r + d_r
        n_c = c + d_c
        if 0 <= n_r < bounds[0] and 0 <= n_c < bounds[1]:
            yield (n_r, n_c)


def is_sym(c: str):
    return not c.isdigit() and c != "."


def solve(data: str):
    lines = data.splitlines()
    bounds = (len(lines), len(lines[0]))

    ans = 0
    for part in iter_part_numbers(lines):
        has_adjacent_sym = False

        for c in range(part.start_col, part.end_col):
            if any(
                is_sym(lines[adj_r][adj_c])
                for adj_r, adj_c in iter_adjacent(part.row, c, bounds)
            ):
                has_adjacent_sym = True
                break

        if has_adjacent_sym:
            ans += part.val

    return ans

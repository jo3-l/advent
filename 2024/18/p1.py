from typing import Optional
from collections import deque

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve(data: str, *, exit: tuple[int, int], lim: Optional[int] = None):
    lines = data.splitlines()
    if lim is not None:
        lines = lines[: min(len(lines), lim)]

    corrupted = set()
    for line in lines:
        x, y = map(int, line.split(","))
        corrupted.add((x, y))

    start = (0, 0)
    q: deque[tuple[int, int]] = deque([start])
    visited: set[tuple[int, int]] = set([start])
    steps = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dy, dx in dirs:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx <= exit[0]
                    and 0 <= ny <= exit[1]
                    and (nx, ny) not in corrupted
                    and (nx, ny) not in visited
                ):
                    if (nx, ny) == exit:
                        return steps + 1
                    visited.add((nx, ny))
                    q.append((nx, ny))
        steps += 1

    assert False, "no path found"

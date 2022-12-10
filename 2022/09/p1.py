from dataclasses import dataclass


@dataclass(frozen=True, unsafe_hash=True)
class Point:
    x: int
    y: int

    def iter_adjacent(self):
        return (
            Point(self.x + dx, self.y + dy)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))
        )

    def iter_diagonals(self):
        return (
            Point(self.x + dx, self.y + dy)
            for dx, dy in ((1, -1), (-1, 1), (1, 1), (-1, -1))
        )

    def is_touching(self, p: "Point"):
        dx, dy = abs(self.x - p.x), abs(self.y - p.y)
        return dx + dy <= 1 or dx == dy == 1

    def __str__(self):
        return f"({self.x}, {self.y})"


def solve(data: str):
    head = tail = Point(0, 0)
    visited = {tail}
    dirs = {"L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0)}
    for move in data.splitlines():
        dir, n = move.split()
        dx, dy = dirs[dir]
        for _ in range(int(n)):
            head = Point(head.x + dx, head.y + dy)
            if not tail.is_touching(head):
                if head.x == tail.x or head.y == tail.y:
                    possible_new_tails = tail.iter_adjacent()
                else:
                    possible_new_tails = tail.iter_diagonals()

                tail = next(
                    new_tail
                    for new_tail in possible_new_tails
                    if new_tail.is_touching(head)
                )
                visited.add(tail)
    return len(visited)

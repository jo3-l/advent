from dataclasses import dataclass
from heapq import heappop, heappush
from functools import total_ordering
from typing import Optional
from collections import defaultdict, deque

# in clockwise order, starting with east
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

INF = 10**18


@total_ordering
@dataclass
class Item:
    i: int
    j: int
    dir: int
    cost: int

    def state(self) -> "State":
        return State(self.i, self.j, self.dir)

    def __lt__(self, other: "Item"):
        return (self.cost, self.dir, self.i, self.j) < (
            other.cost,
            other.dir,
            other.i,
            other.j,
        )


@dataclass(frozen=True)
class State:
    i: int
    j: int
    dir: int


@dataclass
class OptimalPathInfo:
    cost: int
    parents: set[State]


class WorkState:
    def __init__(self, maze: list[list[str]]):
        self.q = []
        self.best = defaultdict(lambda: OptimalPathInfo(INF, set()))
        self.maze = maze

    def add(self, item: Item, parent: Optional[State] = None):
        state = item.state()
        opt = self.best[state]
        if item.cost == opt.cost:
            if parent:
                if parent not in opt.parents:
                    opt.parents.add(parent)
                    self._push(item)
        elif item.cost < opt.cost:
            opt.cost = item.cost
            opt.parents.clear()
            if parent:
                opt.parents.add(parent)
            self._push(item)

    def _push(self, item: Item):
        if self.maze[item.i][item.j] != "E":
            heappush(self.q, item)

    def done(self) -> bool:
        return not self.q

    def pop(self) -> Item:
        return heappop(self.q)

    def min_cost_to(self, i: int, j: int) -> Optional[tuple[int, list[State]]]:
        min_cost = INF
        min_states = []
        for d in range(4):
            state = State(i, j, d)
            cost = self.best[state].cost
            if cost != INF:
                if cost == min_cost:
                    min_states.append(state)
                elif cost < min_cost:
                    min_cost = cost
                    min_states = [state]

        if min_cost == INF:
            return None
        else:
            return min_cost, min_states

    def backtrack(self, end_states: list[State]) -> set[State]:
        seen = set(end_states)
        q = deque(end_states)
        while q:
            state = q.popleft()
            for parent in self.best[state].parents:
                if parent not in seen:
                    seen.add(parent)
                    q.append(parent)
        return seen


def solve(data: str):
    maze = list(map(list, data.splitlines()))

    work = WorkState(maze)
    end_i, end_j = -1, -1
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == "S":
                work.add(Item(i, j, dir=0, cost=0))
            elif c == "E":
                end_i, end_j = i, j

    while not work.done():
        item = work.pop()
        state = item.state()
        if item.cost > work.best[state].cost:
            continue

        for ndir in ((item.dir - 1) % 4, (item.dir + 1) % 4):
            work.add(
                Item(item.i, item.j, dir=ndir, cost=item.cost + 1000),
                parent=state,
            )

        dy, dx = dirs[item.dir]
        ni, nj = item.i + dy, item.j + dx
        if maze[ni][nj] != "#":
            work.add(Item(ni, nj, dir=item.dir, cost=item.cost + 1), parent=state)

    best = work.min_cost_to(end_i, end_j)
    assert best, "no path found"

    min_cost, end_states = best
    print(f"min cost: {min_cost}")
    good_tiles = set((state.i, state.j) for state in work.backtrack(end_states))
    print(f"good tiles: {len(good_tiles)}")

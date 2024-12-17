from dataclasses import dataclass
from heapq import heappop
from functools import total_ordering
from typing import Optional
import math

# in clockwise order, starting with east
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

StateKey = tuple[int, int, int]


@total_ordering
@dataclass
class Work:
    i: int
    j: int
    dir: int
    cost: int

    def state(self) -> "State":
        return State(self.i, self.j, self.dir)

    def __lt__(self, other: "Work"):
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
class OptPathInfo:
    cost: int
    predecessors: set[State]


def solve(data: str):
    maze = list(map(list, data.splitlines()))

    best: dict[State, OptPathInfo] = {}
    q: list[Work] = []

    def push(w: "Work"):
        if maze[w.i][w.j] != "E":
            q.append(w)

    def process(w: "Work", prev: Optional[State] = None):
        k = w.state()
        try:
            opt = best[k]
            if w.cost == opt.cost:
                if prev:
                    if prev not in opt.predecessors:
                        opt.predecessors.add(prev)
                        push(w)
                else:
                    push(w)
            elif w.cost < opt.cost:
                best[k] = OptPathInfo(w.cost, predecessors=set([prev] if prev else []))
                push(w)
        except KeyError:
            best[k] = OptPathInfo(w.cost, predecessors=set([prev] if prev else []))
            push(w)

    end_i, end_j = -1, -1
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == "S":
                process(Work(i, j, dir=0, cost=0))
            elif c == "E":
                end_i, end_j = i, j

    while q:
        w = heappop(q)
        if w.cost > best[w.state()].cost:
            continue

        for ndir in ((w.dir - 1) % 4, (w.dir + 1) % 4):
            process(Work(w.i, w.j, dir=ndir, cost=w.cost + 1000), prev=w.state())

        dy, dx = dirs[w.dir]
        ni, nj = w.i + dy, w.j + dx
        if maze[ni][nj] != "#":
            process(Work(ni, nj, dir=w.dir, cost=w.cost + 1), prev=w.state())

    min_cost = math.inf
    min_cost_states = []
    for dir in range(4):
        k = State(end_i, end_j, dir)
        try:
            opt = best[k]
            if opt.cost == min_cost:
                min_cost_states.append(k)
            elif opt.cost < min_cost:
                min_cost = opt.cost
                min_cost_states = [k]
        except KeyError:
            pass

    print(f"min cost: {min_cost}")
    good_tiles: set[tuple[int, int]] = set([(end_i, end_j)])

    visited_states = set()

    def visit(k: State):
        if k in visited_states:
            return
        visited_states.add(k)
        opt = best[k]
        for p in opt.predecessors:
            good_tiles.add((p.i, p.j))
            visit(p)

    for k in min_cost_states:
        visit(k)

    print(f"good tiles: {len(good_tiles)}")

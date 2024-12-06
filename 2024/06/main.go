package main

import (
	"bufio"
	"fmt"
	"os"
	"sync"
	"sync/atomic"
)

const part2Workers = 16

func main() {
	in, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	var grid []string
	sc := bufio.NewScanner(in)
	for sc.Scan() {
		grid = append(grid, sc.Text())
	}

	part1(grid)
	part2(grid, part2Workers)
}

type dir struct{ dy, dx int }

const numDirs = 4

var dirs = [numDirs]dir{{-1, 0}, {0, 1}, {1, 0}, {0, -1}} // in clockwise order, starting up

func part1(grid []string) {
	start, found := locateStart(grid)
	if !found {
		panic("no start position found")
	}

	g := newGuardState(grid, npos)
	g.Go(start.i, start.j, 0 /* up */)
	fmt.Println("part 1:", g.CalcNumVisited())
}

func part2(grid []string, workers int) {
	start, found := locateStart(grid)
	if !found {
		panic("no start position found")
	}

	work := make([][]pos, workers)
	w := 0
	for i, row := range grid {
		for j := range len(row) {
			if row[j] == '.' {
				work[w] = append(work[w], pos{i, j})
				w = (w + 1) % workers
			}
		}
	}

	var ans atomic.Int32
	var wg sync.WaitGroup
	for w := range workers {
		wg.Add(1)
		go func() {
			defer wg.Done()
			g := newGuardState(grid, npos)
			for _, o := range work[w] {
				g = reuseGuardState(g, o)
				cycle := g.Go(start.i, start.j, 0 /* up */)
				if cycle {
					ans.Add(1)
				}
			}
		}()
	}

	wg.Wait()
	fmt.Println("part 2:", ans.Load())
}

func locateStart(grid []string) (pos, bool) {
	for i, row := range grid {
		for j := range len(row) {
			if row[j] == '^' {
				return pos{i, j}, true
			}
		}
	}
	return npos, false
}

type pos struct{ i, j int }

var npos = pos{-1, -1}

type guardState struct {
	grid        []string
	visited     []uint8 // flattened grid, each element is bitset
	newObstacle pos
	R, C        int
}

func newGuardState(grid []string, newObstacle pos) *guardState {
	R, C := len(grid), len(grid[0])
	visited := make([]uint8, R*C)
	return &guardState{grid, visited, newObstacle, R, C}
}

func reuseGuardState(old *guardState, newObstacle pos) *guardState {
	vis := old.visited
	clear(vis)
	return &guardState{old.grid, vis, newObstacle, old.R, old.C}
}

func (g *guardState) Go(i, j, d int) (cycle bool) {
	if already := g.markVisited(i, j, d); already {
		return true
	}

	dir := dirs[d]
	ni, nj := i+dir.dy, j+dir.dx
	if !g.inBounds(ni, nj) {
		return false
	}

	if g.get(ni, nj) == '#' {
		// try turning
		return g.Go(i, j, (d+1)%numDirs)
	}
	return g.Go(ni, nj, d)
}

func (g *guardState) CalcNumVisited() int {
	n := 0
	for _, v := range g.visited {
		if v > 0 {
			n++
		}
	}
	return n
}

func (g *guardState) inBounds(i, j int) bool {
	return 0 <= i && i < g.R && 0 <= j && j < g.C
}

func (g *guardState) get(i, j int) byte {
	if o := g.newObstacle; i == o.i && j == o.j {
		return '#'
	}
	return g.grid[i][j]
}

func (g *guardState) markVisited(i, j, d int) (already bool) {
	vidx := g.vidx(i, j)
	already = (g.visited[vidx] & (1 << d)) != 0
	g.visited[vidx] |= (1 << d)
	return
}
func (g *guardState) vidx(i, j int) int {
	return i*g.C + j
}

package main

import (
	"bufio"
	"fmt"
	"iter"
	"os"
	"strings"
)

func main() {
	in, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	sc := bufio.NewScanner(in)
	var grid []string
	for sc.Scan() {
		grid = append(grid, sc.Text())
	}

	rs := regions(grid)
	part1(rs)
	part2(rs)
}

func part1(regions []Region) {
	var price int
	for _, r := range regions {
		price += len(r.Plants) * len(r.Perimeter)
	}
	fmt.Println("part 1:", price)
}

func part2(regions []Region) {
	var price int
	for _, r := range regions {
		price += len(r.Plants) * countSides(r)
	}
	fmt.Println("part 2:", price)
}

func regions(grid []string) []Region {
	padded, R, C := pad(grid)
	g := gardenRegions{padded, make([]bool, R*C), R, C}

	var regions []Region
	for p := range g.allPlants() {
		if !g.hasVisited(p) {
			regions = append(regions, g.traceRegion(p))
		}
	}
	return regions
}

func pad(grid []string) (padded []string, R, C int) {
	origR := len(grid)
	origC := len(grid[0])

	padded = make([]string, 0, R)

	// generate horizontal border
	var horiz strings.Builder
	horiz.WriteByte('+')
	for range origC {
		horiz.WriteByte('-')
		horiz.WriteByte('+')
	}

	padded = append(padded, horiz.String())
	for _, row := range grid {
		var r strings.Builder
		r.WriteByte('|')
		for i := range len(row) {
			r.WriteByte(row[i])
			r.WriteByte('|')
		}
		padded = append(padded, r.String())
		padded = append(padded, horiz.String())
	}

	return padded, 2*origR + 1, 2*origC + 1
}

// + - + - +
// |   |   |
//    ...

func isHorizontalEdge(p pos) bool { return p.i%2 == 0 }
func isVerticalEdge(p pos) bool   { return p.j%2 == 0 }

type gardenRegions struct {
	grid    []string // padded with edge characters
	visited []bool   // flattened R*C grid
	R, C    int      // including added edges
}

type Region struct {
	Plants    []pos
	Perimeter []pos
}

type pos struct{ i, j int }

var npos = pos{-1, -1}

func (g *gardenRegions) traceRegion(start pos) Region {
	var plants, perim []pos
	plants = append(plants, start)

	q := []pos{start}
	g.markVisited(start)
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]

		for edge, neigh := range g.neighbors(cur) {
			if neigh == npos || g.get(neigh) != g.get(cur) {
				perim = append(perim, edge)
			} else if already := g.markVisited(neigh); !already {
				plants = append(plants, neigh)
				q = append(q, neigh)
			}
		}
	}
	return Region{plants, perim}
}

func (g *gardenRegions) markVisited(p pos) (already bool) {
	idx := p.i*g.C + p.j
	already = g.visited[idx]
	g.visited[idx] = true
	return already
}

func (g *gardenRegions) hasVisited(p pos) bool {
	return g.visited[p.i*g.C+p.j]
}

func (g *gardenRegions) get(p pos) byte {
	return g.grid[p.i][p.j]
}

func (g *gardenRegions) allPlants() iter.Seq[pos] {
	return func(yield func(pos) bool) {
		for i := 1; i < g.R-1; i += 2 {
			for j := 1; j < g.C-1; j += 2 {
				if !yield(pos{i, j}) {
					return
				}
			}
		}
	}
}

type dir struct{ dy, dx int }

var dirs = [...]dir{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

// neighbors returns an iterator of pairs of `(neighboring edge, neighboring plant)` to the top,
// bottom, left, and right of `plant`. In cases where there is no neighboring plant in a particular
// direction, for instance if `plant` is at a corner of the garden, the pair `(edgepos, npos)` is
// yielded.
func (g *gardenRegions) neighbors(plant pos) iter.Seq2[pos, pos] {
	return func(yield func(pos, pos) bool) {
		for _, d := range dirs {
			dy, dx := d.dy, d.dx

			edge := pos{plant.i + dy, plant.j + dx}
			neigh := pos{plant.i + 2*dy, plant.j + 2*dx}
			if !g.inBounds(neigh) {
				neigh = npos
			}

			if !yield(edge, neigh) {
				return
			}
		}
	}
}

func (g *gardenRegions) inBounds(p pos) bool {
	return 0 <= p.i && p.i < g.R && 0 <= p.j && p.j < g.C
}

func countSides(r Region) int {
	edges := make(map[pos]bool)
	for _, e := range r.Perimeter {
		edges[e] = true
	}

	vertTraced, horizTraced := make(map[pos]bool), make(map[pos]bool)
	lt := &lineTracer{edges, vertTraced, horizTraced}

	var sides int
	for _, e := range r.Perimeter {
		if isVerticalEdge(e) && !lt.vertTraced[e] {
			lt.traceVertical(e)
			sides++
		}
		if isHorizontalEdge(e) && !lt.horizTraced[e] {
			lt.traceHorizontal(e)
			sides++
		}
	}
	return sides
}

type lineTracer struct {
	edges                   map[pos]bool
	vertTraced, horizTraced map[pos]bool
}

func (lt *lineTracer) traceVertical(p pos) {
	if lt.vertTraced[p] {
		return
	}
	lt.vertTraced[p] = true
	if lt.hasEdge(p.i-2, p.j) && !lt.cutsHorizontal(p.i-1, p.j) {
		lt.traceVertical(pos{p.i - 2, p.j})
	}
	if lt.hasEdge(p.i+2, p.j) && !lt.cutsHorizontal(p.i+1, p.j) {
		lt.traceVertical(pos{p.i + 2, p.j})
	}
}

func (lt *lineTracer) cutsHorizontal(i, j int) bool {
	//   -- + --
	//	    ^ (i, j)
	return lt.hasEdge(i, j-1) && lt.hasEdge(i, j+1)
}

func (lt *lineTracer) traceHorizontal(p pos) {
	if lt.horizTraced[p] {
		return
	}
	lt.horizTraced[p] = true
	if lt.hasEdge(p.i, p.j-2) && !lt.cutsVertical(p.i, p.j-1) {
		lt.traceHorizontal(pos{p.i, p.j - 2})
	}
	if lt.hasEdge(p.i, p.j+2) && !lt.cutsVertical(p.i, p.j+1) {
		lt.traceHorizontal(pos{p.i, p.j + 2})
	}
}

func (lt *lineTracer) cutsVertical(i, j int) bool {
	//     |
	//     + <- (i, j)
	//     |
	return lt.hasEdge(i-1, j) && lt.hasEdge(i+1, j)
}

func (lt *lineTracer) hasEdge(i, j int) bool {
	return lt.edges[pos{i, j}]
}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type scanMode int

const (
	scanGrid scanMode = iota
	scanMoves
)

func main() {
	in, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer in.Close()

	sc := bufio.NewScanner(in)
	mode := scanGrid

	var (
		warehouse [][]byte
		moves     []byte
	)
	for sc.Scan() {
		if sc.Text() == "" {
			mode = scanMoves
			continue
		}

		switch mode {
		case scanGrid:
			warehouse = append(warehouse, resize(sc.Text()))
		case scanMoves:
			moves = append(moves, sc.Text()...)
		}
	}

	rpos, ok := locateRobot(warehouse)
	if !ok {
		panic("robot not found")
	}

	r := newRobot(warehouse, rpos)
	for _, dir := range moves {
		r.Move(dir)
	}

	final := r.State()
	var ans int
	for i, row := range final {
		for j, c := range row {
			if c == '[' {
				ans += i*100 + j
			}
		}
	}
	fmt.Println("part 2:", ans)
}

var resized = [256]string{'#': "##", 'O': "[]", '.': "..", '@': "@."}

func resize(line string) []byte {
	out := make([]byte, 0, len(line)*2)
	for i := range len(line) {
		out = append(out, resized[line[i]]...)
	}
	return out
}

type pos struct{ i, j int }

var npos = pos{-1, -1}

func locateRobot(warehouse [][]byte) (robot pos, ok bool) {
	for i, row := range warehouse {
		for j, c := range row {
			if c == '@' {
				return pos{i, j}, true
			}
		}
	}
	return npos, false
}

type robot struct {
	warehouse [][]byte
	cur       pos
}

func newRobot(warehouse [][]byte, cur pos) *robot {
	return &robot{warehouse, cur}
}

type dir struct{ dy, dx int }

func (d dir) Vertical() bool   { return d.dy != 0 }
func (d dir) Horizontal() bool { return d.dx != 0 }

func mustDir(d byte) dir {
	switch d {
	case '^':
		return dir{-1, 0}
	case 'v':
		return dir{1, 0}
	case '<':
		return dir{0, -1}
	case '>':
		return dir{0, 1}
	default:
		panic("unknown dir " + string(d))
	}
}

func (r *robot) Move(d byte) {
	r.pushAll([]pos{r.cur}, mustDir(d))
}

// pushAll tries to move all items one step toward the indicated direction.
func (r *robot) pushAll(items []pos, dir dir) (ok bool) {
	if len(items) == 0 {
		return true
	}

	frontier := make(map[pos]bool)
	for _, v := range items {
		ni, nj := v.i+dir.dy, v.j+dir.dx
		switch c := r.warehouse[ni][nj]; c {
		case '#':
			return false
		case '.':
			// ok
		case '[', ']':
			if dir.Vertical() {
				// boxes move together
				frontier[pos{ni, nj}] = true
				if c == '[' {
					frontier[pos{ni, nj + 1}] = true
				} else {
					frontier[pos{ni, nj - 1}] = true
				}
			} else {
				frontier[pos{ni, nj}] = true
			}
		}
	}

	next := make([]pos, 0, len(frontier))
	for v := range frontier {
		next = append(next, v)
	}
	if !r.pushAll(next, dir) {
		return false
	}

	for _, v := range items {
		ni, nj := v.i+dir.dy, v.j+dir.dx
		r.relocate(v, pos{ni, nj})
	}
	return true
}

func (r *robot) relocate(src pos, dst pos) {
	if r.warehouse[dst.i][dst.j] != '.' {
		panic("relocate: new location not empty")
	}

	if src == r.cur {
		r.cur = dst
	}
	r.warehouse[src.i][src.j], r.warehouse[dst.i][dst.j] = r.warehouse[dst.i][dst.j], r.warehouse[src.i][src.j]
}

func (r *robot) String() string {
	var sb strings.Builder
	for i, row := range r.warehouse {
		if i > 0 {
			sb.WriteByte('\n')
		}
		sb.Write(row)
	}
	return sb.String()
}

func (r *robot) State() [][]byte {
	return r.warehouse
}

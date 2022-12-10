IMG_WIDTH = 40


def solve(data: str):
    cycle = 0
    reg = 1

    img = [["."] * IMG_WIDTH for _ in range(6)]

    def tick():
        nonlocal cycle
        cycle += 1

    def draw():
        if (cycle % IMG_WIDTH) in (reg - 1, reg, reg + 1):
            img[cycle // IMG_WIDTH][cycle % IMG_WIDTH] = "#"

    draw()
    for inst in data.splitlines():
        op, *args = inst.split()
        if op == "addx":
            tick()
            draw()
            tick()
            reg += int(args[0])
            draw()
        else:
            tick()
            draw()

    for row in img:
        print("".join(row))


with open("input.txt") as f:
    solve(f.read())

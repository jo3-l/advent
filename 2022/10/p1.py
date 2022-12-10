def solve(data: str):
    ans = 0
    cycle = 0
    reg = 1

    def tick():
        nonlocal cycle, ans
        cycle += 1
        if cycle % 40 == 20:
            ans += cycle * reg

    for inst in data.splitlines():
        op, *args = inst.split()
        if op == "addx":
            tick()
            tick()
            reg += int(args[0])
        else:
            tick()
    return ans

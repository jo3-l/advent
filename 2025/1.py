def solve(s: str):
    dial = 50
    ans = 0
    for inst in s.splitlines():
        lr, n = inst[0], int(inst[1:])
        if lr == "L":
            dial = (dial - n) % 100
        else:
            dial = (dial + n) % 100
        ans += dial == 0
    return ans


def solve2(s: str):
    dial = 50
    ans = 0
    for inst in s.splitlines():
        lr, n = inst[0], int(inst[1:])
        if lr == "L":
            if dial == 0:
                ans += n // 100
            else:
                to_next_0 = dial
                if n >= to_next_0:
                    ans += 1 + (n - to_next_0) // 100
            dial = (dial - n) % 100

        elif lr == "R":
            if dial == 0:
                ans += n // 100
            else:
                to_next_0 = 100 - dial
                if n >= to_next_0:
                    ans += 1 + (n - to_next_0) // 100
            dial = (dial + n) % 100

    return ans

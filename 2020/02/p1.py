def solve(input):
    cnt = 0
    for s in input.split("\n"):
        parts = s.split()
        lo, _, hi = parts[0].partition("-")
        c = parts[1][0]
        pw = parts[2]
        if int(lo) <= pw.count(c) <= int(hi):
            cnt += 1
    return cnt

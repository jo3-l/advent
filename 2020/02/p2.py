def solve(input):
    cnt = 0
    for s in input.split("\n"):
        parts = s.split()
        lo, _, hi = parts[0].partition("-")
        lo, hi = int(lo) - 1, int(hi) - 1
        c = parts[1][0]
        pw = parts[2]
        if int(pw[lo] == c) ^ int(pw[hi] == c):
            cnt += 1
    return cnt

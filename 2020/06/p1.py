def solve(input):
    ans = 0
    for g in input.split("\n\n"):
        b = 0
        for c in g:
            if c.isalpha():
                b |= 1 << (ord(c) - ord("a"))
        ans += bin(b).count("1")
    return ans

def calc(cs, lo, hi, lc):
    for c in cs:
        mid = (lo + hi + 1) // 2
        if c == lc:
            hi = mid
        else:
            lo = mid
    return lo


def solve(input):
    m_id = 0
    for p in input.split():
        r, c = calc(p[:7], 0, 127, "F"), calc(p[7:], 0, 7, "L")
        m_id = max(m_id, r * 8 + c)
    return m_id

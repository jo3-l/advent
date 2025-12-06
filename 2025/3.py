def solve1(s: str):
    def joltage(line: str):
        best = 0
        best_tens = int(line[0])
        for n in map(int, line[1:]):
            best = max(best, 10 * best_tens + n)
            best_tens = max(best_tens, n)
        return best

    return sum(map(joltage, s.splitlines()))


def solve2(s: str):
    def joltage(line: str, ndigits=12):
        best_digits = [0] * ndigits  # least significant first
        remaining = len(line)
        for n in map(int, line):
            for j in range(min(remaining, ndigits) - 1, -1, -1):
                if n > best_digits[j]:
                    best_digits[j] = n
                    best_digits[:j] = [0] * j
                    break
            remaining -= 1

        best = 0
        for d in reversed(best_digits):
            best = (best * 10) + d
        return best

    return sum(joltage(line) for line in s.splitlines())

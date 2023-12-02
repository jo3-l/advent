from typing import Optional


def solve(data: str):
    total = 0
    for line in data.splitlines():
        digits: list[int] = []
        for i in range(len(line)):
            # On the first day of Christmas, my true love / sent to me / An O(n^2) algorithm
            d = extract_digit(line[i:])
            if d is not None:
                digits.append(d)

        total += digits[0] * 10 + digits[-1]
    return total


WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def extract_digit(s: str) -> Optional[int]:
    if s[0].isdigit():
        return int(s[0])

    for n, word in enumerate(WORDS):
        if s.startswith(word):
            return n + 1  # convert to one-indexed

    return None

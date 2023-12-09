import re


def extract_ints(s: str):
    return map(int, re.findall(r"\d+", s))


ACCELERATION = 1


def solve(data: str):
    times, distances = data.splitlines()

    ans = 1
    for dur, record in zip(extract_ints(times), extract_ints(distances)):
        ways = 0
        for t in range(1, dur):
            v = t * ACCELERATION
            dist = v * (dur - t)
            if dist > record:
                ways += 1
        ans *= ways
    return ans

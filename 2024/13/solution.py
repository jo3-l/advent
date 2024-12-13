import re


def solve(data: str, offset: int):
    min_tokens = 0
    for group in data.split("\n\n"):
        a, b, prize = group.splitlines()

        a_x, a_y = ints(a)
        b_x, b_y = ints(b)

        t_x, t_y = ints(prize)
        t_x += offset
        t_y += offset

        # solve the system
        #   a*a_x + b*b_x = t_x
        #   a*a_y + b*b_y = t_y
        b = (a_x * t_y - a_y * t_x) // (a_x * b_y - a_y * b_x)
        a = (t_x - b_x * b) // a_x
        if a >= 0 and b >= 0 and a * a_x + b * b_x == t_x and a * a_y + b * b_y == t_y:
            min_tokens += 3 * a + b

    return min_tokens


def ints(s: str):
    return map(int, re.findall(r"-?\d+", s))

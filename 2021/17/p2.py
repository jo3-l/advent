from collections import namedtuple
import re
import math


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def sum_arith_series(t1, tn, n):
    return ((t1 + tn) * n) // 2


def solve(input):
    min_x, max_x = ints(re.search(r"x=(-?\d+)\.\.(-?\d+)", input).groups())
    min_y, max_y = ints(re.search(r"y=(-?\d+)\.\.(-?\d+)", input).groups())

    def check(dx, dy):
        def f(n):
            x = 0
            if dx < 0:
                x += sum_arith_series(dx, min(dx + n, 0), min(n, dx))
            elif dx > 0:
                x += sum_arith_series(max(dx - n, 0) + 1, dx, min(n, dx))
            return x, sum_arith_series(dy - n + 1, dy, n)

        def check_range(n1, n2=math.inf):
            if n1 > n2:
                return False
            y = math.inf
            while n1 <= n2 and y >= min_y:
                x, y = f(n1)
                if min_x <= x <= max_x and min_y <= y <= max_y:
                    return True
                n1 += 1
            return False

        # We have that:
        # sum of [dy - n + 1, dy] <= max_y
        # (dy - n + 1 + dy) * n
        # ---------------------  <= max_y
        #         2
        # (-n + 2 * dy + 1) * n <= 2 * max_y
        # -n^2 + 2n * dy + n <= 2 * max_y
        # -n^2 + 2n * dy + n - 2 * max_y <= 0
        # n^2 - 2n * dy - n + 2 * max_y >= 0
        # n^2 - (2 * dy + 1)n + 2 * max_y >= 0
        #
        # a = 1
        # b = -2 * dy - 1
        # c = 2 * max_y
        #
        # Given that n1, n2 are roots,
        #   (n - n1)(n - n2) >= 0
        # Then, either of the following conditions has to hold:
        #   1) n - n1 >= 0 and n - n2 >= 0
        #   2) n - n1 <= 0 and n - n2 <= 0
        #
        # 1) n >= n1, n >= n2 => n >= max(n1, n2)
        # 2) n <= n1, n <= n2 => n <= min(n1, n2)
        a, b, c = 1, -2 * dy - 1, 2 * max_y
        Δ = b ** 2 - 4 * a * c
        if Δ < 0:
            return False
        n1, n2 = (-b + math.isqrt(Δ)) / (2 * a), (-b - math.isqrt(Δ)) / (2 * a)
        return check_range(1, math.ceil(min(n1, n2)) + 1) or check_range(
            math.floor(max(n1, n2)) - 1
        )

    return sum(
        check(dx, dy) for dx in range(max_x + 1) for dy in range(min_y, abs(min_y) + 1)
    )

import re
import math


def solve(data: str):
    times, distances = data.splitlines()
    dur = int("".join(re.findall(r"\d+", times)))
    record = int("".join(re.findall(r"\d+", distances)))

    # we want number of distinct integers t satisfying
    #       t(dur - t) > record
    #    => -t^2 + dur * t - record > 0
    #    => t^2 - dur * t + record < 0
    #    => (t - t1)(t - t2) < 0         {t1 < t2 are roots from quad formula}
    # so t lies between t1 and t2

    a, b, c = 1, -dur, record  # quadratic coefficients
    discrim = b * b - 4 * a * c
    t1 = (-b - math.sqrt(discrim)) / (2 * a)
    t2 = (-b + math.sqrt(discrim)) / (2 * a)

    lo = int(t1 + 1) if t1.is_integer() else math.ceil(t1)
    hi = int(t2 - 1) if t2.is_integer() else math.floor(t2)
    return hi - lo + 1

def make_year_validator(lo, hi):
    return lambda v: len(v) == 4 and all(c.isdigit() for c in v) and lo <= int(v) <= hi


def validate_height(v):
    if len(v) <= 2:
        return False
    vv, typ = v[:-2], v[-2:]
    if typ not in ("cm", "in") or any(not c.isdigit() for c in vv):
        return False
    if typ == "cm":
        return 150 <= int(vv) <= 193
    return 59 <= int(vv) <= 76


def validate_hcl(v):
    return len(v) == 7 and v[0] == "#" and all(c in "0123456789abcdef" for c in v[1:])


validators = {
    "byr": make_year_validator(1920, 2002),
    "iyr": make_year_validator(2010, 2020),
    "eyr": make_year_validator(2020, 2030),
    "hgt": validate_height,
    "hcl": validate_hcl,
    "ecl": lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda v: len(v) == 9 and all(c.isdigit() for c in v),
}


def solve(input):
    cnt = 0
    for p in input.split("\n\n"):
        seen = set()
        for l in p.split("\n"):
            for part in l.split():
                f, _, v = part.partition(":")
                if f != "cid" and validators[f](v):
                    seen.add(f)
        if len(seen) == 7:
            cnt += 1
    return cnt

def solve(data: str):
    score = 0
    for round in data.splitlines():
        opp, us = round.split()
        #   0     1        2
        # rock  paper  scissors
        opp_idx, our_idx = "ABC".index(opp), "XYZ".index(us)
        score += our_idx + 1

        # 0 beats 1, 1 beats 2, 2 beats 0
        if (opp_idx + 1) % 3 == our_idx:
            score += 6
        elif opp_idx == our_idx:
            score += 3
    return score

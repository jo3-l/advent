def solve(data: str):
    score = 0
    for round in data.splitlines():
        opp, outcome = round.split()
        opp_idx = "ABC".index(opp)
        match outcome:
            case "X":
                score += (opp_idx - 1) % 3 + 1
            case "Y":
                score += opp_idx + 1
                score += 3
            case "Z":
                score += (opp_idx + 1) % 3 + 1
                score += 6
    return score

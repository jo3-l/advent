from enum import Enum, IntEnum, auto


class Shape(IntEnum):
    R = 1
    P = 2
    S = 3


class Outcome(Enum):
    LOSS = auto()
    DRAW = auto()
    WIN = auto()


# wins_against[shape] = what wins against shape?
wins_against = {Shape.S: Shape.R, Shape.R: Shape.P, Shape.P: Shape.S}

# loses_to[shape] = what loses to shape?
loses_to = {loser: winner for winner, loser in wins_against.items()}

opponent_key = {"A": Shape.R, "B": Shape.P, "C": Shape.S}
outcome_key = {"X": Outcome.LOSS, "Y": Outcome.DRAW, "Z": Outcome.WIN}


def solve(data):
    score = 0
    for line in data.splitlines():
        enc_opponent_shape, enc_outcome = line.split()
        opponent_shape = opponent_key[enc_opponent_shape]
        outcome = outcome_key[enc_outcome]

        if outcome == Outcome.LOSS:
            score += loses_to[opponent_shape].value
        elif outcome == Outcome.DRAW:
            score += opponent_shape.value
            score += 3
        else:
            score += wins_against[opponent_shape].value
            score += 6
    return score

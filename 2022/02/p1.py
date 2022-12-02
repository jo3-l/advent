import enum


class Shape(enum.IntEnum):
    R = 1
    P = 2
    S = 3


# wins_against[shape] = what wins against shape?
wins_against = {Shape.S: Shape.R, Shape.R: Shape.P, Shape.P: Shape.S}

# loses_to[shape] = what loses to shape?
loses_to = {loser: winner for winner, loser in wins_against.items()}

opponent_key = {"A": Shape.R, "B": Shape.P, "C": Shape.S}
self_key = {"X": Shape.R, "Y": Shape.P, "Z": Shape.S}


def solve(data):
    score = 0
    for line in data.splitlines():
        enc_opponent_shape, enc_self_shape = line.split()
        opponent_shape = opponent_key[enc_opponent_shape]
        self_shape = self_key[enc_self_shape]

        score += self_shape
        if wins_against[self_shape] == opponent_shape:
            score += 6
        elif self_shape == opponent_shape:
            score += 3
    return score

K = 4


def solve(data):
    for i in range(len(data) - K):
        if len(set(data[i : i + K])) == K:
            return i + K

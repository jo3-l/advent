def solve(data: str):
    max_calories = 0
    for items in data.split("\n\n"):
        calories = sum(map(int, items.split()))
        max_calories = max(max_calories, calories)
    return max_calories

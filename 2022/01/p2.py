def solve(lines):
    all_calories = []
    for items in lines.split("\n\n"):
        calories = sum(map(int, items.split()))
        all_calories.append(calories)
    all_calories.sort()
    return sum(all_calories[-3:])

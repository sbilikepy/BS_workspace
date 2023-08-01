import math


def get_plan(current_production, month, percent):
    goals = []
    for _ in range(month):
        current_production += current_production * (percent / 100)
        if isinstance(current_production, float):
            current_production = math.floor(current_production)

        goals.append(current_production)
    return goals


print(get_plan(500, 3, 50))

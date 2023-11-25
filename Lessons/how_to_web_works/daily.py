import math


def cakes(recipe: dict, available: dict) -> int:
    result = []
    for name, amount in available.items():
        if name in recipe.keys():
            result.append(amount / recipe[name])
    for i in recipe.keys():
        if i not in available.keys():
            return 0
    return math.floor(min(result))


cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})  # 2
cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})  # 0

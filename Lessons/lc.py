import decimal
import random


def get_loot(tt: int = 0, iterations: int = 1):
    print(f"\n{'*' * 80}\nTreasure tokens amount: {tt}")
    print(f"Iterations: {tt}")
    print("*" * 80)
    drop_name = ["Prestige", "Star", "Legendary",
                 "Epic - S", "Epic - H",
                 "Rare - S", "Rare - H",
                 "Currency"]
    drop_chance = [0.01, 0.3, 5, 10, 10, 10, 10, 54.69]
    drop_ranges = [
        [0, 54.69],  # Curr
        [54.6900000001, 64.6900000001],  # R-H
        [64.6900000002, 74.6900000002],  # R-S
        [74.6900000003, 84.6900000003],  # E-H
        [84.6900000004, 94.6900000004],  # E-S
        [94.6900000005, 99.6900000004],  # L
        [99.6900000005, 99.9900000005],  # S
        [99.9900000005, 100]  # P

    ]

    loot_segments = {
        key: {drop_chance[drop_name.index(key)]: drop_ranges[::-1][
            drop_name.index(key)]} for key in
        drop_name
    }
    print(drop_name)
    print(drop_chance)
    print(drop_ranges)
    print(loot_segments)
    print("*" * 80)

    for name, percent in loot_segments.items():
        for key, val in percent.items():
            print(
                f"{name}: {' ' * ((len(name)) - 10)}"
                f" {' ' * (10 - (len(name)))} {key}% "
                f"||| Range from {val[0]}% to {val[1]}%"
            )
    print("*" * 80)
    simulation_result_dict = {key: 0 for key in drop_name}
    print(simulation_result_dict)
    for iter in range(iterations):
        print(f"Simulation #{iter + 1}")
        for i in range(0, int(tt / 50)):
            medalion = 0
            iteration = i + 1
            rand_num = random.uniform(0, 100)

            for name, value_dict in loot_segments.items():
                for percent, chance_range in value_dict.items():

                    if chance_range[0] <= rand_num <= chance_range[1]:
                        print(
                            f"Iteration #{iteration} | {rand_num} in range "
                            f"between {chance_range[0]} and {chance_range[1]} -> {name}"
                        )
                        if name =="Currency":
                            if 0 <= rand_num <= 0.3:
                                medalion += 5
                            if 0.3 <= rand_num <= 2.5:
                                medalion += 1


                        simulation_result_dict[name] += 1
    simulation_result_dict["Medallion"] = medalion
    print("*" * 80)
    return simulation_result_dict


tt = 1810
iterations = 1000
for key, value in get_loot(tt=tt, iterations=iterations).items():
    print(f"{key}: {value / iterations}")

import math, random

quality_types_names_sorted = [
    "Prestige", "Star", "Legendary",
    "Epic - Standard", "Epic - Highlight",
    "Rare - Standard", "Rare - Highlight",
]
quality_types_odds_sorted = [
    0.01, 0.3, 5,
    10, 10,
    10, 10,
    54.69
]
table_of_contents = {

}
print(table_of_contents)

example = {
    "Prestinge": {"Chibi": 0.01},
    "Star": {"Le Bunny Bonbon Bistro": 0.3}
}
data = []
dict_data = {}
for i in range(1, 11):
    print(f"Key {i} has been initialized")
    dict_data[i] = 0

for i in range(10 ** 6):
    rand_key = random.randint(1, 10)
    dict_data[random.randint(1, 10)] += 1

print(dict_data)
print(len(dict_data))

for k, v in dict_data.items():
    print(f"{k} = {v}")

print(
    f"min value: {min(dict_data.values())},\n"
    f"avg value: {int(sum(dict_data.values()) / len(dict_data))} \n"
    f"max value: {max(dict_data.values())}\n"
    f"max difference: {max(dict_data.values()) - min(dict_data.values())}"
)

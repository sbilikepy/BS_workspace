from datetime import datetime

from data import traits, champions, composition_iterator

current_composition = []
current_traits = {}


def timer(func):
    start = datetime.now()

    def wrapper(*args, **kwargs):
        func()

    end = datetime.now()
    print(f"{func.__name__} execution takes {end - start}s.")

    return wrapper


@timer
def data_fill():
    for composition in composition_iterator:
        trait_champions = composition[0]
        trait_name = composition[1]

        for champion in trait_champions:
            champions[champion].append(trait_name)


def request():
    print("Enter \"help\" to calculate")

    flag = True
    while flag:

        character = input("Character name: ").lower()
        if character.capitalize() in current_composition:
            print(f"{character.capitalize()} already here")
        if character == "help":
            return

        if character.capitalize() == "Akali":
            if "Akali" not in current_composition:
                akali_spec = None
                while akali_spec not in ("1", "2"):
                    akali_spec = input("\nAkali spec: \n1. K/DA\n2. True Damage\n")

                if akali_spec == "1":
                    champions["Akali"].append("K/DA")
                    print("K/DA Akali has been added\n")
                    current_composition.append("Akali")
                if akali_spec == "2":
                    champions["Akali"].append("True Damage")
                    print("True Damage Akali has been added\n")
                    current_composition.append("Akali")


        else:
            if any(character == champ.lower() for champ in champions.keys()):
                if character.lower() not in [i.lower() for i in current_composition]:
                    current_composition.append(character.capitalize())
                    print(f"{character.capitalize()} has been added\n")
            else:
                print("Enter a valid character\n")


def tailor():
    print("*" * 50, "\n")
    if not len(current_composition):
        return
    print(f"Your composition: {current_composition}")
    # current_traits = {}

    for character in current_composition:
        for trait in champions[character]:
            current_traits[trait] = current_traits.get(trait, 0) + 1

        for trait in champions[character]:
            if current_traits[trait] == traits[trait][-1]:
                current_traits[trait] = f"{current_traits.get(trait, 0)} CAPPED"

            if current_traits[trait] in traits[trait]:
                current_index = traits[trait].index(current_traits[trait])
                next_upgrade = traits[trait][current_index + 1] - current_traits[trait]
                current_traits[trait] = f"{current_traits.get(trait, 0)} BREAKPOINT [ -> {next_upgrade}]"

        current = current_traits.get(trait, 0)
        for non_breakpoint in traits[trait]:
            if int(current) < int(non_breakpoint):
                current_traits[trait] = f"{current_traits.get(trait, 0)} [you need +{non_breakpoint - int(current)}]"
                break


    print("Your traits:")
    print(current_traits)
    # CAPPED
    for key, value in current_traits.items():
        if isinstance(value, str):
            if "CAPPED" in value:
                print(key, value)
    # BREAKPOINT
    for key, value in current_traits.items():
        if isinstance(value, str):
            if "BREAKPOINT" in value:
                print(key, value)
    for key, value in current_traits.items():
        if isinstance(value, str) and "+" in value:
            print(f"{key}: {value}")


if __name__ == "__main__":
    data_fill()

    print("\n")
    print("*" * 50, "\n")
    request()
    tailor()

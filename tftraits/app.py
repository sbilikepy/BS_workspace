from flask import Flask, render_template, request, redirect
from datetime import datetime
from data import traits, champions, composition_iterator

app = Flask(__name__)

current_composition = []
current_traits = {}
capped_traits = []
breakpoint_traits = []
remaining_traits = []
first_prior = []
second_prior = []
third_prior = []
no_prior = []


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"\n{func.__name__} execution takes {end - start}s.\n")

    return wrapper


@app.route('/reset', methods=['POST'])
def reset():
    current_composition.clear()
    current_traits.clear()
    capped_traits.clear()
    breakpoint_traits.clear()
    remaining_traits.clear()
    first_prior.clear()
    second_prior.clear()
    third_prior.clear()
    no_prior.clear()
    return redirect('/')


@timer
def data_fill():
    for composition in composition_iterator:
        trait_champions = composition[0]
        trait_name = composition[1]
        for champion in trait_champions:
            champions[champion].append(trait_name)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        character = request.form['character'].lower()
        if character.capitalize() in current_composition:
            print(f"{character.capitalize()} already here")
        elif character.capitalize() == "help":
            return render_template('index.html',
                                   composition=current_composition,
                                   capped_traits=capped_traits,
                                   breakpoint_traits=breakpoint_traits,
                                   remaining_traits=remaining_traits,
                                   first_prior=first_prior,
                                   second_prior=second_prior,
                                   third_prior=third_prior,
                                   no_prior=no_prior,
                                   suggestions=None)
        elif character.capitalize() == "akali":
            akali()
        elif any(character == champ.lower() for champ in champions.keys()):
            if character.lower() not in [i.lower() for i in current_composition]:
                current_composition.append(character.capitalize())
                print(f"{character.capitalize()} has been added\n")
        else:
            print("Enter a valid character\n")

    group_data()
    suggestions = tailor()
    return render_template('index.html',
                           composition=current_composition,
                           capped_traits=capped_traits,
                           breakpoint_traits=breakpoint_traits,
                           remaining_traits=remaining_traits,
                           first_prior=first_prior,
                           second_prior=second_prior,
                           third_prior=third_prior,
                           no_prior=no_prior,
                           suggestions=suggestions)


def group_data():
    current_traits.clear()
    capped_traits.clear()
    breakpoint_traits.clear()
    remaining_traits.clear()
    first_prior.clear()
    second_prior.clear()
    third_prior.clear()
    no_prior.clear()

    print("*" * 50, "\n")
    if not current_composition:
        return

    print(f"Your composition: {current_composition}")

    for character in current_composition:
        for trait in champions[character]:
            current_traits[trait] = current_traits.get(trait, 0) + 1

    for trait, count in current_traits.items():
        if count == traits[trait][-1]:
            capped_traits.append(f"{trait}: {count} | CAPPED")
            no_prior.append(trait)
        elif count in traits[trait]:
            current_index = traits[trait].index(count)
            next_upgrade = traits[trait][current_index + 1] - count
            breakpoint_traits.append(f"{trait}: {count} | BREAKPOINT [+{next_upgrade}]")
            if next_upgrade == 1:
                first_prior.append(trait)
        else:
            remaining_traits.append(f"{trait}: {count} [+{traits[trait][0] - count}]")
            if (traits[trait][0] - count) == 1:
                second_prior.append(trait)
            if (traits[trait][0] - count) > 1:
                third_prior.append(trait)


def tailor():
    print(f"\n\nFirst prio: {first_prior}")
    print(f"Second prio: {second_prior} ")
    print(f"Third prio: {third_prior}")
    print(f"No prio: {no_prior}\n\n")
    suggestions = {
        name: 0 for name in champions.keys()
    }

    for trait in first_prior + second_prior + third_prior + no_prior:

        for name, traits in champions.items():
            if name not in current_composition:

                if trait in first_prior:
                    if trait in traits:
                        suggestions[name] += 3

                if trait in second_prior:
                    if trait in traits:
                        suggestions[name] += 2

                if trait in third_prior:
                    if trait in traits:
                        suggestions[name] += 1

                if trait in no_prior:
                    if trait in traits:
                        suggestions[name] += 0

    suggestions = dict(sorted(suggestions.items(), key=lambda item: item[1], reverse=True))

    scoreboard = {}

    for character, score in suggestions.items():
        if score not in scoreboard:
            scoreboard[score] = [character]
        else:
            scoreboard[score].append(character)

    result = {}
    for score, characters in scoreboard.items():
        result[score] = characters

    return result


def akali():
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


if __name__ == "__main__":
    data_fill()
    app.run(debug=False)

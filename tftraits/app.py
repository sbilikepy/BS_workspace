from flask import Flask, render_template, request, redirect, session
from datetime import datetime
from data import traits, champions, composition_iterator
import os

app = Flask(__name__)
app.secret_key = "woahtopsecretkey"

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"\n{func.__name__} execution takes {end - start}s.\n")

    return wrapper

@timer
def data_fill():
    for composition in composition_iterator:
        trait_champions = composition[0]
        trait_name = composition[1]
        for champion in trait_champions:
            champions[champion].append(trait_name)

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'current_composition' not in session:
        session['current_composition'] = []
    if 'current_traits' not in session:
        session['current_traits'] = {}
    if 'capped_traits' not in session:
        session['capped_traits'] = []
    if 'breakpoint_traits' not in session:
        session['breakpoint_traits'] = []
    if 'remaining_traits' not in session:
        session['remaining_traits'] = []
    if 'first_prior' not in session:
        session['first_prior'] = []
    if 'second_prior' not in session:
        session['second_prior'] = []
    if 'third_prior' not in session:
        session['third_prior'] = []
    if 'no_prior' not in session:
        session['no_prior'] = []

    if request.method == 'POST':
        character = request.form['character'].lower()
        if character.capitalize() in session['current_composition']:
            print(f"{character.capitalize()} already here")
        elif character.capitalize() == "help":
            return render_template('index.html',
                                   composition=session['current_composition'],
                                   capped_traits=session['capped_traits'],
                                   breakpoint_traits=session['breakpoint_traits'],
                                   remaining_traits=session['remaining_traits'],
                                   first_prior=session['first_prior'],
                                   second_prior=session['second_prior'],
                                   third_prior=session['third_prior'],
                                   no_prior=session['no_prior'],
                                   suggestions=None)
        elif character.capitalize() == "akali":
            akali()
        elif any(character == champ.lower() for champ in champions.keys()):
            if character.lower() not in [i.lower() for i in session['current_composition']]:
                session['current_composition'].append(character.capitalize())
                print(f"{character.capitalize()} has been added\n")
        else:
            print("Enter a valid character\n")

    group_data()
    suggestions = tailor()
    return render_template('index.html',
                           composition=session['current_composition'],
                           capped_traits=session['capped_traits'],
                           breakpoint_traits=session['breakpoint_traits'],
                           remaining_traits=session['remaining_traits'],
                           first_prior=session['first_prior'],
                           second_prior=session['second_prior'],
                           third_prior=session['third_prior'],
                           no_prior=session['no_prior'],
                           suggestions=suggestions)

def group_data():
    session['current_traits'].clear()
    session['capped_traits'].clear()
    session['breakpoint_traits'].clear()
    session['remaining_traits'].clear()
    session['first_prior'].clear()
    session['second_prior'].clear()
    session['third_prior'].clear()
    session['no_prior'].clear()

    print("*" * 50, "\n")
    if not session['current_composition']:
        return

    print(f"Your composition: {session['current_composition']}")

    for character in session['current_composition']:
        for trait in champions[character]:
            session['current_traits'][trait] = session['current_traits'].get(trait, 0) + 1

    for trait, count in session['current_traits'].items():
        if count == traits[trait][-1]:
            session['capped_traits'].append(f"{trait}: {count} | CAPPED")
            session['no_prior'].append(trait)
        elif count in traits[trait]:
            current_index = traits[trait].index(count)
            next_upgrade = traits[trait][current_index + 1] - count
            session['breakpoint_traits'].append(f"{trait}: {count} | BREAKPOINT [+{next_upgrade}]")
            if next_upgrade == 1:
                session['first_prior'].append(trait)
        else:
            session['remaining_traits'].append(f"{trait}: {count} [+{traits[trait][0] - count}]")
            if (traits[trait][0] - count) == 1:
                session['second_prior'].append(trait)
            if (traits[trait][0] - count) > 1:
                session['third_prior'].append(trait)

def tailor():
    print(f"\n\nFirst prio: {session['first_prior']}")
    print(f"Second prio: {session['second_prior']} ")
    print(f"Third prio: {session['third_prior']}")
    print(f"No prio: {session['no_prior']}\n\n")
    suggestions = {
        name: 0 for name in champions.keys()
    }

    for trait in session['first_prior'] + session['second_prior'] + session['third_prior'] + session['no_prior']:
        for name, traits in champions.items():
            if name not in session['current_composition']:
                if trait in session['first_prior']:
                    if trait in traits:
                        suggestions[name] += 3

                if trait in session['second_prior']:
                    if trait in traits:
                        suggestions[name] += 2

                if trait in session['third_prior']:
                    if trait in traits:
                        suggestions[name] += 1

                if trait in session['no_prior']:
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
    if "Akali" not in session['current_composition']:
        akali_spec = None
        while akali_spec not in ("1", "2"):
            akali_spec = input("\nAkali spec: \n1. K/DA\n2. True Damage\n")

        if akali_spec == "1":
            champions["Akali"].append("K/DA")
            print("K/DA Akali has been added\n")
            session['current_composition'].append("Akali")
        if akali_spec == "2":
            champions["Akali"].append("True Damage")
            print("True Damage Akali has been added\n")
            session['current_composition'].append("Akali")

if __name__ == "__main__":
    data_fill()
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

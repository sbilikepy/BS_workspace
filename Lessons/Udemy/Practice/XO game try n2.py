import webbrowser

game_over = 0
turn_counter_from = 9
current_player = "X"
x_player = "X"
o_player = "O"
cell_pares = {  # DICT
    "cell_1": "1",
    "cell_2": "2",
    "cell_3": "3",
    "cell_4": "4",
    "cell_5": "5",
    "cell_6": "6",
    "cell_7": "7",
    "cell_8": "8",
    "cell_9": "9",
}
game_field = (
    f"{cell_pares['cell_1']} | "  # FIELD VISUAL
    f"{cell_pares['cell_2']} | "
    f"{cell_pares['cell_3']} \n"
    f"{cell_pares['cell_4']} | "
    f"{cell_pares['cell_5']} | "
    f"{cell_pares['cell_6']} \n"
    f"{cell_pares['cell_7']} | "
    f"{cell_pares['cell_8']} | "
    f"{cell_pares['cell_9']}  "
)

print(
    f"Hello! Lets play tic-tac-toe.\n"  # MAIN PART
    f"Field looks like this: \n"
    f"{game_field}\n"
    f"Every cell have index from 0 to 9\n"
    f"First player start with 'X'"
)

while turn_counter_from > 1:  # LOGIC
    while game_over == 0:
        if (
            {cell_pares["cell_1"]} == {cell_pares["cell_2"]} == {cell_pares["cell_3"]}
        ):  # WIN CONDITION
            print(f"'{current_player}' player WIN with 1 2 3 combo")
            game_over = 1
            turn_counter_from = 0
        if {cell_pares["cell_4"]} == {cell_pares["cell_5"]} == {cell_pares["cell_6"]}:
            print(f"'{current_player}' player WIN with 4 5 6 combo")
            game_over = 1
            turn_counter_from = 0
        if {cell_pares["cell_7"]} == {cell_pares["cell_8"]} == {cell_pares["cell_9"]}:
            print(f"'{current_player}' player WIN with 7 8 9 combo")
            game_over = 1
            turn_counter_from = 0
        if {cell_pares["cell_1"]} == {cell_pares["cell_4"]} == {cell_pares["cell_7"]}:
            print(f"'{current_player}' player WIN with 1 4 7 combo")
            game_over = 1
            turn_counter_from = 0
        if {cell_pares["cell_2"]} == {cell_pares["cell_5"]} == {cell_pares["cell_8"]}:
            print(f"'{current_player}' player WIN with 2 5 8 combo")
            game_over = 1
            turn_counter_from = 0
        if {cell_pares["cell_3"]} == {cell_pares["cell_6"]} == {cell_pares["cell_9"]}:
            print(f"'{current_player}' player WIN with 3 6 9 combo")
            game_over = 1
            turn_counter_from = 0
        if {cell_pares["cell_1"]} == {cell_pares["cell_5"]} == {cell_pares["cell_9"]}:
            print(f"'{current_player}' player WIN with 1 5 9 combo")
            game_over = 1
            turn_counter_from = 0
        if {cell_pares["cell_3"]} == {cell_pares["cell_5"]} == {cell_pares["cell_7"]}:
            print(f"'{current_player}' player WIN with 3 5 7 combo")
            game_over = 1
            turn_counter_from = 0

        if game_over == 1:
            print("GAME OVER")
            webbrowser.open(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8gTahxFSuUI-JyGRdyc8B0HftQK5Kgu_YHg&usqp=CAU"
            )
        if turn_counter_from == 1:
            print(f"You have last one turn to play")
        if turn_counter_from > 0:
            print(f"You have {turn_counter_from} more turns to play")

        if game_over == 0:  # INPUT PART
            player_choose = input("Choose cell number: ")
            print(f"__________________________________________________")
            print(f"Player '{current_player}' choose cell № {player_choose}")
            for key, value in cell_pares.items():
                if player_choose == value:
                    cell_pares[key] = f"{current_player}"
                    print(f"__________________________________________________")
                    game_field = (
                        f"{cell_pares['cell_1']} | "
                        f"{cell_pares['cell_2']} | "
                        f"{cell_pares['cell_3']} \n"
                        f"{cell_pares['cell_4']} | "
                        f"{cell_pares['cell_5']} | "
                        f"{cell_pares['cell_6']} \n"
                        f"{cell_pares['cell_7']} | "
                        f"{cell_pares['cell_8']} | "
                        f"{cell_pares['cell_9']}  "
                    )
                    print(f"Bord now looks like this:\n" f"{game_field}")
                    if current_player == "X":
                        current_player = o_player
                    else:
                        current_player = "X"
                    turn_counter_from -= 1

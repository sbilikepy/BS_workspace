# А вот и новое домашнее задание. Непростое. Но вполне реализуемое.
# Вы попробуете реализовать игру в крестики-нолики размером 3х3 -
# самые что ни наесть обыкновенные.
# Сделайте метод, который выводит на каждом ходу текущее положение
# с линейками, крестиками и ноликами (используйте буквы X и O в качестве крестиков и ноликов) -
# так игрокам будет удобнее ориентироваться. Подсказка: если надо вывести строку
# без перевода коретки на новую строку, используйте функцию print и передавайте параметр end=''.
# Также вам понадобится реализовать способ проверки наличия выигрышной
# комбинации. Подсказа: договоримся, что клетки поля будут пронумерованы
# от 0 до 8 и пользователи будут вводить индекс поля, чтобы поставить там
# крестик или нолик.
# Для упрощения - тот кто ходит первым - ставит крестик.
def lets_play():
    max_turns = 9
    game_over = 0
    next_trun_player = ""
    cell_1 = "_"
    cell_2 = "_"
    cell_3 = "_"
    cell_4 = "_"
    cell_5 = "_"
    cell_6 = "_"
    cell_7 = " "
    cell_8 = " "
    cell_9 = " "
    game_field = (
        f" {cell_1}|{cell_2}|{cell_3}\n"
        f" {cell_4}|{cell_5}|{cell_6}\n "
        f"{cell_7}|{cell_8}|{cell_9}\n"
    )
    print(game_field)
    player_1_choose = input(str("choose X or O: "))
    p1_class = player_1_choose
    p2_class = ""
    if p1_class == "X":
        p2_class = "O"
        next_turn_player = "O"
    else:
        p2_class = "X"
        next_turn_player = "X"
    print(f"Player 1 choose '{p1_class}'")
    print(f"Player 2 playing '{p2_class}' then")
    first_turn = input(
        "All cells on game field have indexes, input your "
        "index to put your symbol on game board\n"
        " 1|2|3 \n 4|5|6 \n 7|8|9 \n"
        "First player choose cell №  "
    )
    while max_turns >= 1:
        if first_turn == "1":
            cell_1 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_1 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "2":
            cell_2 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "2":
                cell_2 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "3":
            cell_3 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_3 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "4":
            cell_4 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_4 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "5":
            cell_5 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_5 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "6":
            cell_6 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_6 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "7":
            cell_7 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_7 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "8":
            cell_8 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_8 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if first_turn == "9":
            cell_9 = p1_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )
            max_turns -= 1
            next_turn_player = input("Next player choose cell №  ")
            if next_turn_player == "1":
                cell_9 = p2_class
            print(
                f" {cell_1}|{cell_2}|{cell_3}\n"
                f" {cell_4}|{cell_5}|{cell_6}\n "
                f"{cell_7}|{cell_8}|{cell_9}\n"
            )

        if cell_1 == cell_2 == cell_3:
            if cell_1 != "_" and " ":
                print(f"{cell_1} player WIN with 1 2 3 comboo")
        if cell_4 == cell_5 == cell_6:
            if cell_4 != "_" and " ":
                print(f"{cell_1} player WIN with 456 combo")
        if cell_7 == cell_8 == cell_9:
            if cell_7 != " " and "_":
                print(f"{cell_1} player WIN with 789 combo")
        if cell_1 == cell_4 == cell_7:
            if cell_1 != "_" and " ":
                print(f"{cell_1} player WIN with 147 combo")
        if cell_2 == cell_5 == cell_8:
            if cell_2 != "_" and " ":
                print(f"{cell_1} player WIN with 258 combo")
        if cell_3 == cell_6 == cell_9:
            if cell_3 != "_" and " ":
                print(f"{cell_1} player WIN 369")
        if cell_1 == cell_5 == cell_9:
            if cell_1 != "_" and " ":
                print(f"{cell_1} player WIN 159")
        if cell_3 == cell_5 == cell_7:
            if cell_3 != "_" and " ":
                print(f"{cell_1} player WIN 357")


lets_play()

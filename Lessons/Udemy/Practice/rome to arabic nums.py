# Написать функцию, которая принимает на вход строку - римское число,
# а возвращает это число в арабском виде. Например, если передаём "XV" - должна
# вернуть 15, если передаём "IV" - должна вернуть 4.
# Вот список римских символов и их отображение на арабские числа:
# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000
# Варианты типа IIIV = 5-3 = 2 мы не рассматриваем. Хотя Римляне и пользовались
# иногда такими видами записей, но есть разная информация о приемлимости оных.
# В нашем ДЗ такие варианты мы не рассматриваем. Вот выдержка из wiki:
# "Необходимо отметить, что другие способы «вычитания» недопустимы; так, число
# 99 должно быть записано как XCIX, но не как IC."
# Подсказка. Для решения надо реализовать два правила:
# Правила записи чисел римскими цифрами:

# - если большая цифра стоит перед меньшей, то они складываются (принцип сложения),
# - если меньшая цифра стоит перед большей, то меньшая вычитается из большей (принцип вычитания).

# Защиту от некорректного ввода реализовать по вашему желанию (можно не делать, но для
# тренировки всегда полезно).


def rome_to_arabic():
    rome = input('input your rome number here: ')
    pares = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    cycle_range = range(1, len(rome))
    arabic_list = []
    cycle_counter = 0
    increment = 0
    decrement = 0
    result = 0

    print(f'input rome len = {len(rome)}')
    print(f'current cycle range len = {len(cycle_range)}')

    print('_____________________________________________')
    print('_____________________________________________')

    for rome_number in rome:
        for k, v in pares.items():
            if rome_number == k:
                print('_________')
                print(f'current rome number = {rome_number}, his arabic pare = {v}')
                arabic_list.append(v)
                print(f'arabic_list in process: {arabic_list}')
    print('_____________________________________________')
    print('_____________________________________________')
    print('we have next index/value pares in arabic_list')
    for index, value in enumerate(arabic_list):
        print((index, value))

    for i, j in enumerate(arabic_list[:-1]):
        if j >= arabic_list[i + 1]:
            increment += arabic_list[i]
        else:
            decrement += arabic_list[i]

    result = increment + arabic_list[-1] - decrement
    print('_____________________________________________')
    print('_________________result_section______________')
    print(f'{rome} = {result}')
    return result


###


rome_to_arabic()

# Реализуйте одну классическую и достаточно простую игру: "угадай число".
#
# Компьютер загадывает число от 1 до 50 и даёт 6 попыток пользователю, чтобы
# тот смог угадать загаданное число. Когда пользователь вводит число, компьютер
# проверяет угадано ли число и если не угадано, то сообщает пользователю меньше
# ли или больше загаданое число. Если пользователь угадал - то сообщает о том,
# что число отгадано.
#
# Подсказка: для "загадывания" числа используйте модуль random: импортируйте
# его и для генерации (загадывания) числа вызовите метод random.randint(1, 50).


import random
random_num = random.randint(1, 100)

attempt_range = range (1,6)
attempt_start = 6
attempt_final = 7 - attempt_start
attempt_match = attempt_start - 1
user_num = int(input('your num please: '))

for n in attempt_range:
    if user_num == random_num:
        print(f'You won, gj')
        break
    if user_num > random_num:
        attempt_start -= 1
        print(f'answer num LOWER than your, you have {attempt_start} more attempts')
        user_num = int(input('your num please: '))
    if user_num < random_num:
        attempt_start -= 1
        print(f'answer num GREATER than your, you have {attempt_start} more attempts')
        user_num = int(input('your num please: '))
    if attempt_start == 0:
        break








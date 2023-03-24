numbers = [1, 2, 3]
numbers.append(4)
help(numbers.append)  # позволяет получить документацию.

print('________________встроенные функции математические_________________')

print(abs(-1))  # abs берет модуль
print(max(1, 2, 3, 4, 5))  # берет максимальное значение,
print(min([1, 2, 3, 4, 5]))  # работает со списками
print(pow(2, 8))  # возведение в степень, 2**8
print(round(3.37, 1))  # округление, 1 - значение, 2 - кол-во агрументов после точки
print(sum([1, 2, 3, 4, 5]))  # суммирует тольк осписки
h = hex(42)  # вывод в 16-ти ричную систему
o = oct(42)  # вывод в 8-ми ричный формат (самый редкий)
b = bin(42)  # вывод в 2-ичную систему (бинарную)
print(h, o, b)

print('________________встроенные функции с итерируемыми объектами_________________')

all_true1 = all([True, True, True])  # cтановится тру, если все элементы тру
all_true2 = all([True, False, False])
print(all_true1, all_true2)

players = [('Carlsen', 2842), ('Caruana', 2822), ('Mamedyarov', 2801), ('Giri', 2780), ('Ding', 2797)]
print(all(rating > 2800 for _, rating in players))  # all( b > 123 for name, b in (X)
print(all([rating > 2800 for _, rating in players]))  # all( b > 123 for name, b in (X), медленный вариант
                                                        #  вызова

any # хотя бы 1 элем должен быть тру для тру, а фолс вернется только если все фолс
any_true1 = any([True, False, False])
any_true2 = any([False, False, False])
print(any_true1, any_true2)

players = [('Carlsen', 2842), ('Caruana', 2822), ('Mamedyarov', 2801), ('Giri', 2780), ('Ding', 2797)]
print(any([rating < 2790 for _, rating in players]))
print(any([rating < 2700 for _, rating in players]))

letters = 'abcd'
numbers = (10,20,30) #tuple
zipped = zip(letters, numbers
             )
print(zipped)
print(type(zipped))
zipped_list = list(zipped) # срабатывает только после конструктора лист
print(zipped_list)            # излишние элементы будут отсечены



names = ['Carlsen', 'Caruana', 'mamedyarov', "Ding", "Giri"]
ratings = [2842, 2822, 2801, 2797, 2780]
players = dict(zip(names, ratings))                # зип со словарём
print(players)




code = ord('a')      # конверт в юникод для работы на низком уровне
print(code)
c = chr(97)          # конверт из юникода для работы на низком уровне
print(c)
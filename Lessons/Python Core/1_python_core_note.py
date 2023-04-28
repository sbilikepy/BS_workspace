# result = 2 > 1
# print(type(result))
#
# print(2 > 2)
# print(2 >= 2)
# print(3 >= 2)
# print(3 >= 4)
#
# print(2 < 3)
# print(3 < 2)
# print(3 <= 3)
# print(3 <= 2)
# print(3 <= 4)
#
# 1 != 1
# 2 != 1
#
# print('string' == 'string')
# print('string' == 'str1ng')
# print('________________________________________')
# print('strinG'.lower() == 'string'.lower())
# print('__')
# print('__')
# print('________________________________________')
# print(1 < 2 < 3)
# 1 < 2 and 2 < 3
#
# print('________________________________________')
# print('________________________________________')
#
# 1 > 2 or 2 < 3
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
#
# should_open_file = None
# is_admin = True  # pretend asking for security module
# file_exist = True  # pretend asking OS about file existance
# if is_admin and file_exist == True:
#     should_open_file = True
#     print('ACCESS SUCCESSFUL')
# else:
#     print('ACCESS DENIED GO HOME BUDDY')
# print(should_open_file)
#
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
# print('________________________________________')
#
# mount_list = "[Goldenmane's Reins]"
# mount_list = mount_list.strip('[')
# mount_list = mount_list.strip(']')
# print(mount_list)
#
# "r" - только
# чтение
# "r+" - и
# чтение
# и
# запись, при
# открытии
# в
# таком
# режиме
# файл
# должен
# существовать
# "w" - Write - создаёт, данные
# перезаписываются
# "w+" - Write - открывается
# на
# чтение
# и
# запись, данные
# перезаписываются
# если
# он
# существовал, если
# не
# существовал - то
# создаем
# "x" - Create - will
# create
# a
# file, returns
# an
# error if the
# file
# exist
# "a" - Append - will
# create
# a
# file if the
# specified
# file
# does
# not exist, добавляет
# в
# конец, файл
# не
# создается
#
# import getpass  # показывает текущую директорию
#
# print(getpass.getuser())
# with open('test.txt', 'w') as f:  # write
#     f.write(
#         '\n name | phone'
#         '\n John;1234'
#         '\n Bob;5678'
#         '\n Alice;9432')
#
#     f.close()
#
# file = open('test.txt')
# data = file.read()
# print(data)
# print(type(data))
#
# print(file.read())  # курсор в конце файла
# file.seek(0)  # курсор на 0 байт
# print(file.read())
# file.seek(0)
# lines = file.readlines()  # возвращает список list
# print(type(lines))
# print(lines)
# print(lines)
# print(type(lines))
# print(len(lines))
#
# print(file.closed)
#
# with open('test.txt') as sample_file:
#     sample_data = sample_file.read()
#     print(sample_data)
#
# f = open("test.txt", "r")  # read
# print(f.read())
# data = f.read()
# print(data)
# print('__________________________________________________________')
# with open('test.txt', mode='a') as sample_file:  # ОТДЕЛЬНО ЧТЕНИЕ  И ЗАПИСЬ
#     sample_file.write('Eric;7639')
# with open('test.txt', mode='r') as sample_file:
#     print(sample_file.read())
#
# print('__________________________________________________________')
# print('__________________________________________________________')
#
# with open('test.txt', mode='r+') as sample_file:
#     sample_file.seek(0, 2)  # (0, 1, 2) начало, след после курсора, конец)
#     sample_file.write('\nToub:3453')
#     sample_file.seek(0)
#     print(sample_file.read())
#
# with open('abracadabra.txt', mode='w+') as spell_file:
#     spell_file.write('abra-abra')
#     spell_file.seek(0)
#     print('__________________________________________________________')
#     print(spell_file.read())
# import sys
#
# my_utf = sys.getdefaultencoding()
# print(my_utf)
#
# print(ord('a'))  # узнать код utf
# print(chr(int('97')))  # узнать символ по коду
# print(chr(int('198')))
# s = 'hello'
# enc_ascii = s.encode('ascii')
# enc_utf8 = s.encode('utf8')
# enc_utf16 = s.encode('utf16')
#
# print(type(enc_ascii))
# print(enc_ascii)
# print(enc_utf8)
# print(enc_utf16)
#
# print(len(enc_ascii))
# print(len(enc_utf8))
# print(len(enc_utf16))
# print('_________________________')
# str_in_bytes = b'hello'
# print(str_in_bytes)
# str_in_bytes = s.encode('utf8')
#
# str_in_text = 'hello'
#
# print(type(str_in_bytes))
# print(type(str_in_text))
#
# print('bytes'.encode('utf8'))
# print('байты'.encode('utf8'))
# print('_________________________')
# print(str_in_bytes[0])
# print(str_in_text[0])
#
# ba = bytearray(b'hello')
# ba[0] = 87
# print(ba)
# print('_________________________')
#
# result = str(str_in_bytes)  # бред
# print(result)  # бред
# print(len(result))  # бред
#
# print('_________________________')
# result = str(str_in_bytes, 'utf8')
# print(result)
# print('_________________________')
# result = str_in_bytes.decode('utf8')  # функция не отрботает, если не передать таблицу
# print(result)
# print('___________qwwqwqwq______')
# jpeg = [120, 3, 255, 0, 100]
# with open(r'C:\Users\BS_HOME\Desktop\my files\Other\валлпаперс\1.jpg', 'w+b') as file:
#     file.write(bytes(jpeg))
# with open(r'C:\Users\BS_HOME\Desktop\my files\Other\валлпаперс\1.jpg', 'rb') as file:
#     data = file.read()
#     for b in data:
#         print(int(b))
# name_b = 'Bohdan'
# print('my name is {}'.format(name_b))
# name_b = 'Bohdan'
# print("my name is {0} and i'm {1}".format(name_b, 27))
# pi = 3.1415
# print(pi)
# print('Pi equals {pi:1.2f}'.format(pi=pi))  # .2 = 2 числа после запятой    # f = форматирование
# name = 'bodan'
# age = 30
# print(f"My name is {name} and i'm {age}")  # что бы не прописывать формат в конце можно
# # использовать f перед '/" для вызова функции .format
#
#
# print(f'P equals {pi:1.2f}')  # 1.2f
#
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# for i in numbers:
#     print(i)
#
# for i in numbers:
#     print(i * i)
#
# numbers = range(1, 6)  # последняя граница не включается в вывод
# print(type(numbers))
#
# for i in numbers:
#     print(i)
#
# for i in range(1, 6):
#     print(i)
#
# for i in range(1, 6):
#     if i % 2 == 0:
#         print((f'{i} is even'))
#     else:
#         print((f'{i} is odd'))
#
# print('______')
#
# numbers = [1, 3, 5, 7, 9]
# for i, item in enumerate(numbers):
#     numbers[i] *= 2
# print(numbers)
#
# print('_________________________________')
#
# name = "John"
# for i in name:
#     print(i)
#
# for _ in range(5):  # _ если нет необходимости именовать
#     print('Povitryana tryvoga!')
#
# person = "John", 'Silver', 22
# for _ in person:
#     print(_)
#
# print('_________________________________')
#
# persons = [('John', 22,), ('Bob', 32), ('Dave', 20)]
# print(len(persons))
#
# tuple
# unpacking
# for (name, age) in persons:
#     print(f'{name} is {age} year\'s old')
#
# print('_________________________________')
#
# players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801)
# for name in players:
#     print(name)
#
# for item in players.items():
#     print(item)
#
# for k, v in players.items():  # 1-я переменная кей, а вторая ЗНАЧЕНИЕ В ДИКТЕ
#     print(f'{k} have {v} elo')
#
# for v in players.values():  # 1-я переменная кей, а вторая ЗНАЧЕНИЕ В ДИКТЕ
#     print(v)
#
# find
# all
# pairs
# sum
# of
# wich
# equals
# 0
# list1 = [2, 4, -5, 6, 8, -2]
# list2 = [2, -6, 8, 3, 5, -2]
# pairs = []
# for x in list1:
#     for y in list2:
#         if x + y == 0:
#             print('______________________')
#             print(f'{x} + {y} = 0')
#             pair = [x, y]
#             pairs.append((pair))
#
# print(f'\n what we have for now:\n{pairs}')
#
# print(type(pairs))
#
# Cписок
# пар
# ключ: значение
# записные
# книги, логин - пароли
# print('________________________')
# Поиск
# по
# ключу
# намного
# быстрее
# чем
# поиск
# по
# значению
# Поиск
# по
# ключу - мгновенный
#
# Summary
# Let
# me
# summarize
# what
# we
# found
# out
# with our performance tests:
#
# If
# you
# focus
# on
# performance, use
# {}
# When
# merging
# dictionaries(without
# changing
# either
# of
# them), use
# .copy().update()
# for dictionaries with more than 15 elements
# dict(a, **b)
# for smaller dictionaries
#
# qwe = 'a'
# test = {
#     qwe: 1,
#     'b': 2,
#     'd': 4,
#     'c': 3
# }
# players = {
#     'Carlsen': 2842,  # КЛЮЧ - ЗНАЧЕНИЕ chess players name : elo           {} a : b,
#     'Caruana': 2822,  # KEYS  - VALUES
#     'Mamedyarov': 2801,
#     'Ding': 2797,
#     'Giri': 2780
# }
# print('________________________')
# players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801, Ding=2797, Giri=2780)  # переназначение
# print(players)
# print('________________________')
# top1 = players['Carlsen']
# print(f"Top chess player's rating is {top1}")
# print(list(players))
# print(sorted(players))  # сортировка по названию
# print('________________________')
# print(list(test))
# print(sorted(test))
# print(('Carlsen' in players))
#
# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# print(dict({('sape', 4139), ('guido', 4127), ('jack', 4098)}))
#
# print(players.get('Carlsen'))
# players['so'] = 2780
# print(players)
# print('so' in players)
# print(players)
# del players['so']
# print(players)
# keys = players.keys()
# print(type(keys))
# print(keys)
# l = list(players.keys())
# print(type(l))
# print(sorted(players.keys()))
# print('Carlsen' in players)
# print('Kramnik' not in players)
# vals = players.values()
# print(type(vals))
#
# vals = list(players.values())
# print(type(vals))
# print(sorted(players.values()))
# players_copy = players.copy()
# print('________________________')
# print(players_copy)
#
# for k, v in players.items():
#     print(k, v, 'q')
#
# items = players.items()
# print(type(items))
# players.pop('Giri')
# print(players)
# print(players.popitem())
# print(players)
# print(len(players))
# players.setdefault('Karjakin')  # .SETDEFAULT если запрашиваемого элем.
# нет, то
# ключ
# добавляется, а
# значение
# становится
# NONE
# print(players)
# print(('_________________________________'))
# print(('_________________________________'))
# print(('_________________________________'))
# print(('_________________________________'))
# ######################          DICT VS ORDERED DICT
# ######################          DICT VS ORDERED DICT
# ######################          DICT VS ORDERED DICT
# ######################          DICT VS ORDERED DICT
# ######################          DICT VS ORDERED DICT
# d1 = {}
# d1['a'] = 'A'
# d1['b'] = 'B'
# d1['c'] = 'C'
#
# d2 = {}
# d2['b'] = 'B'  # Порядок ввода не важен, словари идентичны (начиная с пайтон 3.7)
# d2['a'] = 'A'
# d2['c'] = 'C'
#
# d3 = {}
# d3['a'] = 'A'
# d3['b'] = 'B'
# d3['c'] = 'C'
#
# print(d1 == d2)
# print(d1 == d3)
#
# for k, v in d1.items():
#     print(k, v)
# for k, v in d2.items():
#     print(k, v)
# for k, v in d3.items():
#     print(k, v)
#
# from collections import OrderedDict
#
# d1 = OrderedDict()
# d1['a'] = 'A'
# d1['b'] = 'B'
# d1['C'] = 'C'
#
# d2 = OrderedDict()  # Пары ключ-значение идентичны, но из за очередности они НЕ РАВНЫ
# d2['b'] = 'B'  # OrderedDict контролирует порядок пар ключ - значение
# d2['a'] = 'A'
# d2['C'] = 'C'
#
# d3 = OrderedDict()
# d3['a'] = 'A'
# d3['b'] = 'B'
# d3['C'] = 'C'
# print(d1 == d2)
# print(d1 == d3)
#
# int_list = [1, 2, 3]
# mixed_list = [1, 2.0, 'string']
# print(type(int_list))
# print(len(int_list))
# print(int_list[0])
# print(int_list[-1])
# print(int_list[0::2])
# names1 = ['John', 'Bob', 'Alice']
# names2 = ['Tracy', 'Elijah', 'Mason']
# names_combined = names1 + names2
# print(names_combined)
# names1[0] = 'Liam'
# print(names1)
# names_combined = names1 + names2
# print(names_combined)
# names1.append('William')
# names1.append('James')
# print(names1)
# popped = names1.pop()
# print(popped)
# print(names1)
# names1.pop(0)
# print(names1)
# names1.append('James')
# names1.sort()  # СОРТИРОВКА
# print(names1)
# letters = ['ac', 'ab', 'aa']
# letters.sort()
# print(letters)
# letters = ['abc', 'a', 'ab']
# letters.sort(key=len)  # сортировка по длинне
# print(letters)
# numbers = [3, 2, 8, 5, 0, 3, 4, 1, 1]
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print("_________________")
# numbers44 = [3, 2, 8, 5, 0, 3, 4, 1, 1]
# print(numbers44)
# numbers44.reverse()
# print(numbers44)
# numbers44.sort(reverse=True)
# print(numbers44)
# print('_______')
# print(numbers)
# numbers.insert(0, 22)
# print(numbers)
# listtest = ['1', '2', '3']
# listtest.append('321')
# print(listtest)
# print(numbers.index(5))  # вписываем значение, которое ищем,
# # получаем индекс
# print(numbers.count(3))  # вписываем значение, которое ищем,
# # получаем количество
# copy = numbers.copy()  # делает бекап списка в переменной,
# # но содержит изменяемый тип данных,
# то
# есть
# он
# может
# поменяться
#
# print(copy)
# numbers.append('1441')
# print(numbers)
# print(copy)
# numbers.clear()
# print(numbers)
# Take
# an
# array and remove
# every
# second
# element.
# Always
# keep
# the
# first
# element and start
# removing
# with the next element.
#
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
#
# None
# of
# the
# arrays
# will
# be
# empty, so
# you
# don
# 't have to worry about that!
#
#
# def remove_every_other(my_list):
#     new_list = my_list[::2]
#     return new_list
#
#
# if True:
#     print('Indeed, true.')
# if 3 > 2:
#     print('3 is greater than 2')
# if 3 < 2:
#     print('2 is less than 2')
#
# is_admin = True
# if is_admin:
#     print('Its admin')
#
# selected_character = input('select your race:  ')
# if selected_character == 'Protos':
#     print('Protos is the most powerful race')
# elif selected_character == 'Zerg':
#     print('Zerg is the most weak race but it spreads like a plague')
# elif selected_character == 'Terrain':
#     print('Terrain is a race balanced between Zerg and Protos')
# else:
#     print('idk what race is it')
# NamedTuple
# даёт
# возможность
# проименовать
# элементы, которые
# он
# сожержит
# NamedTupleCLASS = namedtuple('a', 'b')
# Subtup = [NamedTupleCLASS('a', 'name age etc')
#           players = [('Carlsen', 1990, 2842), ('Caruana, 1992, 2822'), ('Mamedyarov', 1985, 2801)]
# print(type(players))
# print(type(players[0]))
#
# player = namedtuple('player', 'name age elo')
# players = [player('Carlsen', 1990, 2842), player('Caruana', 1992, 2822),
#            player('Mamedyarov', 1985, 2801)]
# print(players[0])
# print(players[1])
# print(players[2])
# for a, b, c in players:
#     print(a, b, c)
# print('_____')
#
# print(players[0])
# print(players[0].name)
# print(players[0].age)
# print(players[0].elo)
#
# тип
# сет
# содержит
# уникальные
# элементы
# my_set = set()  # set() - конструктор
# print(my_set)
# print(type(my_set))
# my_set.add(1)
# print(my_set)
# my_set.add(2)
# print(my_set)
# my_set.add(2)  # вторая двойка не добавляется так как она не уникальна
# print(my_set)
# my_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, ]
# s = set(my_list)
# print(s)
#
# print(len(s))
#
# print(1 in s)
# print(5 in s)
# print('___')
# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))  # что входит.issubset(куда входит)
# print(set2.issuperset(set1))  # куда входит.issuperset(что входит)
#
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.isdisjoint(set2))  # возвращает TRUE если совпадений нет
#
# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3, 4, 5}
# set3 = set1.union(set2)
# print(set3)
#
# set3 = set1.intersection(set2)  # находит одинаковые значения в множествах
# print(set3)
#
# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 2, 3, 4, 5}
#
# set3 = set1.difference(set2)  # показывает чего нет из первого множества во втором
# print(set3)
# set4 = set1.symmetric_difference(
#     set2)  # показывает чего нет из первого во втором и из второго в первом
# print(set4)
#
# set1.update(set2)  # update как union, но он не возвращает новое множество, а модифицирует то
# на
# котором
# вызван
# метод
# update
# print(set1)
#
# .remove.discrad.pop - методы
# удаления
# элементов
# из
# множеств
# set1.remove(1)
# print(set1)
# print(set1.remove(42))  # возникла бы ошибка, так как числа нет в множестве
# set1.discard(2)
# print(set1)
# set1.discard(42)  # ошибки не возникло
# print(set1)
# popped_out_element = set1.pop()
# print(popped_out_element)  # по документации .Pop удаляет СЛУЧАЙНЫЙ ЭЛЕМЕНТ
#
# set1.clear()  # полностью вычищает список
# print(set1)
#
# кортеж, неизменяемый
# список = ('', '', '')
# используется
# для
# защиты
# от
# изменений
# strings = ('str1', 'str2', 'str3')
# strings2 = ['str1', 'str2', 'str3']
# print(strings[0])
# print(type(strings))
# print('___')
# person = ('John', 'Silver', 22)
# print(type(person))
# print(len(person))
# print(person[0])
# print(person[-1])
# print(strings2[-1])
# print(strings2)
# strings2[0] = 'Bob'
# print(strings2)
# print(person.count('John'))
# print(person.index('John'))
#
# x = 0
# while x < 3:
#     print(f'x equals {x}')  # ДО ТЕХ ПОР ПОКА что то остается TRUE
#     x += 1
# else:
#     print('condition is not met')
# print('_________________________________')
#
# vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum = 0
# for v in vals:
#     if v % 2 == 0:
#         continue  # переход в v
#     else:
#         sum += v
#     if sum > 10:
#         break  # прекращает цикл
# print(sum)
#
# for v in vals:
#     pass  # ничего не происходит, не знаю зачем нужно
#
# продвинутая
# тема
# функция
# в
# питоне - полноценный
# объект
#
#
# def hello_world():
#     print('Hello world')
#
#
# hello_world()
#
# hello2 = hello_world  # () = вызов
# print(hello2())
#
#
# def hello_world():
#     def internal():
#         print('Hello world')
#
#     return internal
#
#
# hello2 = hello_world()
#
# print(hello2)
# hello2()
#
# print('________________функция в качестве аргумента принимает другую функцию_________________')
#
#
# def say_something(func):
#     func()
#
#
# def hello_world():
#     print('Hello world')
#
#
# say_something(hello_world)
#
#
# def log_decorator(func):
#     def wrap():
#         print(f'calling func: {func}')
#         func()
#         print(f'func {func} finished, its wkr')
#
#     return wrap
#
#
# def hello():
#     print('hello world')
#
#
# wrappedbylogger = log_decorator(hello)
# wrappedbylogger()
#
#
# @log_decorator
# def hello():
#     print('hello')
#
#
# hello()
#
# print('________________Замер скорости выполнения функций_________________')
#
# from timeit import default_timer as timer
#
#
# def measure_time(func):
#     def inner(*args, **kwargs):
#         start = timer()
#
#         func(*args, **kwargs)
#
#         end = timer()
#
#         print(f'{func.__name__} tool {end - start} for execution')
#
#     return inner
#
#
# @measure_time
# def factorial(num):
#     time.sleep(3)
#     print(math.factorial(num))
#
#
# factorial(10)
#
# numbers = [1, 2, 3]
# numbers.append(4)
# help(numbers.append)  # позволяет получить документацию.
#
# print('________________встроенные функции математические_________________')
#
# print(abs(-1))  # abs берет модуль
# print(max(1, 2, 3, 4, 5))  # берет максимальное значение,
# print(min([1, 2, 3, 4, 5]))  # работает со списками
# print(pow(2, 8))  # возведение в степень, 2**8
# print(round(3.37, 1))  # округление, 1 - значение, 2 - кол-во агрументов после точки
# print(sum([1, 2, 3, 4, 5]))  # суммирует тольк осписки
# h = hex(42)  # вывод в 16-ти ричную систему
# o = oct(42)  # вывод в 8-ми ричный формат (самый редкий)
# b = bin(42)  # вывод в 2-ичную систему (бинарную)
# print(h, o, b)
#
# print('________________встроенные функции с итерируемыми объектами_________________')
#
# all_true1 = all([True, True, True])  # cтановится тру, если все элементы тру
# all_true2 = all([True, False, False])
# print(all_true1, all_true2)
#
# players = [('Carlsen', 2842), ('Caruana', 2822), ('Mamedyarov', 2801), ('Giri', 2780),
#            ('Ding', 2797)]
# print(all(rating > 2800 for _, rating in players))  # all( b > 123 for name, b in (X)
# print(all([rating > 2800 for _, rating in
#            players]))  # all( b > 123 for name, b in (X), медленный вариант
# #  вызова
#
# any  # хотя бы 1 элем должен быть тру для тру, а фолс вернется только если все фолс
# any_true1 = any([True, False, False])
# any_true2 = any([False, False, False])
# print(any_true1, any_true2)
#
# players = [('Carlsen', 2842), ('Caruana', 2822), ('Mamedyarov', 2801), ('Giri', 2780),
#            ('Ding', 2797)]
# print(any([rating < 2790 for _, rating in players]))
# print(any([rating < 2700 for _, rating in players]))
#
# letters = 'abcd'
# numbers = (10, 20, 30)  # tuple
# zipped = zip(letters, numbers
#              )
# print(zipped)
# print(type(zipped))
# zipped_list = list(zipped)  # срабатывает только после конструктора лист
# print(zipped_list)  # излишние элементы будут отсечены
#
# names = ['Carlsen', 'Caruana', 'mamedyarov', "Ding", "Giri"]
# ratings = [2842, 2822, 2801, 2797, 2780]
# players = dict(zip(names, ratings))  # зип со словарём
# print(players)
#
# code = ord('a')  # конверт в юникод для работы на низком уровне
# print(code)
# c = chr(97)  # конверт из юникода для работы на низком уровне
# print(c)
#
# greeting = 'Hello from the global scope'  # вне классов
#
#
# def greet():
#     greeting = "Hello from enclosing scope"  # считается такой, только в ней еще одна вложенная функция
#
#     def nested():
#         greeting = "Hello from local scope"
#         print(greeting)
#
#     nested()
#
#
# greet()
# print(greeting)
# print('_________________________________')
#
# greeting = 'global'
#
#
# def greet(greeting):
#     print(f'greet in funk {greeting}')
#
#     greeting = 'hELLO FROM ENCLOSING SCOPE'
#
#     print(f'greet in func:{greeting}')
#
#     def nested():
#         greeting = "local"
#         print(greeting)
#
#     nested()
#
#
# greet('test')
# print(greeting)
#
# print(
#     '________________global greeting_________________')  # начиная с этог места = работа с переменной
# из
# глобального
# цикла
#
# greeting = 'global'
#
#
# def greet():
#     global greeting
#     print(f'greet in funk {greeting}')
#
#     greeting = 'hELLO FROM ENCLOSING SCOPE'
#
#     print(f'greet in func:{greeting}')
#
#     def nested():
#         greeting = "local"
#         print(greeting)
#
#     nested()
#
#
# greet()
# print(greeting)
#
#
# def greeting():  # def Название():
#     '''
#     DOCSTRING: info about the function
#     INPUT: no input...
#     OUTPUT: Hello!
#     '''
#     print('HellO!')
#
#
# greeting()
# help(greeting)
#
#
# def print_name(a):
#     print(a)
#
#
# print_name('Baga')
#
#
# def print_name(name):
#     print(name)
#
#
# print_name(123)
#
# print('_________________________________')
#
#
# def print_name(name='Default'):  # в случае если ничего не передаем то значение будет по умолчанию
#     print(name)
#
#
# print_name(123)
#
# print('_________________________________')
# result = print_name()
# print(result)
# print(type(result))
#
# print('_________________________________')
#
#
# def get_greeting(name):
#     return 'Hello ' + name
#
#
# greeting = get_greeting('Baga')
#
# print(greeting)
#
# print('_________________________________')
#
#
# def get_sum(a, b):
#     return a + b
#
#
# result = get_sum(10, 2)
# print(result)
#
# print('_________________________________')
#
#
# def is_adult(age):
#     return age >= 18
#
#
# is_adult = is_adult(20)
# print(is_adult)
#
# print('_________________________________')
#
#
# def is_palindrom(text):
#     return text == text[::-1]
#
#
# print(is_palindrom('aabaa'))
# print(is_palindrom('aaba2a'))
#
# print('_________________________________')
#
#
# def calc_taxes(p1, p2, p3):
#     return sum((p1, p2, p3)) * 0.06
#
#
# print(calc_taxes(10, 20, 30))
#
# print('_________________________________')
#
#
# def calc_taxes(p1, p2, p3):
#     print(sum((p1, p2, p3)) * 0.06)
#
#
# calc_taxes(10, 20, 30)
#
# print('_________________________________')
#
#
# def calc_taxes(p1, p2, p3):
#     return sum((p1, p2, p3)) * 0.06
#
#
# print(calc_taxes(10, 20, 30))
#
# print('_________________________________')  ############### бесконечное кол-во аргументов
#
#
# def calc_taxes(*args):
#     for x in args:
#         print(f'Got payment = {x}')
#     return sum(args) * 0.06
#
#
# print(calc_taxes(10, 20, 30, 40))
#
#
# def save_players(**kwargs):  # значит что сюда передаются N пар ключ: значение
#     for k, v in kwargs.items():
#         print(f'player {k} has ratio {v}')
#
#
# save_players(carlsen=2800, giri=2780)
#
#
# def func_importan(a, b, c, d, *args, *kwargs)  # позиционные элементы,
#
#
# # затем аргс (болшое кол-во аргументов)
# # а затем кваргс (клю: значение), большая редкость
# трансформация
# последовательности
# в
# другую
#
#
# def square(*args):
#     return [x * x for x in args]
#
#
# print(square(1, 2, 3, 4, 5))
#
#
# def triple(*args):
#     return [x * 3 for x in args]
#
#
# print(triple(1, 2, 3, 4, 5))
#
# print('________________map function_________________')  # проходится по двум функциям
#
#
# def square(number):
#     return number * number
#
#
# numbers = [1, 2, 3, 4, 5]
#
# result = map(square, numbers)
# print(result)
#
# for i in result:
#     print(i)
#
# print(type(result))
#
# print(list(map(square, numbers)))
#
#
# def is_adult(age):
#     return age >= 18
#
#
# ages = [14, 18, 21, 16, 30]
#
# adult_result = filter(is_adult, ages)  # фильтр возвращает объект, в него передаётся фильтр,
# # который возвращает тру или фалс, если фалс - он исключается
# # из последовательности и результатат
#
# print(adult_result)
# print(list(filter(is_adult, ages)))
#
# print(('________________lambda expressions________лямбда выражения_________'))
#
# is_adult = lambda age: age >= 18
# print(list(filter(is_adult, ages)))
#
# multiplier = lambda x, y: x * y
# print(multiplier(2, 3))
#
# x = ('Hello, my name is Elias')
# len(x)
# x[len(x) - 1]
# x.count('l')
# capitalized_text = x.capitalize()
# print(capitalized_text)
# upper_cased = x.upper()
# print(upper_cased)
# lower_cased = x.lower()
# print(lower_cased)
# print(upper_cased.isupper())
# print(lower_cased.islower())
# print(x.islower())
# print('__________________________')
# print(x.find('m', 4, 15))
# print('__________________________')
# print(x.find('my'))
# print('__________________________')
# print('123abc'.isalnum())
# print('123abc!'.isalnum())
# print('__________________________')
#
# print('abc'.isalpha())
# print('123abc'.isalpha())
# print('__________________________')
# print('   '.isspace())
# print(''.isspace())
# print('1'.isspace())
# empty_string = ''
# print('__________________________')
# print(empty_string.strip(' ') == '')
#
# if not empty_string == '':
#     print('not empty')
# else:
#     print('empty')
# print('__________________________')
# print('__________________________')
# print('__________________________')
# h = 'hello'
# print(h.startswith('he'))
# print(h.endswith('lo'))
# print('__________________________')
# print('__________________________')
# split = h.split('l')
# print(type(split))
# print(split)
# split = h.split('e')
# print(split)
# print('__________________________')
# print('__________________________')
# data = '12;10;8;10'
# split_data = data.split(';')
# print(type(split_data))
# print(split_data)
# print('__________________________')
# print('__________________________')
# data = '12;10;8;10'
# data = data.partition(';')
# print(type(data))
# print(data)
#
#
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as ex:
#         print(f'an error occurred: {ex}')
#     except:
#         print(f'unknown error occurred')
#
#
# divider = int(input('input divider: '))  # str test
# print(divide(100, divider))
#
#
# class invalidtriangeerror(Exception):
#     """Raised when a triangle has invalid sides"""
#
#
# def calc_square(ab, ac, bc):
#     if ab <= 0 or ac <= 0 or bc <= 0:
#         raise invalidtriangeerror(f" One of the sides is less or equal to zero")  # RAISE
#     p = (ab + ac + bc) / 2
#     s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
#     return s
#
#
# square = calc_square(10, 10, 10)
# try:
#     square = calc_square(10, 10, 10)
#     print(square)
# except invalidtriangeerror as ex:
#     print(ex)
# else:
#     print(square)
#
#
# class invalidtriangeerror(Exception):
#     """Raised when a triangle has invalid sides"""
#
#
# file = None
# try:
#     file = open(r'C:\notexist\something.txt')
#     data = file.read()
# except FileNotFoundError as ex:
#     print(f'error has occurred. description: {ex.strerror}')
# else:
#     print('maybe else')
# finally:
#     print('finally1')
#     if file:
#         file.close()
#         print('finally2')  #
#
# print('doing some work here ')  # test
#
#
# def get_int():
#     while True:
#         try:
#             reply = int(input('enter int here: '))
#             return reply
#         except:
#             print(f'we need INT you dumbass')
#             continue
#
#
# number = get_int()
#
# print('_________________________________')
# print(number)
#
#
# def get_reply(number):  # fizzbuzz
#     if number % 5 == 0 and number % 3 == 0:
#         print('Fizzbuzz')
#         return 'Fizzbuzz'
#     elif number % 5 == 0:
#         print('Buzz')
#         return 'Buzz'
#     elif number % 3 == 0:
#         print('Fizz')
#         return 'Fizz'
#     else:
#         print('')
#
#
# import unittest
# import fizz_buzz
#
#
# class fizzbuzztest(unittest.TestCase):
#
#     def test_fizz(self):
#         number = 6
#         result = fizz_buzz.get_reply(number)
#
#         self.assertEqual(result, 'Fizz')
#
#     def test_buzz(self):
#         number = 10
#         result = fizz_buzz.get_reply(number)
#
#         self.assertEqual(result, 'Buzz')
#
#     def test_fizz(self):
#         number = 15
#         result = fizz_buzz.get_reply(number)
#
#         self.assertEqual(result, 'Fizzbuzz')
#
#
# if __name__ == '__main__':
#     unittest.main()
# from PIL import Image
#
# with Image.open(
#         r"C:\Users\BS_HOME\PycharmProjects\pythonProject_test_curse\__main__\lessons\6. OOP\python-classes.jpg") as im:
#     im.rotate(0).show()
#
# oop
#
#
# class Character():  # pascal casing rule
#
#     def __init__(self, race, damage=10,
#                  armor=20):  # определение конструктора, все атрибуты записываются через ссылку селф
#         self.race = race
#         self.damage = damage
#         self.armor = armor
#
#
# unit = Character('Elf', damage=20, armor=40)  #
# print(type(unit))
#
# print(unit.race, unit.damage, unit.armor)
#
#
# class Character():
#     max_speed = 1000  # можно обращаться без создания экземпляра
#     max_health = 100
#     death_health = 0
#
#     def __init__(self, race, dmg=10, armor=20):  # методы
#         self.race = race  # атрибуты
#         self.dmg = dmg
#         self.armor = armor
#         self.health = 100
#         # нельзя обращаться без создания экземпляра (инстанция)
#
#     def hit(self, damage):
#         self.health -= damage
#
#     def is_dead(self):
#         return self.health <= Character.death_health
#
#
# unit = Character('Orc')
#
# print(unit.race, unit.dmg, unit.armor)
# print(unit.max_speed)
#
# unit.hit(20)
# print(unit.health)
# print(unit.is_dead())
# unit.hit(80)
# print(unit.is_dead())
#
# unit.health = -200
# print(unit.is_dead())
#
# print(unit.health)
#
#
# class Character():
#     MAX_SPEED = 100  # costant atribute CAPS
#
#     def __init__(self, race, damage=10):
#         self.damage = damage
#         self.__race = race  # private __n                  # то что не меняется, приватный
#         self._health = 100  # inheritance visible _n       # то что меняется редко, защищенный
#         self.current_speed = 20
#
#     def hit(self, damage):
#         self._healt -= damage
#
#     @property  # декоратор свойства для чтения
#     def health(self):
#         return self._health
#
#     @property  # декоратор свойства для чтения
#     def race(self):
#         return self.__race
#
#     @property
#     def current_speed(self):
#         return self._current_speed
#
#     @current_speed.setter
#     def current_speed(self, current_speed):
#         if current_speed < 0:
#             self._current_speed = 0
#         elif current_speed > 100:
#             self._current_speed = 100
#         else:
#             self._current_speed = current_speed
#
#
# print(Character.MAX_SPEED)
# Character.MAX_SPEED = 10  # this constant can change
# print(Character.MAX_SPEED)
#
# c = Character('Elf', 20)
# print(c._Character__race)
# c._Character__race = 'Orc'
# print(c._Character__race)
#
# c._health = 0
# print(c._health)
# print('___')
# print(c.health)
# print(c.race)
#
# print(c.current_speed)
# c.current_speed = 120
# print(c.current_speed)
#
# c.current_speed = -123
# print(c.current_speed)
#
#
# class StaticTest():
#     x = 1  # class
#     # def __init__(self,):
#
#
# t1 = StaticTest()
# print(f'via instance: {t1.x}')
# print(f'via class: {StaticTest.x}')
# print('________________read and write_________________')
# t1.x = 2  # instance
# print(f'via instance: {t1.x}')
# print(f'via class: {StaticTest.x}')
#
# StaticTest.x = 3
#
# print(f'via instance: {t1.x}')
# print(f'via class: {StaticTest.x}')  # its dif atributes
#
# print('___static methods creation example___')  # when no atributes, just method collection
#
#
# class Date():
#     def __init__(self, month, day, year):
#         self.month = month
#         self.day = day
#         self.year = year
#
#     def display(self):  # instance
#         return f'{self.month} - {self.day} - {self.year}'
#
#     @classmethod
#     def millenium_classmethod(cls, month, day):  # self is instantion and cls is info about class
#         return cls(month, day, 2000)
#
#     @staticmethod
#     def millenium_staticmethod(month, day):  # self is instantion and cls is info about class
#         return Date(month, day, 2000)
#
#
# date1 = Date.millenium_classmethod(6, 9)
# date2 = Date.millenium_staticmethod(6, 9)
#
# print(date1.display())
# print(date2.display())
#
#
# class DateTime(Date):
#     def display(self):
#         return f'{self.month} - {self.day} - {self.year} - 00:00:00 PM'
#
#
# dt1 = DateTime(10, 10, 1990)
# dt2 = DateTime.millenium_staticmethod(10, 10)
#
# print(isinstance(dt1, DateTime))
# print(isinstance(dt2, DateTime))
#
# print('________________display_________________')
# print(dt1.display())
# print(dt2.display())
#
# классметод
# содержит
# информацию
# о
# классе, поэтому
# конструируется
# именно
# он
# статикметод
# абстрагирован
# от
# класса
#
#
# class StrConverter():
#
#     @staticmethod
#     def to_str(bytes_or_str):
#         if isinstance(bytes_or_str, bytes):
#             value = bytes_or_str.decode('utf-8')
#
#         else:
#             value = bytes_or_str
#         return value
#
#     @staticmethod
#     def to_bytes(bytes_or_str):
#         if isinstance(bytes_or_str, str):
#             value = bytes_or_str.encode('utf-8')
#
#         else:
#             value = bytes_or_str
#         return value
#
#
# print(StrConverter.to_str('\x41'))
# print(StrConverter.to_str('A'))
#
# print(StrConverter.to_bytes('\x41'))
# print(StrConverter.to_bytes('A'))
#
#
# class Shape():
#
#     def __init__(self):
#         print('Shape created.')
#
#     def draw(self):
#         print('Drawing shape')
#
#     def area(self):
#         print('Calc area')
#
#     def perimeter(self):
#         print('Calculating perimeter')
#
#
# class Rectangle(Shape):  # наследник Shape, мы имеет доступ к атрибутам класса Shape
#     def __init__(self, width,
#                  height):  # так же можем переопределять реализацию родительских методов
#         Shape.__init__(self)
#         self.width = width
#         self.height = height
#
#         print('Rectangle created.')
#         Shape.area(self)
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def draw(self):
#         print('Drawing rectangle with weight and height')
#
#
# rect = Rectangle(10, 15)
#
# print(rect.area())
# print(rect.perimeter())
# rect.draw()
#
#
# class Triangle(Shape):
#
#     def __init__(self, a, b, c):
#         Shape.__init__(self)
#
#         self.a = a
#         self.b = b
#         self.c = c
#
#         print('Triangle created')
#
#     def draw(self):
#         print(f'Drawing triangle with sides: {self.a},{self.b},{self.c}')
#
#     def area(self):
#         s = (self.a + self.b + self.c) / 2
#         are = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
#         print(are)
#
#     def perimeter(self):
#         periansw = self.a + self.b + self.c
#         print(periansw)
#
#
# print('---------')
# tritest = Triangle(10, 10, 10)
# tritest.draw()
# tritest.area()
# tritest.perimeter()
#
# for shape in [rect, tritest]:
#     shape.draw()
#
# если
# 2
# класса
# имеют
# методы
# с
# одинаковыми
# названиями, то
# можно
# использовать
# концепцию
# полиморфизма
# when
# lil
#
#
# class have more then 1 giga class
#
#
# class Animal():
#     def die(self):
#         print('bye ;(')
#         self.health = 0
#
#
# class Carnivour():
#     def hunt(self):
#         print('eating')
#         self.satiety = 100
#
#
# class Dog(Animal, Carnivour):
#     def bark(self):
#         print('woof-woof')
#
#
# dogo = Dog()
# dogo.bark()
# dogo.hunt()
# dogo.die()
#
# print('_________________________________')
#
#
# class Animal:  # deadly diamond of death example
#     def set_health(self, health):
#         print('set in animal')
#
#
# class Carnivour(Animal):
#     def set_health(self, health):
#         print('set in carnivour')
#
#
# class Mammal(Animal):
#     def set_health(self, health):
#         print('set in mammal')
#
#
# class Dog(Carnivour, Mammal):  # НАСЛЕДУЕТ ПЕРВОЕ в случае, если у предка одинаковые методы
#     pass
#
#
# print('_________________________________')
#
# print('_________________________________')
#
# dogo = Dog()
# dogo.set_health(10)
#
#
# class Animal:  # deadly diamond of death example
#     def set_health(self, health):
#         print('set in animal')
#
#
# class Carnivour(Animal):
#     def set_health(self, health):
#         print('set in carnivour')
#
#
# class Mammal(Animal):
#     def set_health(self, health):
#         print('set in mammal')
#
#
# class Dog(Carnivour, Mammal):  # НАСЛЕДУЕТ ПЕРВОЕ в случае, если у предка одинаковые методы
#     def set_health(self, health):
#         Mammal.set_health(self, health)
#         Carnivour.set_health(self, health)
#         Animal.set_health(self, health)
#
#
# dogo = Dog()
# dogo.set_health(10)
#
# print('_________________________________')
#
# print('_________________________________')
#
#
# class Animal:  # deadly diamond of death example
#     def set_health(self, health):
#         print('set in animal')
#
#
# class Carnivour(Animal):
#     def set_health(self, health):
#         super().set_health(health)
#         # Animal.set_health(self, health)
#         print('set in carnivour')
#
#
# class Mammal(Animal):
#     def set_health(self, health):
#         super().set_health(health)
#         # Animal.set_health(self, health)
#         print('set in mammal')
#
#
# class Dog(Carnivour, Mammal):  # НАСЛЕДУЕТ ПЕРВОЕ в случае, если у предка одинаковые методы
#     def set_health(self, health):
#         super().set_health(
#             health)  # ГАРАНТИЯ ПОСЛЕДОВАТЕЛЬНОСТИ снизу вверх(глубина), слева направо
#         # Mammal.set_health(self, health)
#         # Carnivour.set_health(self, health)
#         print('set in dog')
#
#
# dogo = Dog()
# dogo.set_health(10)
#
#
#
# print('_________________________________')
#
# print('_________________________________')
#
#
# class Animal():
#     def __init__(self):
#         self.health = 100
#
#     def hit(self, damage):
#         self.health -= damage
#
#
# class Carnivour(Animal):
#     def __init__(self):
#         super().__init__()
#         self.legs = 4
#
#
# c = Carnivour()
# c.hit(10)
#
# print(c.health)
#
# для
# запрещения
# вызова
# метод
# raise
#
# from abc import ABC
# from abc import abstractmethod
#
#
# class Shape(ABC):
#     def __init__(self):
#         super().__init__()
#
#     @abstractmethod  # объявление абстрактным
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         print('calc perimeter')
#         # pass
#
#     def drag(self):
#         print('basic dragging functionality')
#
#
# class Triangle(Shape):  # Наследует абстрактный класс
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def draw(self):
#         print(f"drawing triangle with sides = {self.a}, {self.b}, {self.c}")
#
#     def area(self):
#         s = (self.a + self.b + self.c) / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def drag(self):
#         super().drag()
#         print('Additional action')
#
#
# t = Triangle(10, 10, 10)
# print(t.perimeter())
# t.drag()
#
#
#
# class Point():
#     def __init__(self, x, y):  # init конструктор класса
#         self.x = x
#         self.y = y
#
#     def __str__(self):  # строковое представление экземпляра класса
#         return (f'point x = {self.x} and y = {self.y}')
#
#
# p = Point(3, 4)
# print(p)
#
#
# class Road():
#     def __init__(self, len):
#         self.len = len
#
#     def __len__(self):
#         return self.len
#
#     def __str__(self):
#         return (f'a road len : {len(self)}')
#
#     def __del__(self):
#         print(f'The road has been destroyed')
#
#
# r = Road(100)
# print(len(r))
#
# print(r)
#
#
# player_1 = 0
# player_2 = 0
# sticks = 10
# looser = ''
# print(type(sticks))
# print(f'Перед вами 10 палочек, каждый игрок по '
#       f'очереди тянет от 1 до 3-х палок, кто берет последним'
#       f' - тот проиграл')
#
# while sticks > 0:
#     print('_____________________________________________')
#     print(f'Палочек перед вами: {sticks} ')
#     player_1 = int(input(f'Сколько палочек тянет Игрок_1?:  '))
#     sticks -= player_1
#     looser = 'Игрок_1'
#     if sticks < 2 or sticks == 0:
#         print('_____________________________________________')
#         print(f'Игра окончена, {looser} проиграл')
#     print('_____________________________________________')
#     print(f'Палочек перед вами: {sticks} ')
#     player_1 = int(input(f'Сколько палочек тянет Игрок_2?:  '))
#     looser = 'Игрок_2'
#     if sticks < 2 or sticks == 0:
#         print('_____________________________________________')
#         print(f'Игра окончена, {looser} проиграл')
#         break
#     if player_1 > 3:
#         print('_____________________________________________')
#         print('Нельзя вытягивать более 3-х палочек')
#         print('_____________________________________________')
#         break
#     sticks -= player_1
#     if sticks < 2 or sticks == 0:
#         print('_____________________________________________')
#         print(f'Игра окончена, {looser} проиграл')
#         break
#     print(f'Игрок_1 вытянул {player_1} палочек')
#
#
# def bubbleSort(theSeq):
#     n = len(theSeq)
#
#     for i in range(n - 1):
#         flag = 0
#
#         for j in range(n - 1):
#
#             if theSeq[j] > theSeq[j + 1]:
#                 print(theSeq)
#                 tmp = theSeq[j]
#                 theSeq[j] = theSeq[j + 1]
#                 theSeq[j + 1] = tmp
#                 flag = 1
#
#         if flag == 0:
#             print(theSeq)
#             break
#
#     return theSeq
#
#
# el = [21, 6, 9, 33, 3]
#
# result = bubbleSort(el)
#
# print(result)
# калькулятор
# цельсий
# в
# форенгейт
# и
# обратно
# a = input('Исходное измерение Ц = c ; Ф = f :  ')
# b = int(input('Какая температура:  '))
# c = float(0)
# for i in (a):
#     if i == 'c':
#         c = (b) * (9 / 5) + 32
#         print(c)
#         break
#     elif i == 'f':
#         c = (b - 32) * (5 / 9)
#         print(c)
#         break
#
# x = 'asd'
# print('x: ', x)
# type_x = type(x)
# print('type_x:', type_x)
# print('is x a string: ', isinstance(x, str))
#
# x = 10 - 5
# print(x)
#
# x = 10
# print(type(x))
# x = x - 0.1
# print(type(x))
#
# name = 'bob'
# age = 25
# age = age + 1
# message = name + " is " + str(age)
# print(message)
# name = 'aboba'
# message2 = f'{name} is {age + 1}'
# print(message2)
# message3 = "{name} is {age}".format(name=name, age=age)
# print(message3)
# w  #
# long_text = f"""this is
# another text {message2}"""
#
# print(long_text)
#
# a = "Hello"
# b = "world"
# write
# your
# code
# below
# this
# line
#
# result_string = "{a}, {b}!".format(a=a, b=b)
# print(result_string)
#
#
# def print_rectangle_info(a, b):
#     perimeter = (a + b) * 2
#     square = a * b
#     print(perimeter)
#     print(square)
#
#
# print_rectangle_info(3, 10)
# print_rectangle_info(6, 9)
#
#
# def is_adult(age: int) -> bool:
#     return print(age >= 18)
#
#
# is_adult(15)
# is_adult(32)
#
#
# def get_rectangle_square(a, b):
#     square = a * b
#     return square
#
#
# print(get_rectangle_square(3, 4))
#
#
# def double(num: int) -> int:
#     return num * 2
#
#
# print(double(2))
#
#
# def kekload():
#     counter = 100
#     progress_percent = 0
#     while counter > 0:
#         l = []
#         l.append('|')
#         s = ''.join(l)
#         print(f"""{s}
# {progress_percent}%""")
#         counter -= 1
#         progress_percent += 1
#
#
# kekload()
# a = 1.32 + 0.68
# b = 2
# print(a)
# print(type(a))
# print(type(b))
# print(b)
# print(a == b)
# print('type_check')
# print(type(a) == type(b))
#
# my_age = 0
#
# for _ in range(5):
#     my_age += 1
#     print('asd')
#
#
# def get_drinks(number_of_guests: int) -> int:
#     result = 0
#
#     for i in range(number_of_guests + 1):
#         result += i
#
#     return result
#
#
# print(get_drinks(3))
#
#
# def get_drinks_with_step(number_of_guests: int, step: int) -> int:
#     counter = 0
#     for i in range(1, number_of_guests + 1, step):
#         counter += i
#     return counter
#
#
# from typing import Union
#
#
# def calculate_profit(amount: int, percent: Union[float, int], period: int) -> int:
#     result = 0
#     start = amount
#     print(amount)
#     for i in range(period):
#         print(amount)
#         amount = amount + (amount / 100 * percent)
#         result += amount
#         print(amount)
#     result = result - start
#     print(result)
#     if amount or percent or period == 0:
#         return 0
#     else:
#         print(result)
#
#
# calculate_profit(1000, 10, 10)
#
# profit = 1000
#
# profit *= 1 + 5 / 100
# print(profit)
#
# word = 'hello world'
# for i in range(len(word) - 1, -1, - 1):
#     print(word[i])
#
# word = "hello world"
# for i in range(len(word) - 1, -1):
#     print(word[i])
# word = 'hello world'
# for char in word:
#
# for i in word:
#     print(i)
#     print(char)
#
# word = "hello world"
#
# for i, x in enumerate(word):
#     print(x, i)
#
# x = 'abcdebc'
# y = 'bc'
#
# print(y in x,
#       x.index(y),  # left index
#       x.rindex(y),  # right index
#       )
#
# print(y in x,
#       x.find(y, 3, 5),  # if y not in x return -1  # ? start stop
#       x.rfind(y))  # if y not in x return -1
# #   x.startswith(y),  # if x start with y -> bool
# # x.endswith(y)) # if x ends with y
#
#
# message = "Hello, Dania!"
# message = message.upper()
# print(message)
# upper_message = message.upper()
# message = message.upper()
# print(upper_message)
# lower_message = message.lower()
# print(lower_message)
# capitalized_message = message.capitalize()
# print(capitalized_message)
#
# model = "Apple iPhone 13"
#
#
# def find_model(search_text):
#     condition = search_text.lower() in model.lower()
#     if condition:
#         print('found')
#
#
# while True:
#     search = input(str('searched: '))
#     find_model(search)
#
# message = '01234567890'
# sl = slice(1, 5)
# print(message[sl])
#
#
# def remove_vowels(document: str) -> str:
#     golosni = "aeiouy"
#     result = ""
#     for i in document.lower():
#         if i in golosni:
#             print(f'ALARM: Document contain "{i}" from forbiden list')
#         else:
#             print(f'{i} - OK')
#             result += i
#     print(result)
#     return result
#
#
# remove_vowels('aeiouyqwrtp')
#
#
# def make_abbr(words: str) -> str:
#     result = ""
#     space_d = " "
#     result += words[0]
#     slice_magic = slice(1)
#     if space_d in words:
#         print('____________________________________________________space found')
#         for i in words:
#             print(i)
#             if i == " ":
#                 print(words.index(space_d))
#                 slice_magic = slice(i)
#                 print(slice_magic)
#
#     print('_________________________________________________________________')
#     print(f'"{words}" converted to "{result.upper()}"')
#
#
# make_abbr('national aeronautics space administration')
#
# my_string = '01234 6789 11 13'
# lf = ' '
# x =
# sl = slice(0, x)
# print(my_string[sl])
#
#
# def make_abbr(words: str) -> str:
#     result = ""
#     result += words[0]
#     while True:
#         for i in words:
#             print(i)
#             if i == " ":
#                 print('CUT HERE______________________')
#                 nextelement = words.index(i) + 1
#                 print(f'{nextelement} IS THIS')
#                 result += words[nextelement]
#
#         return result.upper()
#
#
# print(make_abbr('national aeronautics space administration'))
#
#
# def make_abbr(words: str) -> str:
#     result = ""
#     result += words[0]
#     for i in words:
#         thiselem = i
#         print(thiselem)
#         nextelem = words[words.index(i) + 1]
#         print(nextelem)
#         if i == " ":
#             result += nextelem
#
#     return result.upper()
#
#
# print(make_abbr('national aeronautics'))
#
#
# def make_abbr(words: str) -> str:
#     result = ""
#     result += words[0]
#     x = 0  # for index adding
#     for i in range(len(words)):
#         print(f"{(i)} is {words[i]}")  # (i) - index      ; words[i] - value
#         if words[i] == " ":
#             x = (i)
#             result += words[x + 1]
#     print(f"{words} converted to {result.upper()}")
#     return result.upper()
#
#
# print(make_abbr("national aeronautics space administration"))
#
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# def make_abbr(words: str) -> str:
#     if words == "":
#         return ""
#     else:
#         result = ""
#         result += words[0]
#         for i in range(len(words)):
#             if words[i] == " ":
#                 result += words[(i) + 1]
#     return result.upper()
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# def is_werewolf(target: str) -> bool:
#     target = target.lower()
#     check_here = ''
#
#     for i in target:
#         if i == " " or i == "," or i == ":" or i == ";" or i == "?" or i == "!":
#             None
#         else:
#             check_here += i
#     print("_____________________________________________________")
#     print(f"-> {target} - > {check_here} - > {check_here[::-1]}")
#     print("_____________________________________________________")
#     if check_here.upper() == check_here[::-1].upper() \
#             and \
#             check_here.lower() == check_here[::-1].lower():
#         return True
#     else:
#         return False
#
#
# print(is_werewolf("rotator"))
# print(is_werewolf("home"))
# print(is_werewolf("racecar"))
# print(is_werewolf("red rum sir is murder"))
# print(is_werewolf("eva, can I see bees in a cave"))
#
#
# def happy_birthday() -> None:
#     name = input(f"What's your name?")
#     print(f"Happy birthday, {name}!")
#     return f"Happy birthday, {name}!"
#
#
# print(happy_birthday())
#
#
# def parity_checker() -> None:
#     number = int(input(f"What number do you want to check?"))
#     if number % 2 > 0:
#         print("Odd")
#     if number % 2 == 0:
#         print("Even")
#
#
# parity_checker()
#
#
# def get_success_rate(statistics: str) -> int:
#     if len(statistics) == 0:
#         return 0
#     fail = 0
#     success = 0
#
#     for i in statistics:
#         if i == "0":
#             fail += 1
#
#     success = len(statistics) - fail
#     if success == 0:
#         return 0
#     else:
#         return round((len(statistics) - fail) / (len(statistics) / 100))
#
#
# print(get_success_rate("1010101010"))  # 50% 5 -1 5 -0
#
#
# def check_fermat(a, b, c, n):
#     if n > 2 and (a ** n + b ** n == c ** n):
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn’t work.")
#
#
# def check_numbers():
#     a = int(input("Choose a number for a: "))
#     b = int(input("Choose a number for b: "))
#     c = int(input("Choose a number for c: "))
#     n = int(input("Choose a number for n: "))
#     return check_fermat(a, b, c, n)
#
#
# check_numbers()
#
# from random import Random
# from math import ldexp
#
#
# class FullRandom(Random):
#
#     def random(self):
#         mantissa = 0x10_0000_0000_0000 | self.getrandbits(52)
#         exponent = -53
#         x = 0
#         while not x:
#             x = self.getrandbits(32)
#             exponent += x.bit_length() - 32
#         return ldexp(mantissa, exponent)
#
#
# fr = FullRandom()
# print(fr.random())
#
# fr.random()
# ###############LISTS#####################
# numbers = [10, True, "guga", 11, 12, 13]
#
# print(numbers)
#
# print(numbers[0])
# print(len(numbers))
#
# for index in range(len(numbers)):
#     print(numbers[index])
#
# for num in numbers:
#     print(num)
#
# print("_" * 10)
# x = 456
# numbers[0] = 45
#
# numbers.append(100)
# for num in numbers:
#     print(num)
# numbers[0] = x
# numbers.append(100)
# for num in numbers:
#     print(num)
#
# numbers.insert(3, 1000)  # index, value
#
# for num in numbers:
#     print(num)
#
# numbers[-1] = 15  # last elem
#
# print(numbers)
# y = "afdfgjkldhfg aslkdf asldjfasf"
# xt = list(y)
# print(xt)
#
#
# def make_stickers(details_count: int, robot_part: str) -> list:
#     if details_count == 0:
#         return []
#     result = []
#     print(result)
#
#     details_numbers = list(range(1, details_count + 1))
#     print(details_numbers)
#
#     for i in range(1, details_count + 1):
#         print(i)
#         temporary = f"{robot_part} detail #{i}"
#         print(temporary)
#         result.append(temporary)
#     print(result)
#     return result
#
#
# make_stickers(3, "Body")
#
# x_direction = '_|' * 10
# for i in x_direction:
#     print('q')
# print(x_direction)
#
# ___________________________________________________________________________________
#
#
# def double_power(current_powers: list) -> list:
#     result = []
#     for i in current_powers:
#         result.append(i * 2)
#     return result
#
#
# def is_sorted(box_numbers: list) -> bool:
#     new_list = []
#     for i in box_numbers:
#         new_list.append(i)
#     new_list.sort()
#     if box_numbers == new_list:
#         return True
#     else:
#         return False
#
#
# print(is_sorted([1, 2, 3, 4, 5]))
#
# is_sorted([1, 2, 3, 4, 5]) is True
# is_sorted([0, 1, 1, 1, 2]) is True
# is_sorted([1, 5, 7]) is True
# is_sorted([1, 2, 11]) is True
# is_sorted([5]) is True
# is_sorted([]) is True
# is_sorted([0, 3, 1, 2, 2, 2]) is False
# is_sorted([1, 11, 2]) is False
# is_sorted([5, 3]) is False
#
#
# def get_location(coordinates: list, commands: list) -> list:
#     for i in commands:
#         result = coordinates
#         if i == "forward":
#             coordinates[1] += 1
#         elif i == "back":
#             coordinates[1] -= 1
#         elif i == "right":
#             coordinates[0] += 1
#         else:
#             coordinates[0] -= 1
#         print(f"result {coordinates}")
#     return coordinates
#
#
# print(get_location([0, 5], ["back", "back", "back", "right", "left", "forward"]))
#
#
# def get_plan(current_production: int, month: int, percent: int) -> list:
#     result = []
#     for i in range(1, month + 1):
#         current_production = int(math.floor(current_production))
#         current_production = int(round(current_production))
#         current_production *= (1 + (percent / 100))
#         result.append(int(current_production))
#     return result
#
#
# print(get_plan(1000, 6, 35))  # [1350, 1822, 2459, 3319, 4480, 6048]
#
#
# def get_speed_statistic(test_results: list) -> list:
#     if len(test_results) < 1:
#         return [0, 0, 0]
#     if len(test_results) == 1:
#         return [test_results[0]] * 3
#     result = []
#     avg_counter = 0
#     print(f"inc looks like this: {test_results}")
#     test_results.sort()
#     print(f"result after sort: {test_results}")
#     result.append(test_results[0])
#     result.append(test_results[-1])
#
#     for i in test_results:
#         avg_counter += i
#
#     print(f"avg counter = {avg_counter}")
#     avg_counter = (avg_counter / len(test_results))
#     result.append(int(avg_counter))
#     print(f"min: {result[0]}")
#     print(f"max: {result[-1]}")
#     print(f"avg = {avg_counter}")
#     print(f"result looks like this: {result}")
#     print('_' * 10)
#
#     return result
#
#
# print(get_speed_statistic([10, 10, 11, 9, 12, 8]))  # [8, 12, 10]
# print(get_speed_statistic([10]))  # [10, 10, 10]
# print(get_speed_statistic([]))  # [0, 0, 0]
# print(get_speed_statistic([8, 9, 9, 9]))  # == [8, 9, 8]
# print(get_speed_statistic([5]))  # == [5, 5, 5]
#
# _________________________________________________________________________________________
#
#
# def split_string(string: str) -> list:
#     if len(string) == 1:
#         return [string[0] + "_"]
#     result = []
#     temporary_list = []
#     for i in string:
#         temporary_list.append(i)
#     for i in range(1, len(temporary_list)):
#         result.append(temporary_list[i - 1] + temporary_list[i])
#     if len(temporary_list) % 2 == 0:
#         return result[::2]
#     last_elem = result[-1]
#     last_elem = last_elem[-1] + "_"
#     result = result[::2]
#     result.append(last_elem)
#     return result
#
#
# print(split_string("a"))
# print(split_string("abcdefg"))
#
# __________________________________________________________________________________
#
#
# def scrolling_text(string: str) -> list:
#     result_list = [string.upper()]
#     tempo_string = string
#
#     for i in string:
#         tempo_string = tempo_string[1::]
#         tempo_string = tempo_string.upper() + i.upper()
#         result_list.append(tempo_string)
#     result_list.pop()
#     return result_list
#
#
# print(scrolling_text("robot"))
#
#
# def check_number(number: int) -> list:
#     result = []
#     if number > 0:
#         result.append(True)
#     else:
#         result.append(False)
#     if number % 2 == 0:
#         result.append(True)
#     else:
#         result.append(False)
#     if number % 10 == 0:
#         result.append(True)
#     else:
#         result.append(False)
#     return result
#
#
# def get_lists_sum(ls1: list, ls2: list) -> int:
#     result = 0
#
#     for i in ls1:
#         result += i
#
#     print("*" * 10)
#
#     for i in ls2:
#         result += i
#
#     return result
#
#
# print(get_lists_sum([1, 2], [3, 4])) == 10  # 1 + 2 + 3 + 4 = 10
# print(get_lists_sum([], [])) == 0
#
#
# def combine_lists(ls1: list, ls2: list) -> list:
#     result = [0] * len(ls1)
#     print(result)
#     for i in range(len(result)):
#         result[i] += ls1[i] + ls2[i]
#         print(result[i])
#     return result
#
#     # result[0] += ls1[0] + ls2[0]
#     # result[1] += ls1[1] + ls2[1]
#     # result[2] += ls1[2] + ls2[2]
#
#     print(result)
#
#     # print(result)
#
#
# combine_lists([1, 2, 5], [3, 6, 1])  # == [4, 8, 6]
#
# всегда
# до
# конца
# 1 - й
# строки
# по
# очереди
#
#
# def spiral(resolution: int):
#     result = [0] * resolution ** 2
#     result[-1] = resolution ** 2
#     result = result[::-1]
#
#     for i in range(1, len(result)):
#         print(f"(i) = {(i)} // [i] = {[i]}")
#         if result[i] < result[i - 1]:
#             result[i] = result[i - 1] - 1
#
#     result = result[::-1]
#
#     # result.insert(resolution, "change direction")
#     # for i in result[resolution-1::resolution+1]:
#     #     result.insert(i,'change direction')
#     # result.append('change direction')
#     # print(f"result list at this stage: {result}")
#
#     print(f"result list at final stage: {result}")
#     return result
#
#
# spiral(3)
#
#
# def is_jumping(number: int) -> str:
#     number = str(number)
#     test = []
#     errors = 0
#     for i in number:
#         test.append(i)
#     if len(test) < 2:
#         return "JUMPING"
#     for i in range(1, len(test)):
#         y = int(test[i])
#         x = int(test[i - 1])
#         if (x - y) == 1 \
#                 or (x - y) == -1 \
#                 or (x + y) == 1 \
#                 or (x + y) == -1:
#             errors += 0
#         else:
#             errors += 1
#     if errors == 0:
#         return "JUMPING"
#     else:
#         return "NOT JUMPING"
#
#
# is_jumping(12543)
#
#
# def is_special_number(number: int) -> str:
#     special_numbers = [0, 1, 2, 3, 4, 5]
#     list_but_number = []
#     to_compare = []
#     counter = 0
#     for i in str(number):
#         list_but_number.append(i)
#     for i in list_but_number:
#         to_compare.append(int(i))
#
#     print(special_numbers)
#     print(list_but_number)
#     print(to_compare)
#     for i in to_compare:
#         if i in special_numbers:
#             counter += 1
#     if counter == len(to_compare):
#         return "Special!!"
#     else:
#         return "NOT!!"
#
#
# def is_tidy(number: int) -> bool:
#     list_str = []
#     list_num = []
#     counter = 0
#     for i in str(number):
#         list_str.append(i)
#     for i in list_str:
#         list_num.append(int(i))
#     if len(list_num) == 1:
#         return True
#     for i in range(1, len(list_num)):
#         if list_num[i - 1] <= list_num[i]:
#             counter += 1
#     if counter + 1 == len(list_num):
#         return True
#     else:
#         return False
#
#
# ctrl + shift + a // shortcut
# info
# ctrl + r // change
# variable
# name
# everywhere
# python - m
# pdb
# basics_extended_note.py
#
# print("""
# q
# we
# rty
# sd""")
# f = 123
# x = 'qwe'
# a = 12
# cwerwerrwe = \
#     'qeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq %s' % \
#     a  # "%s" % X //It automatically provides type conversion from value to string
# cwerwerrwe = 'qw'
#
#
# def sum(q,
#         we,
#         e,
#         r):
#     """
#     this f
#     """
#
#
# print("asdsdfsdfljkfdsjlkfdsjlkdfsjkldfsjkdflsfdslkjfsdkjfjsdlfjsd "
#       "flskdjf ssldfj sdlf sdlfslffsdlkdf sdlkfjs dlfjsdlf "
#       "sldfkjsdfjffj for "
#       "asddddddddddddddddddddddddddddddddddddddddddddd"
#
# change
# code
# below
# change
# code
# below
# trapeze_perimeter = 2 + 4 + 4 + 10
# triangle_perimeter = 10 + 20 + 30
# rectangle_perimeter = 2 * (50 + 20)
# big_math_formula = (
#                            10 * trapeze_perimeter +
#                            rectangle_perimeter * 100) - 228
# print(big_math_formula)
#
#
# def login_with_username_and_password(username: str,
#                                      password: str) -> str:
#     """
#     This "super-secure" function simulates login process.
#     If password is equal to "12345678",
#     it is considered that the user has successfully logged in
#     """
#     if password == "12345678":
#         print("Successfully logged in!")
#         return "Successfully logged in!"
#     print("Login Failed: incorrect password")
#     return "Login Failed: incorrect password"
#
#
# login_with_username_and_password('boba', '12345678')
# fffff
#
# import requests
#
# r = requests.get('https://pypi.org/project/requests/', auth=(
#     'user', 'pass'))
# print(r.status_code)
#
# a = 10
# b = a + 5
# c = a + b
# print(c)
#
#
# def print_index_ok(index: int):
#     print(index)
#     print("Ok!")
#
#
# print("--- START ---")
#
# for i in range(3):
#     print_index_ok(i)
#
# print("--- END!---")
#
# decimal = 111
# = 100 + 10 + 1
# binary = 0b111
# hexadecimal = 0x111
#
# print(decimal, binary, hexadecimal)
#
# x = (10 % 2) ** 2
# print(x)
#
# print(10 ** 100)
#
# x = 0.1 + 0.2
# print(x)
#
# y = 0.3
# print(y)
#
# z = x - y
# print(z)
# d = 4.44
# v = d - z
# print(v)
#
# x = float('nan')
#
# print(type(x))
#
# x = 16 ** 0.5
# print(x)
#
# g = (-1) ** 0.5
# print(type(g))
#
# input = '-12 '
# if input.strip().isnumeric():  # strip -> delete spaces //
#     print("ok")
# else:
#     print('not a number')
#
# import random
#
# list = []
# avgsum = 0
# for i in range(1000):
#     x = random.random() * 1000000
#     list.append(x)
#
# print(len(list))
# for i in list:
#     avgsum += i
#
# res = avgsum / len(list)
# print(res)
#
# import random
#
# for i in range(10):
#     # x = int(random.random() * 5 + 2)
#     x = random.randint(2, 7)
#     print(x)
#
# my_bin = bin(10)
# my_oct = oct(20)
# my_dec = 30
# my_hex = hex(40)
# print(f"""
# system 2;  10 = {my_bin}
# system 8;  20 = {my_oct}
# system 10; 30 = {my_dec}
# system 15; 40 = {my_hex}""")
#
#
# def get_century(year: int) -> int:
#     year_str_format = str(year)
#     result_list = []
#     temporary_result = 0
#     for i in year_str_format:
#         result_list.append(i)
#     if year <= 100:
#         return 1
#     if len(year_str_format) == 3:
#         if result_list[1] == result_list[2] == "0":
#             return int(year_str_format[0])
#         else:
#             return int(year_str_format[0]) + 1
#     if len(year_str_format) == 4:
#         if result_list[2] == result_list[3] == "0":
#             temporary_result = result_list[0] + result_list[1]
#             temporary_result = int(temporary_result)
#             return temporary_result
#         temporary_result = result_list[0] + result_list[1]
#         temporary_result = int(temporary_result) + 1
#         return temporary_result
#     if len(year_str_format) == 5:
#         if result_list[2] == result_list[3] == result_list[4] == "0":
#             temporary_result = result_list[0] + result_list[1] + result_list[2]
#             temporary_result = int(temporary_result)
#             return temporary_result
#         temporary_result = result_list[0] + result_list[1] + result_list[2]
#         temporary_result = int(temporary_result) + 1
#         return temporary_result
#
#
# get_century(40000)
#
# from typing import Union
#
#
# def get_rectangle_area(side: int, diagonal: int) -> Union[float, str]:
#     if diagonal <= side or side == 0:
#         return "not a rectangle"
#     return round(side * (((diagonal ** 2) - (side ** 2)) ** 0.5), 1)
#
#
# from typing import Union
#
#
# def is_even(number: Union[int, float]) -> bool:
#     if number % 2 == 0:
#         return True
#     if type(number) == float:
#         return False
#     return False
#
#
# def number_checker(number: float) -> list:
#     list = []
#     if type(number) == inf:
#         list.append(True)
#
#
# number_checker(-1e10000)
#
#
# def number_checker(number: float) -> list:
#     result = []
#     if math.isinf(number) is True:
#         result.append(True)
#     else:
#         result.append(False)
#
#     if math.isnan(number) is True:
#         result.append(True)
#     else:
#         result.append(False)
#     print(list)
#     return result
#
#
# def make_decision(
#         fuel_remaining: int,
#         distance: int,
#         fuel_consumption: float
# ) -> str:
#     if fuel_remaining < 0 or distance < 0 or fuel_consumption <= 0:
#         return "please, enter the valid data"
#     if fuel_remaining >= distance * (fuel_consumption / 100):
#         return "reach gas station by themselves"
#     return "ask for help"
#
#
# a = 10
# b = 4
#
# add_assignment = a
# sub_assignment = a
# div_assignment = a
# mul_assignment = a
# exp_assignment = a
# mod_assignment = a
#
# WRITE
# CODE
# BELOW
# THIS
# LINE
# add_assignment += b
# sub_assignment -= b
# div_assignment //= b
# mul_assignment *= b
# exp_assignment **= b
# mod_assignment %= b
# WRITE
# CODE
# ABOVE
# THIS
# LINE
#
#
# def count_networking(quarantine_length: int, frequency: int) -> int:
#     possibility = 12 - quarantine_length
#     return math.ceil(possibility / frequency)
#
#
# count_networking(3, 2)
#
#
# def generate_random_list(min_value: int, max_value: int,
#                          length: int) -> list:
#     rand_num_list = []
#     for i in range(0, length):
#         rand_num_list.append(random.randint(min_value, max_value))
#     return rand_num_list
#
#
# from typing import Union
#
#
# def calculate_guests(guests_input: str) -> Union[int, str]:
#     result = []
#     result_return = []
#     final_result = ""
#     guests_input = guests_input.split(".")
#     for i in guests_input:
#         result.append(i)
#     result_str = result[0]
#     for i in result_str:
#         if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" \
#                 or i == "5" or i == "6" or i == "7" or i == "8" or i \
#                 == "9":
#             result_return.append(i)
#     if result_return[0] == 0:
#         return "not a number"
#     if len(result_return) == 0:
#         return "not a number"
#     if len(result_return) == 1:
#         return int(final_result + result_return[0])
#     if len(result_return) == 2:
#         return int(final_result + result_return[0] + result_return[1])
#     if len(result_return) == 3:
#         return int(final_result + result_return[0] + result_return[1] + \
#                    result_return[2])
#
#
# from typing import Union
#
#
# def calculate_guests(guests_input: str) -> Union[int, str]:
#     if len(guests_input) == 0:
#         return "not a number"
#     list_of_numbers_str_format = ["1", "2", "3", "4", "5", "6", "7",
#                                   "8", "9", "0"]
#     result_number_str_format = ""
#     current_i = ""
#     counter_for_1_digit = 0
#
#     for i in guests_input:
#         if i in list_of_numbers_str_format:
#             print(i)
#             current_i = i
#             counter_for_1_digit += 1
#     if current_i == "0":
#         return "not a number"
#     if counter_for_1_digit == 0:
#         return "not a number"
#     if counter_for_1_digit == 1:
#         return int(current_i)
#     for i in range(0, len(guests_input)):
#         if guests_input[i] in list_of_numbers_str_format:
#             result_number_str_format += str(guests_input[i])
#             if guests_input[i + 1] not in list_of_numbers_str_format:
#                 break
#     if int(result_number_str_format) == 0:
#         return "not a number"
#     return int(result_number_str_format)
#
#
# calculate_guests("alone")
#
# my_string = "Hello!\nMy favourite book is \"Clean Code\""
# print(my_string)
#
#
# def is_alphabet(letters: str) -> bool:
#     if len(letters) == 1:
#         return True
#     errors = 0
#     for i in range(1, len(letters)):
#         if ord(letters.lower()[i]) - 1 != ord(letters.lower()[i - 1]):
#             errors += 1
#     if ord(letters.lower()[-1]) - 1 != ord(letters.lower()[-2]):
#         errors += 1
#     if errors == 0:
#         return True
#     else:
#         return False
#
#
# is_alphabet('abcde')
#
#
# def extract_names(message: str) -> list:
#     result = message.split(",")
#     result2 = []
#     for i in result:
#         result2.append(i.strip())
#     return result2
#
#
# extract_names("Oleg")
# ["Oleg"]
# extract_names("Ivan,  Mark,  Sergey")
# ["Ivan", "Mark", "Sergey"]
# extract_names("Ivan,Mark,Sergey")
# ["Ivan", "Mark", "Sergey"]
# extract_names(" Catelyn Stark   ,Samwell Tarly   ,  Bronn")
# ["Catelyn Stark", "Samwell Tarly", "Bronn"
#
#
# def make_variable_name(words: str, number_of_words: int) -> str:
#     if number_of_words == 0:
#         return ""
#     if len(words) == 0:
#         return ""
#     if len(words) == 1:
#         return words
#     result = words.split()
#     tempo_string = ""
#     for i in result:
#         tempo_string += i
#         number_of_words -= 1
#         if number_of_words > 0:
#             tempo_string += "_"
#         else:
#             break
#
#     return tempo_string
#
#
# def make_upper(text: str, letter: str) -> list:
#     result_int_before = text.count(letter.upper())
#     result_str = text.replace(letter, letter.upper())
#     result_int_after = result_str.count(
#         letter.upper()) - result_int_before
#     return [result_str, result_int_after]
#
#
# make_upper('AAaa', 'a')
#
#
# def calc(a=2, b=3):
#     c = a * b
#     print(c)
#
#
# calc(3, 1)
#
#
# def double_num(num: int) -> int:
#     print(num * 2)
#
#
# double_num(4)
#
# double_num_lambda = lambda num: print(num * 2)
# double_num_lambda(5)
#
# qwe = lambda qq: print(qq * 2)
# qwe(100)
#
#
# def multiply_numbers(a: int = 0, b: int = 1) -> int:
#     return a * b
#
#
# greeter = lambda name: "Hello" + ", " + name + "!"
#
# triple_it = lambda input_string: input_string * 3
#
# multiply_numbers = lambda a=1, b=1, *args, **kwargs: a * b
#
#
# def multiply_numbers(a: int = 1, b: int = 1, *args, **kwargs) -> int:
#     return a * b
#
#
# def print_message(username: str, message: str) -> str:
#     print(f"Message from {username}:\n"
#           f"{message}")
#
#
# print_message(username="John", message="I like coding!")
#
# counter = 0
#
#
# def get_random_value():
#     return random.randrange(1, 100000, 1)
#
#
# while True:
#     x = get_random_value()
#     counter += 1
#     print(f"Random num == {x}\n"
#           f"Operation № {counter}")
#     if x == 1:
#         break
#
#
# def get_years(amount: int, percent: int, limit: int) -> int:
#     years = [amount]
#     end_of_year = amount + ((amount / 100) * percent)
#     while end_of_year <= limit:
#         years.append(end_of_year)
#         end_of_year += ((end_of_year / 100) * percent)
#     return len(years) - 1
#
#
# get_years(500, 3, 550)
#
#
# def check_is_prime(number: int) -> bool:
#     flag = False
#     result = list(range(1, (number)))
#     print(f"Number = {number}\nWe create range: {result}")
#     for i in result:
#         print(f"We checking for residue by each num in list, so:")
#         print(f"{number} % {i} = {number / i}")
#     return Flag
#
#
# check_is_prime(13)
#
#
# def check_is_prime(number: int) -> bool:
#     if number <= 1:
#         print("False")
#         return False
#     tempo_list = list(range(2, number))
#     counter = 0
#     for i in tempo_list:
#         current_check = number % i
#         if current_check == 0:
#             counter += 1
#     if counter != 0:
#         print("FALSE")
#         return False
#     else:
#         print("TRUE")
#         return True
#
#
# check_is_prime(-1)  # false
# check_is_prime(0)  # false
# check_is_prime(1)  # false
# check_is_prime(13)  # true
# check_is_prime(-3)  # false
#
#
# def detect_lowercase_words() -> None:
#     to_check = input("Pishi suda plz: ")
#
#     flag = True
#
#     while flag is True:
#         if "exit" in to_check:
#             flag = False
#     for i in range(0, len(to_check)):
#         if i.isupper() is False:
#             counter += 1
#     if counter - len(to_check) != 0:
#         print(f"{to_check} detected")
#
#
# detect_lowercase_words()
# detect_lowercase_words()
#
# counter = 0
# while True:
#     counter += 1
#     print(counter)
#
#
# def detect_lowercase_words() -> None:
#     counter = 0
#     while True:
#         user_input = input(f"")
#         if "exit" in user_input:
#             break
#         for i in user_input:
#             if i.isalpha() is True:
#                 if i == i.upper():
#                     counter += 1
#
#         if counter == 0:
#             print(f"{user_input} detected")
#
#
# detect_lowercase_words()
#
#
# def detect_lowercase_words() -> None:
#     while True:
#         word = input("")
#         if word == "exit":
#             break
#         if word == word.lower():
#             print(f"{word} detected")
#
#
# detect_lowercase_words()
#
# from typing import Any
#
#
# def decode_signal(message: Any) -> int:
#     result = 0
#     if bool(message) is True:
#         result += 1
#     return result
#
#
# from typing import Union
#
#
# def get_winner(
#         max_solved: Union[str, int], roman_solved: Union[str, int]
# ) -> str:
#     if int(max_solved) == int(roman_solved):
#         return "Roman and Maxim are the winners!!!"
#     if int(max_solved) > int(roman_solved):
#         return "Max winner!!!"
#     return "Roman winner!!!"
#
#
# def can_they_book(adults_count=0, children_count=0, *args, **kwargs):
#     if 8 - (adults_count + children_count) < 0:
#         return False
#     if adults_count <= 0:
#         return False
#     if children_count / adults_count > 2:
#         return False
#     return True
#
#
# def can_they_book(
#         adults_count: int = 0,
#         children_count: int = 0,
#         babies_count: int = 0,
#         *args,
#         **kwargs
# ) -> bool:
#     if adults_count < 1:
#         return False
#     if (adults_count + children_count + babies_count) > 9:
#         return False
#     if ((babies_count == 0) or (babies_count == 1)) and (
#             (adults_count + children_count) > 8):
#         return False
#     if (children_count + babies_count) / adults_count > 2:
#         return False
#     return True
#
#
# def recommend_room(
#         adults_count: int = 0,
#         children_count: int = 0,
#         babies_count: int = 0,
#         *args,
#         **kwargs
# ) -> str:
#     result = ""
#     if ((adults_count + children_count + babies_count) > 6) and (
#             (adults_count + children_count + babies_count) < 9):
#         return "big room"
#     if ((adults_count + children_count) <= 4) and (babies_count == 0):
#         return "small room"
#     if (babies_count != 0) and ((adults_count + children_count + babies_count) <= 5):
#         result += "small room"
#         if (babies_count != 0) and ((adults_count + children_count + babies_count) == 5):
#             result += " + extra bed"
#         else:
#             return result
#     else:
#         result += "big room"
#     if (babies_count != 0) and ((adults_count + children_count + babies_count) == 9):
#         result += " + extra bed"
#     return result
#
#
# recommend_room(2, 2, 1)  # == "small room + extra bed"
# recommend_room(2, 1, 1)  # == "small room"
# recommend_room(3, 2)  # == "big room"
# recommend_room(3, 0, 2)  # == "small room + extra bed"
# recommend_room(7, 0, 2)  # == "big room + extra bed"
# recommend_room(8)  # == "big room"
#
#
# def get_sorted(ls: list) -> list:
#     if len(ls) == 0:
#         return []
#     x = ls.copy()
#     x.sort()
#     return x
#
#
# get_sorted([2, 1, 3])  # == [1, 2, 3]
# get_sorted([10, -10, 0, 145])  # == [-10, 0, 10, 145]
# get_sorted([])
#
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
#         "Sunday", "Saturday"]
#
#
# def weekday_order(weekday: str) -> int:
#     if weekday == "Monday":
#         return 1
#     if weekday == "Tuesday":
#         return 2
#     if weekday == "Wednesday":
#         return 3
#     if weekday == "Thursday":
#         return 4
#     if weekday == "Friday":
#         return 5
#     if weekday == "Sunday":
#         return 6
#     if weekday == "Saturday":
#         return 7
#
#
# def sort_weekdays(weekdays: list) -> list:
#     return (sorted(weekdays, key=weekday_order))
#
#
# sort_weekdays(["Saturday", "Monday", "Tuesday", "Sunday",
#                "Wednesday", "Thursday",
#                "Friday", "Sunday", "Saturday"])
#
# african_animals = ["Lion", "Leopard", "Elephant", "Rhinoceros", "Giraffe"]
# new_african_animals = ["Hippo", "Gorilla"]
# european_animals = ["Brown Bear", "Wild Boar", "Polar Bear", "Red Deer"]
# african_animals += new_african_animals
# animals = african_animals + european_animals
#
#
# def get_speed_statistic(test_results: list) -> list:
#     return [min(test_results), max(test_results),
#             math.floor((sum(test_results) / len(test_results)))]
#
#
# def all_targets_hit(attempts_for_each_target: list) -> bool:
#     result = []
#     for i in attempts_for_each_target:
#         result.append(any(i))
#         print(i)
#         print(result)
#     return all(result)
#
#
# all_targets_hit([
#     [True, False, True],  # Постріли у першу мішень
#     [False, True, False, True],  # Постріли у другу мішень
#     [False],  # Постріли у третю мішень
# ])
#
#
# def create_dino_archive(
#         dino_names: list,
#         dino_lengths: list,
#         dino_diets: list,
# ) -> list:
#     result = []
#     counter = list(range(len(dino_names)))
#     for i in counter:
#         current_dino = (dino_names[i], dino_lengths[i], dino_diets[i])
#         result.append(current_dino)
#     return result
#
#
# create_dino_archive([
#     "Saltopus",
#     "Triceratops",
#     "Talarurus",
#     "Urbacodon",
#     "Hypsilophodon"],
#     [1, 9, 6, 1, 2],
#     ["carnivorous",
#      "herbivorous",
#      "herbivorous",
#      "carnivorous",
#      "herbivorous", ])
#
# second_dict = {"KEY": "VALUE",
#                "KEY2": 23}
#
# print(second_dict)
# print(type(second_dict["KEY2"]))
#
# print(second_dict.get("key"))
# print(second_dict.get("KEY"))
#
# for i in second_dict:
#     print(i, second_dict[i])
# print("*" * 10)
# for i, j in second_dict.items():
#     print(i, j)
#
# for key, value in second_dict.items():
#     print(key, value)
#
# test_l = ["carnivorous",
#           "herbivorous",
#           "herbivorous",
#           "carnivorous",
#           "herbivorous", "herbivorous"]
#
# print(len(test_l))
#
# test_set = {"carnivorous",
#             "herbivorous",
#             "herbivorous",
#             "carnivorous",
#             "herbivorous", "herbivorous"}
#
# print(len(test_set))
#
# test_set_2 = set(test_l)
# print(len(test_set_2))
#
# second_dict = {"KEY": "VALUE",
#                "KEY2": 23}
#
# for i, i2 in second_dict.items():
#     print(i, i2)
#
# my_set = set()
# my_set = {}
# my_set = []
# print(type(my_set))
#
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict["color"] = "red"
# thisdict["color"] = "blue"
# print(thisdict)
#
# warehouse = {"memory": 15, "processors": 10, "displays": 20}
#
#
# def restore_names(users: list) -> None:
#     print(f"START {users}")
#     print("*" * 74)
#     print("*" * 74)
#     print("*" * 74)
#
#     result = []
#     for i in users:
#         print("*" * 74)
#         print(f"current index is {i}")
#         print(type(i))
#         i["first_name"] = i.get("full_name").split()[0]
#         print(f"result for current index is {i}")
#         print("*" * 74)
#         result.append(i)
#         print(result)
#     print("*" * 74)
#     print("*" * 74)
#     print(result)
#     users = result
#     print(users)
#
#
# def restore_names(users: list) -> None:
#     result = []
#     for i in users:
#         i["first_name"] = i.get("full_name").split()[0]
#         result.append(i)
#     users = result
#
#
# users = [{'full_name': 'Rubeus Hagrid', 'last_name': 'Hagrid'},
#          {'full_name': 'Draco Malfoy', 'last_name': 'Malfoy'},
#          {'first_name': 'Hermione', 'full_name': 'Hermione Granger', 'last_name': 'Granger'}]
# restore_names(users)
#
#
# def add_full_name(user: dict) -> None:
#     user["full_name"] = user["first_name"] + " " + user["last_name"]
#
#
# user = {
#     "first_name": "Ivan",
#     "last_name": "Vasylchenko",
# }
#
# add_full_name(user)
#
#
# def remove_country(users: list) -> None:
#     print(users)
#     for i in users:
#         if i["status"] == "active":
#             del i["country"]
#
#
# users = [
#     {"name": "Emma", "status": "active", "country": "Ukraine"},
#     {"name": "Avram", "status": "disabled", "country": "Poland"},
# ]
#
# remove_country(users)
#
#
# def test_dict(dict):
#     for key, value in dict.items():
#         print(f"user {key} is {value}")
#
#
# dict = {"name": "Alinochka", "wish": "download SHREK2"}
# test_dict(dict)
#
#
# def get_outdated(robots: list, new_version: int) -> list:
#     result = []
#     for current_dict_number in range(len(robots)):
#         for version in robots[current_dict_number].values():
#             if version < new_version:
#                 result.append(current_dict_number)
#     return result
#
#
# robots = [
#     {"core_version": 9},
#     {"core_version": 13},
#     {"core_version": 16},
#     {"core_version": 9},
#     {"core_version": 14},
# ]
# get_outdated(robots, 10)
#
#
# def count_boxes(boxes: str) -> dict:
#     result = {}
#     if len(boxes) < 1:
#         return result
#     boxes_set = set(boxes)
#     for char in boxes_set:
#         result[char] = boxes.count(char)
#         print(result)
#     return result
#
#
# count_boxes(
#     "{}$%^-report6")
#
#
# def compare_robots(robot1: dict, robot2: dict) -> bool:
#     robot_1 = robot1.copy()
#     robot_2 = robot2.copy()
#
#     if robot_1 == robot_2:
#         return True
#
#     if len(robot_1) != len(robot_2):
#         return False
#
#     del robot_1["serial_no"]
#     del robot_2["serial_no"]
#
#     for i in robot_1:
#         if i in robot_2:
#             if robot_1[i] != robot_2.get(i):
#                 return False
#         else:
#             return False
#
#     return True
#
#
# charlie = {"serial_no": 1, "chip_ver": 12}
# steve = {"serial_no": 6}
# compare_robots(steve, charlie)  # False
#
#
# def count_marks(class_register: dict) -> dict:
#     result = {}
#     temp_list = []
#
#     for score in class_register.values():
#         temp_list.append(score)
#
#     for name, score in class_register.items():
#         result[score] = temp_list.count(score)
#
#     return result
#
#
# class_register = {
#     "Robb Stark": 10,
#     "Sansa Stark": 12,
#     "Arya Stark": 6,
#     "Bran Stark": 8,
#     "Jon Snow": 8,
# }
# count_marks(class_register)
#
#
# def get_unique_marks(class_register: dict) -> list:
#     result = []
#     for i in class_register.values():
#         result.append(i)
#     return set(result)
#
#
# class_register = {
#     "Robb Stark": 2,
#     "Sansa Stark": 12,
#     "Arya Stark": 2,
#     "Bran Stark": 2,
#     "Jon Snow": 2,
# }
# get_unique_marks(class_register)
#
#
# def get_unique_items(ls: list) -> list:
#     return list(set(ls))
#
#
# get_unique_items([1, 2, 4, 4])  # == [1, 2, 4]
# get_unique_items([1, 7, 10])  # == [1, 7, 10]
# get_unique_items([2, 7, 2, 8, 8, 1])  # == [2, 7, 8, 1]
#
#
# def color_stones(stones: str) -> int:
#     counter = 0
#     stones_list = []
#     for i in stones:
#         stones_list.append(i)
#
#     for char in range(1, len(stones_list)):
#         if stones_list[char] == stones_list[char - 1]:
#             counter += 1
#
#     return counter
#
#
#
# def find_smaller_digits(ls: list) -> list:
#     if len(ls) == 1:
#         return 0
#     result = []
#     counter = 0
#     current_num = 0
#     if len(ls) == 0:
#         return result
#     for i in range(1, len(ls)):
#         current_num = ls[i - 1]
#         for j in ls[i::]:
#             if current_num > j:
#                 counter += 1
#         result.append(counter)
#         counter = 0
#     result.append(0)
#     return result
#
#
# ls = [5, 4, 3, 2, 1]
# find_smaller_digits(ls)
#
#
# def get_product_id(url: str) -> str:
#     result = ""
#     list_chars = list(url)[:-14:]
#     list_chars = list_chars[::-1]
#     for i in list_chars:
#         if i == "-":
#             return result[::-1]
#         else:
#             result += i
#
#
# def get_leaders(numbers: list) -> list:
#     result = []
#     if len(numbers) < 3:
#         return result
#     for i in range(len(numbers)):
#         print(f"current number is {numbers[i]}")
#         print(f"all other numbers is {numbers[i + 1::]}")
#         if numbers[i] > sum(numbers[i + 1::]):
#             result.append(numbers[i])
#             print(result)
#     return result
#
#
# get_leaders([16, 17, 4, 3, 5, 2])  # == [17, 5, 2]
#
#
# def product_list(numbers: list) -> list:
#     result = []
#     multiplication_point = 1
#     current_multiplication_list = []
#     x = 1
#
#     counter = len(numbers)
#     if len(numbers) == 2:
#         return numbers[::-1]
#     while counter > 0:
#         tempo_list = []
#         for num in range(len(numbers)):
#             current_multiplication_list = numbers[:num:] + numbers[
#                                                            num + 1::]
#             print(current_multiplication_list)
#             for mult_i in current_multiplication_list:
#
#                 print(mult_i)
#                 multiplication_point *= mult_i
#                 tempo_list.append(multiplication_point)
#                 print(tempo_list)
#                 if len(tempo_list) == len(numbers) - 1:
#                     print(tempo_list[-1])
#                     result.append(tempo_list[-1])
#                     tempo_list = []
#                     multiplication_point = 1
#             counter -= 1
#     print(result)
#     if len(numbers) == len(result):
#         return result
#
#
# product_list([2, 3, 4, 5])
#
# 13: 54
#
#
# def row_weights(row: list) -> list:
#     weight_1 = sum(row[0::2])
#     weight_2 = sum(row[1::2])
#     return [sum(row[0::2]), sum(row[1::2])]
#
#
# row_weights([10])  # == [10, 0]
# row_weights([10, 85, 90])  # == [100, 85]
# row_weights([8, 5, 9, 3])  # == [17, 8]
#
# 13: 59
#
#
# def who_is_online(friends: list) -> dict:
#     to_sort = []
#     for list_index_value in friends:
#         print("*" * 25)
#         print(list_index_value)
#         for key, value in list_index_value.items():
#             print(key, value)
#             if key == "username":
#                 to_sort.append(value)
#             if key == "status":
#                 to_sort.append(value)
#             if key == "lastActivity":
#                 to_sort.append(value)
#     result = {}
#     username_ = to_sort[::3]
#     status_ = to_sort[1::3]
#     lastActivity_ = to_sort[2::3]
#     online_ = []
#     offline_ = []
#     away_ = []
#     print("/" * 25)
#     for i in range(len(status_)):
#         print(i, username_[i])
#         print(i, status_[i])
#         print(i, lastActivity_[i])
#         if status_[i] == "offline":
#             offline_.append(username_[i])
#         if status_[i] != "offline" and lastActivity_[i] > 10:
#             away_.append(username_[i])
#         if status_[i] == "online" and lastActivity_[i] <= 10:
#             online_.append(username_[i])
#         print(f"{online_}, {offline_}, {away_}")
#         if len(offline_) > 0:
#             result["offline"] = offline_
#         if len(away_) > 0:
#             result["away"] = away_
#         if len(online_) > 0:
#             result["online"] = online_
#         print(result)
#     return result
#
#
# who_is_online([{
#     "username": "Alice",
#     "status": "online",
#     "lastActivity": 10
# }, {
#     "username": "Lucy",
#     "status": "offline",
#     "lastActivity": 22
# }, {
#     "username": "Bob",
#     "status": "online",
#     "lastActivity": 104
# }]
# )
#
#
# def count_letters_in_string(string: str) -> dict:
#     result_dict = {}
#     for i in set(string.lower()):
#         result_dict[i] = string.lower().count(i)
#
#     print(result_dict)
#     return result_dict
#
#
# count_letters_in_string(" The Zen of Python, by Tim Peters"
#                         "Beautiful is better than ugly."
#                         "Explicit is better than implicit."
#                         "Simple is better than complex."
#                         "Complex is better than complicated."
#                         "Flat is better than nested."
#                         "Sparse is better than dense."
#                         "Readability counts."
#                         "Special cases aren't special enough to break the rules."
#                         "Although practicality beats purity."
#                         "Errors should never pass silently."
#                         "Unless explicitly silenced."
#                         "In the face of ambiguity, refuse the temptation to guess."
#                         "There should be one-- and preferably only one --obvious way to do it."
#                         "Although that way may not be obvious at first unless you're Dutch."
#                         "Now is better than never."
#                         "Although never is often better than *right* now."
#                         "If the implementation is hard to explain, it's a bad idea."
#                         "If the implementation is easy to explain, it may be a good idea."
#                         "Namespaces are one honking great idea -- let's do more of those!")
#
#
# def sum_dicts(*args) -> dict:
#     l, l2, l3, l4 = [], [], [], []
#     result_dict = {}
#
#     for arg in args:
#         for key, value in arg.items():
#             l.append(key)
#             l.append(value)
#     print(l)
#     for i in range(len(l)):
#         if type(l[i]) is str:
#             l2.append(l[i])
#
#         else:
#             l3.append(l[i])
#     print(l, l2, l3)
#
#     for i in l2:
#         print(i)
#         if l2.count(i) > 1:
#             print('here')
#
#     print(result_dict)
#
#
# sum_dicts({"qw": 0, "wqe": 1}, {"qw": 1, "bd": 2})
#
#
# def sum_dicts(*args) -> dict:
#     result_dict = {}
#     temp_list = []
#     qw = 0
#     for arg in args:
#         qw = sum(arg.values(key="a"))
#         print(qw)
#
#     qw = sum(d.values())
#     print(result_dict)
#
#
# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
#
# sum_dicts(x, y)
#
# Python
# code
# to
# demonstrate
# return the
# sum
# of
# values
# of
# dictionary
# with same keys in list of dictionary
#
#
# def sum_dicts(*args) -> dict:
#     ini_dict = []
#     for arg in args:
#         ini_dict.append(arg)
#     # printing initial dictionary
#     print("initial dictionary", str(ini_dict))
#
#     # sum the values with same keys
#     counter = collections.Counter()
#     for d in ini_dict:
#         counter.update(d)
#
#     result = dict(counter)
#
#     print("resultant dictionary : ", str(counter))
#     return result
#
#
# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
# r = {"a": -1, "b": 2, "c": -5, "d": -2}
# t = {"a": 0, "b": 0, "c": 0, "d": 0}
#
# sum_dicts(r, t)
#
# import collections
#
#
# def sum_dicts(*args) -> dict:
#     ini_dict = []
#     for arg in args:
#         ini_dict.append(arg)
#     counter = collections.Counter()
#     for d in ini_dict:
#         counter.update(d)
#     result = dict(counter)
#     print("resultant dictionary : ", str(counter))
#     return result
#
#
# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
# r = {"a": -1, "b": 2, "c": -5, "d": -2}
# t = {"a": 0, "b": 0, "c": 0, "d": 0}
#
#
# def sum_dicts(*args) -> dict:
#     result_dict = {}
#     for cur_dict in args:
#         for k in cur_dict:
#             if k in result_dict:
#                 result_dict[k] += cur_dict[k]
#             else:
#                 result_dict[k] = cur_dict[k]
#     print(result_dict)
#     return result_dict
#
#
# sum_dicts(x, y)
#
#
# def sum_dicts2(*args) -> dict:
#     result = {}
#     for arg in args:
#         print(arg)
#         for k, v in arg.items():
#             if k in result:
#                 result[k] += arg[k]
#             else:
#                 result[k] = arg[k]
#     return result
#
#
# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
# r = {"a": -1, "b": 2, "c": -5, "d": -2}
# t = {"a": 0, "b": 0, "c": 0, "d": 0}
#
# sum_dicts2(x, y)
#
#
# def count_matching_socks(colors: list) -> int:
#     unique_colors = set(colors)
#     result_list = []
#     result = 0
#     for unique_color in unique_colors:
#         if colors.count(unique_color) > 1:
#             result_list.append((colors.count(unique_color) // 2))
#     print(result_list)
#     print(sum(result_list))
#     return (sum(result_list))
#
#
# x = [10, 10]  # 1 одна пара шкарпеток кольору 10.
# y = [2, 2, 2, 2, 2]  # - #2 дві пари шкарпеток кольору 2.
# q = [10, 20, 30, 40, 50, 60]  # 0 - всі шкарпетки різних кольорів
# w = [10, 20, 30, 10, 20, 60]  # 2. Одна кольору 10 і одна кольору 20.
# count_matching_socks(x)
# count_matching_socks(y)
# count_matching_socks(q)
# count_matching_socks(w)
#
#
# def smash(words):
#     result = ""
#     if len(words) == 0:
#         return result
#     if len(words) == 1:
#         return str(words[0])
#     for i in range(len(words) - 1):
#         result += words[i] + " "
#     return result + words[-1]
#
#
# smash(['hello', 'world', 'this', 'is', 'great'])
#
# from random import choice
#
#
# def decks_count(crafts_amount: int):
#     all_cards = ["Ace_1", "2_1", "3_1", "4_1", "5_1", "6_1", "7_1",
#                  "8_1",
#                  "Ace_2", "2_2", "3_2", "4_2", "5_2", "6_2", "7_2",
#                  "8_2"
#                  "Ace_3", "2_3", "3_3", "4_3", "5_3", "6_3", "7_3",
#                  "8_3"
#                  "Ace_4", "2_4", "3_4", "4_4", "5_4", "6_4", "7_4",
#                  "8_4"]
#     deck_1 = []
#     deck_2 = []
#     deck_3 = []
#     deck_4 = []
#     all_possible_cards = 32
#     x = ""
#     print(
#         f"Crafts amount == {crafts_amount} ||  "
#         f"Range == {all_possible_cards}")
#
#     for craft in range(crafts_amount + 1):
#         print(f"CRAFT # {craft}___________________________")
#         x = choice(all_cards)
#         if "_1" in x:
#             deck_1.append(x)
#             print(f"DECK_1 WAS CHANGED : {x} WAS ADDED")
#         if "_2" in x:
#             deck_2.append(x)
#             print(f"DECK_2 WAS CHANGED : {x} WAS ADDED")
#         if "_3" in x:
#             deck_3.append(x)
#             print(f"DECK_3 WAS CHANGED : {x} WAS ADDED")
#         if "_4" in x:
#             deck_4.append(x)
#             print(f"DECK_4 WAS CHANGED : {x} WAS ADDED")
#         print("COMPLETE___________________________________")
#
#     deck_1.sort()
#     deck_2.sort()
#     deck_3.sort()
#     deck_4.sort()
#
#     print(f"__________________RESULTS__________________")
#
#     print(f"DECK_1 FINAL RESULT : \n{deck_1}\nCards ot this type: "
#           f"{len(deck_1)}\n_____________________")
#     if len(deck_1) == 8:
#         print("all 8 cards in deck#1")
#     print(f"DECK_2 FINAL RESULT : \n{deck_2}\nCards ot this type: "
#           f"{len(deck_2)}\n_____________________")
#     if len(deck_2) == 8:
#         print("all 8 cards in deck#2")
#     print(f"DECK_3 FINAL RESULT : \n{deck_3}\nCards ot this type: "
#           f"{len(deck_3)}\n_____________________")
#     if len(deck_3) == 8:
#         print("all 8 cards in deck#3")
#     print(f"DECK_4 FINAL RESULT : \n{deck_4}\nCards ot this type: "
#           f"{len(deck_4)}\n_____________________")
#     if len(deck_4) == 8:
#         print("all 8 cards in deck#4")
#
#     deck_1 = set(deck_1)
#     deck_2 = set(deck_2)
#     deck_3 = set(deck_3)
#     deck_4 = set(deck_4)
#     print("__________________________________________")
#     print("__________________________________________")
#     print("__________________________________________")
#     print("__________________________________________")
#
#     if len(deck_1) == 8:
#         print("all 8 cards in deck#1")
#     if len(deck_2) == 8:
#         print("all 8 cards in deck#2")
#     if len(deck_3) == 8:
#         print("all 8 cards in deck#3")
#     if len(deck_4) == 8:
#         print("all 8 cards in deck#4")
#
#
# decks_count(1000)
# ##
#
#
# a = {1
#
# asda
# as
# defasd
# asd
#
# }
# a = int(input('Введи чесло, и мы проверим чётное оно или нет:   '))
# b = a % 2
# if b > 0:
#     print('Из-за наличия остатка в количестве', str(b), "ваше число не является чётным")
# else:
#     print('Ваше число чётное')
#
#
# def is_tidy(number: int) -> bool:
#     temp = str(number)
#     for i in range(len(temp) - 1):
#         if temp[i] > temp[i + 1]:
#             return False
#     return True
#
#
# print(is_tidy(12))  # t
# print(is_tidy(32))  # f
# print(is_tidy(1024))  # f
# print(is_tidy(3445))  # t
# print(is_tidy(13579))  # t
#
#
# def spiral(resolution: int):
#     result = [0] * resolution ** 2
#     result[-1] = resolution ** 2
#     result = result[::-1]
#
#     for i in range(1, len(result)):
#         print(f"(i) = {(i)} // [i] = {[i]}")
#         if result[i] < result[i - 1]:
#             result[i] = result[i - 1] - 1
#
#     result = result[::-1]
#
#     # result.insert(resolution, "change direction")
#     # for i in result[resolution-1::resolution+1]:
#     #     result.insert(i,'change direction')
#     # result.append('change direction')
#     # print(f"result list at this stage: {result}")
#
#     print(f"result list at final stage: {result}")
#     return result
#
#
# spiral(3)
#
#
# import random
#
# random_num = random.randint(1, 100)
#
# attempt_range = range(1, 6)
# attempt_start = 6
# attempt_final = 7 - attempt_start
# attempt_match = attempt_start - 1
# user_num = int(input('your num please: '))
#
# for n in attempt_range:
#     if user_num == random_num:
#         print(f'You won, gj')
#         break
#     if user_num > random_num:
#         attempt_start -= 1
#         print(f'answer num LOWER than your, you have {attempt_start} more attempts')
#         user_num = int(input('your num please: '))
#     if user_num < random_num:
#         attempt_start -= 1
#         print(f'answer num GREATER than your, you have {attempt_start} more attempts')
#         user_num = int(input('your num please: '))
#     if attempt_start == 0:
#         break
#
#
# def get_drinks_with_step(number_of_guests: int, step: int) -> int:
#     counter = 0
#     for i in range(1, number_of_guests + 1, step):
#         counter += i
#     return len(counter)
#
#
# pasha_login = 'pasha'
# pasha_password = 'pashapasss777'
# user = input('name   ')  # html
# password = input('pass   ')  # html
# if pasha_login == user:
#     print('ya ya')
# else:
#     print('no no')
# romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
#
# XIV
#
#
# def parse_roman(roman):
#     result = 0
#
#     for i, c in enumerate(roman):
#         if i + 1 < len(roman) and romans[roman[i]] < romans[roman[i + 1]]:  #
#             result -= romans[roman[i]]
#         else:
#             result += romans[roman[i]]
#
#     return result
#
#
# print(parse_roman('I') == 1)
# print(parse_roman('II') == 2)
# print(parse_roman('IV') == 4)
# print(parse_roman('X') == 10)
# print(parse_roman('XIV') == 14)
# print(parse_roman('L') == 50)
# print(parse_roman('M') == 1000)
#
#
# def rome_to_arabic():
#     rome = input('input your rome number here: ')
#     pares = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
#     cycle_range = range(1, len(rome))
#     arabic_list = []
#     cycle_counter = 0
#     increment = 0
#     decrement = 0
#     result = 0
#
#     print(f'input rome len = {len(rome)}')
#     print(f'current cycle range len = {len(cycle_range)}')
#
#     print('_____________________________________________')
#     print('_____________________________________________')
#
#     for rome_number in rome:
#         for k, v in pares.items():
#             if rome_number == k:
#                 print('_________')
#                 print(f'current rome number = {rome_number}, his arabic pare = {v}')
#                 arabic_list.append(v)
#                 print(f'arabic_list in process: {arabic_list}')
#     print('_____________________________________________')
#     print('_____________________________________________')
#     print('we have next index/value pares in arabic_list')
#     for index, value in enumerate(arabic_list):
#         print((index, value))
#
#     for i, j in enumerate(arabic_list[:-1]):
#         if j >= arabic_list[i + 1]:
#             increment += arabic_list[i]
#         else:
#             decrement += arabic_list[i]
#
#     result = increment + arabic_list[-1] - decrement
#     print('_____________________________________________')
#     print('_________________result_section______________')
#     print(f'{rome} = {result}')
#     return result
#
#
# ##
#
#
# rome_to_arabic()
# There is a
# bus
# moving in the
# city, and it
# takes and
# drop
# some
# people in each
# bus
# stop.
# You
# are
# provided
# with a list ( or array) of integer pairs.
# Elements
# of
# each
# pair
# represent
# number
# of
# people
# get
# into
# bus(The
# first
# item) and number
# of
# people
# get
# off
# the
# bus
# (The second item) in a
# bus
# stop.
# Your
# task is to
# return number
# of
# people
# who
# are
# still in
# the
# bus
# after
# the
# last
# bus
# station(after
# the
# last
# array).
# Even
# though
# it is the
# last
# bus
# stop, the
# bus is not empty
# and some
# people
# are
# still in the
# bus, and they
# are
# probably
# sleeping
# there: D
# Take
# a
# look
# on
# the
# test
# cases.
# Please
# keep in mind
# that
# the
# test
# cases
# ensure
# that
# the
# number
# of
# people in the
# bus is always >= 0.
# So
# the
# return integer
# can
# 't be negative.
# The
# second
# value in the
# first
# integer
# array is 0, since
# the
# bus is empty in the
# first
# bus
# stop.
#
# test.assert_equals(number([[10, 0], [3, 5], [5, 8]]), 5)
# test.assert_equals(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)
# test.assert_equals(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)
#
#
# def number(bus_stops):
#     still_in_bus = 0
#     for i, j in bus_stops:
#         still_in_bus += i
#         still_in_bus -= j
#
#     return still_in_bus
#
#
# a = int(12345)
# b = int(12345)
# c = a / 2 + b / 2
# print(a, b, c)
# print(a == c)
# print(b == a)
# print(c == b)
# print(id(a))
# print(id(b))
# print(id(c))
#
# a = 12345
# b = 12345
# print(id(a), id(b))
# arr1 = [1, 2, 3]
# arr2 = [1, 2, 3]
# print(id(arr1))
# print(id(arr2))
#
# none1 = None
# none2 = None
# print(id(none1), id(none2))
# print((a is b))
# print(arr1 is arr2)
# print(none1 is none2)
#
# one1 = 1
# one2 = 1
# print(id(one1), id(one2))
# print(one1 is one2)
# print(id(False))
# print(id(True))
# print('here')
# a = True and False
# print(a is False)
# print(a is True)
# x = 2 * (True + 0.2)
# print(x)
# print(2 * 1.2)
#
# print(none1 is None)
#
# arr = [1, 2]
# print("id of arr before:", id(arr))
#
#
# def change_list(lst: list) -> None:
#     lst += [10]
#
#
# change_list(arr)
# print("id of arr after:", id(arr))
#
# print("arr:", arr)
#
# arr = 1
# bqq = 2
#
#
# def change_list(lst: list) -> None:
#     bqq = 2
#     lst += 100
#     print(bqq)
#     bqq += lst
#     print(bqq)
#
#
# print("id of arr before:", id(arr))
# change_list(arr)
# print("id of arr after:", id(arr))
#
# print("arr:", arr)
# print(bqq)
#
# a = ("hello", [4, 1, 2, 3], (3, 4))
# a[1].append(25)
# print(a)
# print(a[1])
#
# marks = {
#     "Bob": "Good",
#     "Alice": "Excellent",
# }
#
# marks["Bob"] += ", Excellent"
#
# print(marks)
#
# lucky_number = 777
# pi = 3.14
# one_is_a_prime_number = False
# name = "Richard"
# my_favourite_films = [
#     "The Shawshank Redemption",
#     "The Lord of the Rings: The Return of the King",
#     "Pulp Fiction",
#     "The Good, the Bad and the Ugly",
#     "The Matrix",
# ]
# profile_info = ("michel", "michel@gmail.com", "12345678")
# marks = {
#     "John": 4,
#     "Sergio": 3,
# }
# collection_of_coins = {1, 2, 25}
#
# sorted_variables = {"mutable": [], "immutable": []}
# sorted_variables[
#     "mutable"] += my_favourite_films, collection_of_coins, marks
# sorted_variables[
#     "immutable"] += one_is_a_prime_number, lucky_number, pi, profile_info, name
#
#
# def create_dictionary(*args, **kwargs):
#     big_dict = {True: 1, "sda": 2, None: 3, {"ew": 34}: 4}
#
#     print(big_dict)
#
#
# create_dictionary([1, 2, 3], "hello")
# test
# commit
# 20
# 28
# 23.01
# .23
#
#
# def create_dictionary(*args) -> dict:
#     result_dict = {
#     }
#     list_to_sort_args = []
#     counter = 0
#     for key_from_args in args:
#         list_to_sort_args += [[key_from_args, counter]]
#         counter += 1
#     del counter
#
#     for key_in_list in list_to_sort_args:
#
#         if isinstance(key_in_list[0], (int, str, tuple, float)) \
#                 or key_in_list[0] is None \
#                 or callable(key_in_list[0]) is True:
#             result_dict[key_in_list[0]] = key_in_list[1]
#         else:
#             print(f"Cannot add {key_in_list[0]} to the dict!")
#
#     return result_dict
#
#
# list1 = list(range(100))
# print(list1)
#
# rlist = []
# for i in list(range(100)):
#     if "3" in str(i):
#         rlist.append(i)
#
# print(rlist)
#
# print(x)
#
#
# def testitio(num):
#     num += 1
#     return num
#
#
# labdatest = lambda tempo: tempo * 2
# print(labdatest(testitio(1)))
#
# x = [i for i in list(range(100)) if "3" in str(i)]
# print(x)
#
# numbers = [3, 7, 2, 10]
# x = [num ** 2 for num in numbers]
# print(x)
# num = 10
#
# x = 100100
# y = 100100
# print(id(x))
# print(id(y))
# x = y + 1
# print(id(x))
#
# groups = [
#     ["a", "a"],
#     ["b", "b"]
# ]
# new_group = []
# for lilgroup in groups:
#     print(lilgroup)
#     for student in lilgroup:
#         print(student)
#         new_group.append((student) + " python")
# print(new_group)
#
# groups = [
#     ["a", "a"],
#     ["b", "b"]
# ]
# new_group = []
# for lilgr in groups:
#     new_group.append([student + " python" for student in lilgr])
# print(new_group)
#
# x = [[student + "python" for student in lilgr]
#      for lilgr in groups
#      for _ in list(range(2))
#      ]
#
# print(x)
# print(len(x))
# numbers = [4, 2, 7, 10]
# {num: num ** 2 for num in numbers if num % 2 == 0}
# print({num: num ** 2 for num in numbers if num % 2 == 0})  # dict
# {num: num ** 2 for num in numbers if num % 2 == 0}
# print({num ** 2 for num in numbers if num % 2 == 0})
#
#
# def all_targets_hit_upgrade(attempts: list) -> bool:
#     return True if len(([True for attempt in attempts
#                          if any(attempt) is True])) == len(attempts) else False
#
#
# result = [index for index, value
#           in enumerate(robots) if value['core_version'] <
#           new_version]
#
# robots = [
#     {"core_version": 9},
#     {"core_version": 13},
#     {"core_version": 16},
#     {"core_version": 9},
#     {"core_version": 14},
# ]
#
#
# def get_outdated_robots(robots: list, new_version: int) -> list:
#     result = [key for key, value in enumerate(robots) if value[
#         "core_version"] < new_version]
#
#     return result
#
#
# def get_outdated_robots(robots: list, new_version: int) -> list:
#     return [
#         index
#         for index in range(len(robots))
#         if robots[index]["core_version"] < new_version
#     ]
#
#
# print(get_outdated_robots(robots, 10))
# print(get_outdated_robots(robots, 14))
# print(get_outdated_robots(robots, 8))
# print(get_outdated_robots(robots, 18))
#
#
# def get_outdated_robots(robots: list, new_version: int) -> list:
#     return [key for key, value in enumerate(robots) if value["core_version"] < new_version]
#
#
# def get_outdated_robots(robots: list, new_version: int) -> list:
#     return [index for index, value in enumerate(robots) if value[
#         "core_version"] < new_version]
#
#
# robots = [
#     {"core_version": 9},
#     {"core_version": 13},
#     {"core_version": 16},
#     {"core_version": 9},
#     {"core_version": 14},
# ]
#
# print(get_outdated_robots(robots, 10))
# print(get_outdated_robots(robots, 14))
# print(get_outdated_robots(robots, 8))
# print(get_outdated_robots(robots, 18))
#
#
# def is_prime(num: int) -> bool:
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# def prime_numbers(numbers: list) -> dict:
#     return {key: is_prime(key) for key in numbers}
#
#
# numbers = [19]
# print(prime_numbers(numbers))
#
# numbers = [3, 6, 12, 17]
# print(prime_numbers(numbers))
#
#
# def sum_of_even_numbers(numbers: list) -> int:
#     return sum([num for num in numbers if num % 2 == 0])
#
#
# print(sum_of_even_numbers([]))  # == 0
# print(sum_of_even_numbers([1, 3, 5, 7]))  # == 0
# print(sum_of_even_numbers([2, 11, 2, 4]))  # == 8
# users = [
#     (12, 'Maxim', 'maxim@example.com', 'UBg11eub42hge'),
#     (13, 'Dmitro', 'dmitro@example.com', 'sdTioT36723fw'),
#     (14, 'Roman', 'roman@example.com', 'hbFEkj34NggE2'),
#     (15, 'Ivan', 'ivan@example.com', 'sdTioT36723fw'),
# ]
#
#
# def get_users_data(users: list) -> dict:
#     return {key[0]: {"username": key[1],
#                      "email": key[2],
#                      "password": key[3]}
#             for key in users}
#
#
# print(get_users_data(users))
# get_users_data(users) == {
#     12: {'username': 'Maxim', 'email': 'maxim@example.com', 'password': 'UBg11eub42hge'},
#     13: {'username': 'Dmitro', 'email': 'dmitro@example.com', 'password': 'sdTioT36723fw'},
#     14: {'username': 'Roman', 'email': 'roman@example.com', 'password': 'hbFEkj34NggE2'},
#     15: {'username': 'Ivan', 'email': 'ivan@example.com', 'password': 'sdTioT36723fw'},
# }
#
#
# def even_odd(numbers: list) -> list:
#     return ["even" if num % 2 == 0 else "odd" for num in numbers]
#
#
# even_odd([4])  # == ['even']
# even_odd([145, -24442, 317])  # == ['odd', 'even', 'odd']
#
#
# def average_temperature(months: dict, temperature: int) -> dict:
#     print(
#         {
#
#             key: value for (key, value) in months.items() if value >
#                                                              temperature
#
#         }
#     )
#
#
# months = {'Jun': 18, 'Jul': 23.8, 'Aug': 22.9}
# temperature = 20
# average_temperature(months, temperature)
# == {'Jul': 23.8, 'Aug': 22.9}
#
#
# def group_runs(student_runs: list) -> list:
#     print(
#         [
#             [num[0] for num in student_runs],
#             [num[1] for num in student_runs],
#             [num[2] for num in student_runs],
#             [num[3] for num in student_runs]
#         ]
#
#     )
#
#
# student_runs = [
#     [5.9, 12.8, 26.5, 145.9],  # Перший студент
#     [6.1, 13.2, 30.1, 149],  # Другий студент
#     [6.6, 14.3, 32.3, 152.5]  # Третій студент
# ]
# group_runs(student_runs) == [
#     [5.9, 6.1, 6.6],  # 30 метрів
#     [12.8, 13.2, 14.3],  # 100 метрів
#     [26.5, 30.1, 32.3],  # 200 метрів
#     [145.9, 149, 152.5]  # 400 метрів
# ]
#
#
# def group_runs(student_runs: list) -> list:
#     return [
#         [row[i] for row in student_runs] for i in range(len(student_runs[0]))
#     ]
#
#
# def powerful_cars(brand_cars: list, minimal_hp: int) -> list:
#     result = []
#     for first_list in brand_cars:
#         for each_car in first_list:
#             if each_car["HP"] >= minimal_hp:
#                 result.append([each_car])
#     return result
#     return [[dict for dict in dicts if dict.get("HP") >= minimal_hp] for dicts in brand_cars]
#
#
# brand_cars = [
#     [{'name': 'Ferrari_F430', 'HP': 483},
#      {'name': 'Ferrari_360', 'HP': 395},
#      {'name': 'Ferrari_488', 'HP': 661}],
#
#     [{'name': 'Lamborghini_Aventador', 'HP': 690},
#      {'name': 'Lamborghini_Gallardo', 'HP': 560}]
# ]
# minimal_hp = 661
# print(powerful_cars(brand_cars, minimal_hp))
# [{'name': 'Ferrari_488', 'HP': 661}],
# [{'name': 'Lamborghini_Aventador', 'HP': 690}]
# ]
# #
# a, b, c = 1, 2, 3
# print(a)
# print(type((a, b, c)))
# a, b, c = 1, 2 -!
# a, b, c = "123"
# print(a)
# a, b, c = range(1, 4)
# print(a, b, c)
# my_dict = {"one": 1, "two": 2, "three": 3}
# a, b, c = my_dict  # keys
# print(a, b, c)
# a, b, c = my_dict.values()  # values
# print(a, b, c)
# a, b, c = my_dict.items()  # tuples
# print(a, b, c)
# a, b, c = {"a", "b", "c"}
# print(a, b, c)
# a = "one"
# b = "two"
# print(a, b)
# a, b = b, a
# print(a, b)
# print(("*" * 10))
# * a, b = 1, 2, 3
# print(a, b)
#
# * a, b, c, d = 1, 2, 3
# print(a, b, c, d)
#
# * a, = range(10)
# print(a)
#
#
# def get_dict_k_and_v(dictionary: dict):
#     return dictionary.keys(), dictionary.values()
#
#
# keys, values = get_dict_k_and_v({"a": 1, "b": 2})
# print(keys, values)
#
# arr = ["need", "needed", "yes need it too", "no", "nope", "ty no"]
#
# important, info, for_me, *_ = arr
# print(important, info, for_me)
# print(*_)
# print(type(_))
#
# tuple_ = (1, 2, 3)
# x = (0, *tuple_, 4)
# print(x)
#
# numbers = {"q": 1, "s": 2}
# newdict = {**numbers, "c": 4}
# print(newdict)
# for k in newdict.items():
#     print([k])
#
#
# def unlimited_args(*args):
#     print(type(args))
#     print(args)
#
#
# unlimited_args("S")
#
#
# def unlim_kwargs(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
#
# unlim_kwargs(one=1, two=2, three=3)
#
# list_to_add = [1, 2, 3, 4, 5]
#
#
# def add(required: int, optional: int = 0, *args, **kwargs) -> int:
#     print(required)
#     print(optional)
#     print(args)
#     print(kwargs)
#     return required + optional + sum(args) + sum(kwargs.values())
#
#
# add()
# add(1)
# add(1, 2)
# add(1, 2, 3, 6)
#
# print(add(1, 2, 3, 6, num=10, num2=15))
#
#
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# multiply = lambda a, b: a * b
#
# print(add(10, 5))
# print(multiply(10, 5))
#
# immideately
# invoke
# lambda function
# (lambda a, b: a * b)(10, 5)  # not recommended
#
# operation = add
# print(operation(10, 5))
#
#
# def calc():
#     result = operation(10, 5)
#     return result
#
#
# FUNCNAME(CALLBACK) < - 2
# nd
# func
#
#
# def show(x):
#     print(x)
#
#
# def test(f):
#     f(123)
#
#
# test(show)
#
#
# def test(f):
#     f(123)
#     return f
#
#
# anot_s = test(show)
# anot_s(1)
#
#
# def printer():
#     # local variable
#     s = "Hello world"
#     print(s)
#
#
# s = "hello ?"
# printer()
# print(s)
#
#
# def printer():
#     global s
#     s += " how are you?"
#     print(s)
#
#
# s = "Hello, Dania"
# printer()
#
# a = 1
#
#
# def f():
#     print(a)
#
#
# def g():
#     a = 2
#     print(a)
#
#
# def h():
#     a = 3
#     print(a)
#
#
# f(), g(), h()
# print(a)
#
#
# def print_msg(msg):
#     # outer enclosing function
#     def printer():
#         # nested function
#         print(msg)
#
#     printer()
#
#
# print_msg("Hello")
#
#
# def print_msg(msg):
#     # outer enclosing function
#     def printer():
#         # nested function
#         print(msg)
#
#     return printer
#
#
# another = print_msg("hello")
# print(type(another))
# another()
#
#
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#
#     return multiplier
#
#
# times3 = make_multiplier_of(3)
# times5 = make_multiplier_of(5)
#
# print(type(times3))
#
# print(times3(9))
# print(times5(3))
# print(times5(times3(2)))
#
#
# def produce(device_name: str):
#     count = 0
#
#     def device():
#         nonlocal count
#         count += 1
#         print(f"{device_name} launch {count} times")
#
#     return device
#
#
# cell_phone = produce("Cell Phone")
# laptop = produce("Laptop")
# laptop()  # 1
#
# cell_phone()  # 1
# laptop()
# laptop()
#
#
# def get_average_mark(name: str, *args: int) -> str:
#     return (f"{name} got {round(sum(args) / len(args))}")
#
#
# get_average_mark("Danylo", 11) == "Danylo got 11"
# get_average_mark("Oleksii", 12, 10, 11, 11, 11) == "Oleksii got 11"
# get_average_mark("Ivan", 10, 11, 12, 9, 12, 12) == "Ivan got 11"
#
#
# def new_number(number: int) -> None:
#     print(f"Received a new number: {number}")
#
#
# def is_positive(number: int) -> None:
#     if number > 0:
#         print(f"{number} is a positive number")
#     else:
#         print(f"Zero" if number == 0 else f"{number} is a negative number")
#
#
# def print_bye(number: int) -> None:
#     print("Bye!")
#
#
# def numbers_handler(numbers: list, before=0, action=0, after=0) -> None:
#     pass
#
#
# def print_hello(number):
#     print("Hello!")
#
#
# def some_action(number):
#     print("Action!")
#
#
# numbers_handler([10], action=some_action, before=print_hello)
#
#
# def f_123(list, num, f_1, f_2, f_3):
#     print(list)
#     print(num)
#     print(f_1)
#     print(f_2)
#     print(f_3)
#
#
# f_123([123], 777, f_1(), f_2(), f_3())
#
# from typing import Callable
#
#
# def new_number(number: int) -> None:
#     print(f"Received a new number: {number}")
#     return f"Received a new number: {number}"
#
#
# def is_positive(number: int) -> None:
#     if number > 0:
#         print(f"{number} is a positive number")
#         return f"{number} is a positive number"
#     if number == 0:
#         print("Zero")
#         return "Zero"
#     else:
#         print(f"{number} is a negative number")
#         return f"{number} is a negative number"
#
#
# def print_bye(number: int) -> None:
#     print("Bye!")
#     return "Bye!"
#
#
# def numbers_handler(
#         numbers: list,
#         before: Callable = new_number,
#         action: Callable = is_positive,
#         after: Callable = print_bye
# ) -> None:
#     for arg in numbers:
#         before(arg)
#         action(arg)
#         after(arg)
#
#
# numbers_handler([1, 0])
#
#
# def message_people(people: list):
#     # print(people)
#     def print_message(message: str):
#         # print(people)
#         # print(message)
#         return print_message
#
#
# message_people(["Jo", "Boris", "Rakal"])("test string")
#
#
# def make(label):
#     def echo(message):
#         print(label + ':' + message)
#
#     return echo
#
#
# make('label')('message')
#
#
# def message_people(people: list) -> callable:
#     def print_message(message: str) -> None:
#         peoples = ", ".join(people)
#         if message == "hello":
#             print(f"Hello, {peoples}, nice to see you!")
#         if message == "meeting":
#             print(f"{peoples}, we have a meeting in an hour, don't be late!")
#         if message == "bye":
#             print(f"Bye {peoples}, see you tomorrow!")
#
#     return print_message
#
#
# mes_people = message_people(["Alex", "Robert", "Tom"])
# mes_people('hello')
# mes_people('meeting')
# mes_people('bye')
#
#
# @decorators
#
#
# user = "admin"
#
#
# def admin_required(action):
#     pass
#
#
# @admin_required
# def post_article(text: str) -> None:
#     print(f"Article \"{text}\" was posted")
#
#
# def post_release(text: str) -> None:
#     print(f"Release \"{text}\" was posted")
#
#
# post_article("Hello world")
# post_release("Hi")
#
#
# def first(msg):
#     print(msg)
#
#
# first("hello")
# second = first
# second("Hello")
#
#
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# def operation(func, x):
#     result = func(x)
#     return result
#
#
# print(operation(inc, 10))
# print(operation(dec, 10))
#
#
# def make_multiplier_of(multiplier: int):
#     def multiply(num: int):
#         return multiplier * num
#
#     return multiply
#
#
# times3 = make_multiplier_of(3)
# print(times3(7))
#
#
# def decorate(func):
#     def inner():
#         print("Decorated before")
#         func()
#         print("Decorated adter")
#
#     return inner
#
#
# @decorate
# def printer():
#     print("Hello")
#
#
# printer()
#
#
# @decorate  # def printer(): print("Hello // printer = decorate(printer)
# def printer(_: str):
#     print("Hello")
#
#
# def main_f(mplier: int):
#     def make_x_some(num: int):
#         return mplier * num
#
#     return make_x_some
#
#
# test_x10 = main_f(10)
# print(test_x10(10))
#
# import time
#
#
# def timer(func):
#     def inner_func(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Time required to complete: {end_time - start_time}")
#         return result
#
#     return inner_func
#
#
# @timer
# def test_function():
#     return sum(range(50_000_000))
#
#
# @timer
# def long_test_function(num_of_iterations):
#     return sum(range(num_of_iterations))
#
#
# test_function()
# long_test_function(num_of_iterations=90_000_000)
# long_test_function(90_000_000)
#
# from functools import wraps
# from typing import Callable, Any
#
#
# def bread(func: Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args, **kwargs) -> Any:
#         print("</--------\\>")
#         func(*args, **kwargs)
#         print("<\\________/>")
#
#     return wrapper
#
#
# def ingredients(func: Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args, **kwargs) -> Any:
#         print(" #tomatoes#")
#         func(*args, **kwargs)
#         print("   ~salad~")
#
#     return wrapper
#
#
# @bread
# @ingredients
# def sandwich() -> Any:
#     print("   --ham--")
#
#
# from typing import Callable
#
#
# def admin_required(func: Callable) -> None:
#     def inner_f(user: dict) -> None:
#         if user["is_admin"]:
#             print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")
#         else:
#             print("You are not allowed to see this information!")
#
#     return inner_f
#
#
# @admin_required
# def send_secure_information(user: dict) -> None:
#     print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")
#
#
# send_secure_information({'name': 'Administrator', 'is_admin': True})
# send_secure_information({'name': 'User1234', 'is_admin': False})
#
# from typing import Callable
#
#
# def only_admin(func: Callable) -> None:
#     def wrapper(users: list) -> None:
#         admins = [user for user in users if user.get("is_admin") is True]
#         func(admins)
#
#     return wrapper
#
#
# @only_admin
# def create_permissions(users: list) -> None:
#     for user in users:
#         print(f'Creating permissions for {user["username"]}')
#
#
# users = [{'is_admin': False, 'username': 'user'}, {'is_admin': False, 'username': 'user2'},
#          {'is_admin': 'True', 'username': 'user123'}]
#
# create_permissions(users)
#
#
# def html_tag(tag: str) -> None:
#     def tag_d(func: Callable) -> None:
#         def wrapper(*args, **kwargs) -> None:
#             value = f"<{tag}>{func(*args)}</{tag}>"
#             print(value)
#             return value
#
#         return wrapper
#
#     return tag_d
#
#
# from typing import Callable
#
#
# def number_filter(func: Callable) -> None:
#     global result
#     result = []
#
#     def num_only(*args, **kwargs) -> None:
#         numbers = [(round(float(num)) for num in items if
#                     type(num) == int or
#                     type(num) == float)]
#         result = numbers
#         return result
#
#     return num_only
#
#
# def round_dict(func: Callable) -> None:
#     global result
#
#     def list_to_round_dict(*args, **kwargs) -> None:
#         rounded_dict = {num: num * 2 for num in
#                         (int(round(float(num)))
#                          for num in items if
#                          type(num) == int or
#                          type(num) == float)}
#         result = rounded_dict
#         return result
#
#     return list_to_round_dict
#
#
# def arrow(func: Callable) -> None:
#     global result
#
#     def dict_to_list(*args, **kwargs) -> None:
#         arrow_from_dict = f"s"
#         result = [f"{key} -> {value}" for key, value in {num: num * 2 for num in
#                                                          (int(round(float(num)))
#                                                           for num in items if
#                                                           type(num) == int or
#                                                           type(num) == float)}]
#         like_numbers(result)
#
#     return dict_to_list
#
#
# items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]
#
#
# @arrow
# @round_dict
# @number_filter
# def like_numbers(items: list):
#     return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"
#
#
# like_numbers(items)
# == "I like to filter, rounding, doubling, "
# "store and decorate numbers: "
# "2 -> 4, 4 -> 8, 9 -> 18, -123 -> -246!"
#
# #########################################
# from typing import Callable
#
#
# def number_filter(func: Callable) -> None:
#     global result
#     result = []
#
#
# def num_only(*args, **kwargs) -> None:
#     numbers = [(round(float(num)) for num in items if
#                 type(num) == int or
#                 type(num) == float)]
#     result = numbers
#     return result
#
#
# return num_only
#
#
# def round_dict(func: Callable) -> None:
#     global result
#
#     def list_to_round_dict(*args, **kwargs) -> None:
#         rounded_dict = {num: num * 2 for num in
#                         (int(round(float(num)))
#                          for num in items if
#                          type(num) == int or
#                          type(num) == float)}
#         result = rounded_dict
#         return result
#
#     return list_to_round_dict
#
#
# def arrow(func: Callable) -> None:
#     global result
#
#     def dict_to_list(*args, **kwargs) -> None:
#         arrow_from_dict = f"s"
#         result = [f"{key} -> {value}" for key, value in {num: num * 2 for num in
#                                                          (int(round(float(num)))
#                                                           for num in items if
#                                                           type(num) == int or
#                                                           type(num) == float)}]
#         like_numbers(result)
#
#     return dict_to_list
#
#
# items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]
#
#
# @arrow
# @round_dict
# @number_filter
# def like_numbers(items: list):
#     return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"
#
#
# like_numbers(items)
#
#
# def arrow(func):
#     # write your code here
#     pass
#
#
# def number_filter(func):
#     # write your code here
#     pass
#
#
# def round_dict(func):
#     # write your code here
#     pass
#
#
# Decorate
# this
# function
# with 3 decorators above in a correct order
#
#
# def like_numbers(items: list):
#     return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"
#
#
# def like_numbers(items: list):
#     return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"
#
#
# print(like_numbers(items=['2 -> 4', '4 -> 8', '9 -> 18', '-123 -> -246']))
#
# items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]
#
#
# def number_filter(func):
#     def wrapper(*args, **kwargs):
#         numbers = [round(float(num)) for num in items if type(num) == int or type(num) == float]
#         # print(f"1-st deco: {numbers}")
#         return numbers
#
#     return wrapper
#
#
# def round_dict(func):  # round numbers to {num : num*2} # 2
#
#     def round_num_to_dict(*args, **kwargs):
#         # result = number_filter(func)(*args,**kwargs)
#         rounded_dict = {num: num * 2 for num in
#                         number_filter(func)(*args, **kwargs)
#                         if type(num) == int or type(num) == float}
#         # print(f"2-nd deco: {rounded_dict}")
#         return rounded_dict
#
#     return round_num_to_dict
#
#
# def arrow(func):  # dict -> ["key -> value", "key2 -> value2"] #3
#
#     def dict_to_list_of_strings(*args, **kwargs):
#         list_with_strings = []
#         tempo_str = ""
#         for num, value in round_dict(func)(*args, **kwargs).items():
#             tempo_str += str(num) + " -> " + str(value)
#             list_with_strings.append(tempo_str)
#             tempo_str = ""
#         # print(f"3-th deco: {list_with_strings}")
#         items = list_with_strings
#         func(list_with_strings)
#         return list_with_strings
#
#     return dict_to_list_of_strings
#
#
# @arrow
# @round_dict
# @number_filter
# def like_numbers(items: list):
#     return f"I like to filter, rounding, doubling, store and decorate numbers: " \
#            f"{', '.join(items)}!"
#
#
# like_numbers(items)
# == "I like to filter, rounding, doubling, "
# "store and decorate numbers: "
# "2 -> 4, 4 -> 8, 9 -> 18, -123 -> -246!"
#
#
# def arrow(func):
#     def wrapper(items):
#         new_items = [f"{key} -> {value}" for key, value in items.items()]
#         return func(new_items)
#
#     return wrapper
#
#
# def round_dict(func):
#     def wrapper(items):
#         new_items = {round(item): round(item) * 2 for item in items}
#         return func(new_items)
#
#     return wrapper
#
#
# def number_filter(func):
#     def wrapper(items):
#         new_items = [item for item in items if isinstance(item, (int, float))]
#         return func(new_items)
#
#     return wrapper
#
#
# @number_filter
# @round_dict
# @arrow
# def like_numbers(items: list) -> str:
#     return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"
#
#
# items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]
# print(like_numbers(items))
#
# from typing import Callable
#
#
# def arrow(func: Callable) -> None:
#     def wrapper(items: dict) -> None:
#         new_format_items = [f"{key} -> {value}" for key, value in items.items()]
#         return func(new_format_items)
#
#     return wrapper
#
#
# def number_filter(func: Callable) -> None:
#     def wrapper(items: list) -> None:
#         new_format_items = [num for num in items if isinstance(num, (int, float))]
#         return func(new_format_items)
#
#     return wrapper
#
#
# def round_dict(func: Callable) -> None:
#     def wrapper(items: list) -> None:
#         new_format_items = {round(item): round(item) * 2 for item in items}
#         return func(new_format_items)
#
#     return wrapper
#
#
# @number_filter
# @round_dict
# @arrow
# def like_numbers(items: list) -> str:
#     return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"
#
#
# items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]
# print(like_numbers(items))
#
# CLASSES < ---------------------------
#
#
# class User:  # PascalCase
#     pass
#
#
# class_object = User()
#
# print(type(User))
# print(type(class_object))
#
# class_object.name = "John"
# class_object.age = 25
#
# class_object_2 = User()
# class_object_2.name = "Ted"
# class_object_2.age = 30
#
#
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def print_ifo(self):
#         print(f"Name = {self.name}, Age = {self.age}")
#
#
# user1 = User(name="john", age=27)
# user2 = User(name="Ted", age=54)
#
# print(user1.age)
#
# user1.age = 567
#
# print(user1.age)
#
# user1.x = 1234
# print(user1.x)
#
# user2 = user1
# print(user2.x)
#
#
# class Friend:
#     def __init__(self, name: str):
#         self.name = name
#
#
# friend = Friend(name="john")
# guest = friend
# guest.name = "Sherlock"
# guest = None
# print(friend.name)
#
#
# class Person:
#     pass
#
#
# petia = Person()
# petia.name = "Petia"
# petia.last_name = "Smith"
# petia.wife = None
#
# tania = Person()
# tania.name = "Tania"
# tania.last_name = "Black"
# tania.husband = None
#
# petia.wife = tania
# tania.husband = petia
#
# petia.wife = Person()
#
# petia.wife.last_name = petia.last_name
# petia.wife = tania
# petia.wife.last_name = petia.last_name
# print(tania.husband.name)
# print(tania.last_name)
#
#
# class User:
#     pass
#
#
# def func(user):
#     pass
#
#
# user = User()
# print(type(User))
# print(type(user))
# print(type(func))
# print(type(10))
# print(type(int))
#
# print(type(type))
#
#
# class Robot:
#     def __init__(self, name: str):
#         self.name = name
#         self.partner = None
#
#
# def pair_robots(robots: list) -> tuple:
#     robot_0 = Robot(name=robots[0])
#     robot_1 = Robot(name=robots[1])
#     robot_0.partner = robot_1
#     robot_1.partner = robot_0
#     return (robot_0, robot_1)
#
#
# robots = [
#     'Alex',
#     'Tom'
# ]
#
# new_robots = pair_robots(robots)
# print(new_robots[0].name == 'Alex')
#
# print(all([isinstance(robot, Robot)
#            for robot in new_robots]))
#
# print(new_robots[0].partner is new_robots[1])
# print(new_robots[0].partner is new_robots[0])
#
#
# class Robot:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.partner = None
#
#
# def pair_robots(robots: list) -> tuple:
#     robot_0 = Robot(name=robots[0])
#     robot_1 = Robot(name=robots[1])
#     robot_0.partner = robot_1
#     robot_1.partner = robot_0
#     return (robot_0, robot_1)
#
#
# class Robot:
#     def __init__(self, model: str, constructor: str, serial_no: int) -> None:
#         self.model = model
#         self.constructor = constructor
#         self.serial_no = serial_no
#
#
# def copy_robot(robot: Robot) -> Robot:
#     new_robot = Robot(robot.model, robot.constructor, robot.serial_no + 1)
#     return new_robot
#
#
# robot = Robot('g135', 'Alex', 1664)
# copy_robot(robot)
# print(robot.model, robot.constructor, robot.serial_no)
#
#
# class Robot:
#     def __init__(self, wheels: int, gears: int, pistons: int) -> None:
#         self.wheels = wheels
#         self.gears = gears
#         self.pistons = pistons
#
#
# def robots_parts(robots: list) -> dict:
#     result = {"wheels": 0, "gears": 0, "pistons": 0}
#     for robot in robots:
#         result["wheels"] += robot.wheels
#         result["gears"] += robot.gears
#         result["pistons"] += robot.pistons
#     return result
#
#
# robots = [
#     Robot(wheels=10, gears=18, pistons=16),
#     Robot(wheels=4, gears=8, pistons=8),
#     Robot(wheels=22, gears=17, pistons=30),
# ]
# robots_parts(robots)
#
#
# class Matrix:
#     def __init__(self, matrix: list) -> None:
#         self.matrix = matrix
#         for row in self.matrix:
#             if len(row) != len(self.matrix):
#                 return None
#
#     def get_diagonal(self) -> list:
#         if len(self.matrix) == 0:
#             return []
#         diagonal = []
#         current_index = 0
#         for row in self.matrix:
#             diagonal.append(row[current_index])
#             current_index += 1
#         return diagonal
#
#     def get_counter_diagonal(self) -> list:
#         if len(self.matrix) == 0:
#             return []
#         counter_diagonal = []
#         current_index = 0
#         for row in self.matrix:
#             counter_diagonal.append(row[::-1][current_index])
#             current_index += 1
#         return counter_diagonal
#
#     def rotate_rows(self, number: int) -> list:
#         if len(self.matrix) == 0:
#             return []
#         if number % len(self.matrix[0]) == 0:
#             return self.matrix
#         for num in range(number):
#             self.matrix.append(self.matrix[0])
#             self.matrix.pop(0)
#         return self.matrix
#
#     def rotate_columns(self, number: int) -> list:
#         if len(self.matrix) == 0:
#             return []
#         if number % len(self.matrix[0]) == 0:
#             return self.matrix
#         for num in range(number):
#             for row in self.matrix:
#                 row.append(row[0])
#                 row.pop(0)
#         return self.matrix
#
#
# matrix_inst = Matrix([
#     [4, 5, 6],
#     [7, 8, 9],
#     [1, 2, 3]
# ])
# print(matrix_inst.get_diagonal())  # [1, 5, 9]
# matrix_inst.get_counter_diagonal()  # [3, 5, 7]
#
# print(matrix_inst.rotate_rows(5))
# matrix_inst.matrix == [
#     [4, 5, 6],
#     [7, 8, 9],
#     [1, 2, 3]
# ]
#
# matrix_inst.matrix == [
#     [5, 6, 4],
#     [8, 9, 7],
#     [2, 3, 1]
# ]
#
#
# class Car:
#     def __init__(self,
#                  comfort_class: int = 7,
#                  clean_mark: int = 1,
#                  brand: str = "Unknown"
#                  ) -> None:
#         self.comfort_class = comfort_class
#         self.clean_mark = clean_mark
#         self.brand = brand
#
#
# class CarWashStation:
#     def __init__(self,
#                  distance_from_city_center: float = 1,
#                  clean_power: float or int = 10,
#                  average_rating: float = 5,
#                  count_of_ratings: int = 1
#                  ) -> None:
#         self.distance_from_city_center = distance_from_city_center
#         self.clean_power = clean_power
#         self.average_rating = average_rating
#         self.count_of_ratings = count_of_ratings
#
#     def serve_cars(self, cars: list[Car]) -> float:
#         income = 0
#         cars_to_wash = [car for car in cars if car.clean_mark < self.clean_power]
#         for car in cars_to_wash:
#             income += self.calculate_washing_price(car)
#             self.wash_single_car(car)
#         return round(income, 1)
#
#     def calculate_washing_price(self, car: Car) -> float:
#         washing_price = (
#                 car.comfort_class *
#                 (self.clean_power - car.clean_mark) *
#                 (self.average_rating / self.distance_from_city_center)
#         )
#         return round(washing_price, 1)
#
#     def wash_single_car(self, single_car: Car) -> None:
#         if single_car.clean_mark < self.clean_power:
#             single_car.clean_mark = self.clean_power
#         return None
#
#     def rate_service(self, score: int) -> None:
#         self.average_rating = (
#                 (self.average_rating * self.count_of_ratings + score) /
#                 (self.count_of_ratings + 1)
#         )
#         self.count_of_ratings += 1
#         self.average_rating = round(self.average_rating, 1)
#         return None
#
#
# class Car:
#     def __init__(self,
#                  comfort_class: int = 7,
#                  clean_mark: int = 1,
#                  brand: str = "Unknown"
#                  ) -> None:
#         self.comfort_class = comfort_class
#         self.clean_mark = clean_mark
#         self.brand = brand
#
#
# class CarWashStation:
#     def __init__(self,
#                  distance_from_city_center: float = 1,
#                  clean_power: float or int = 10,
#                  average_rating: float = 5,
#                  count_of_ratings: int = 1
#                  ) -> None:
#         self.distance_from_city_center = distance_from_city_center
#         self.clean_power = clean_power
#         self.average_rating = average_rating
#         self.count_of_ratings = count_of_ratings
#
#     def serve_cars(self, cars: list[Car]) -> float:
#         income = 0
#         cars_to_wash = [car for car in cars
#                         if car.clean_mark < self.clean_power]
#         for car in cars_to_wash:
#             income += self.calculate_washing_price(car)
#             self.wash_single_car(car)
#         return round(income, 1)
#
#     def calculate_washing_price(self, car: Car) -> float:
#         price = (car.comfort_class * (self.clean_power - car.clean_mark)
#                  * (self.average_rating / self.distance_from_city_center))
#         return round(price, 1)
#
#     def wash_single_car(self, single_car: Car) -> None:
#         if single_car.clean_mark < self.clean_power:
#             single_car.clean_mark = self.clean_power
#
#     def rate_service(self, score: int) -> None:
#         self.average_rating = ((self.average_rating * self.count_of_ratings
#                                 + score) / (self.count_of_ratings + 1))
#         self.count_of_ratings += 1
#         self.average_rating = round(self.average_rating, 1)
#
#
# Instance and
#
#
# class attributes
#
#
#     class Dog:
#         # атрибут класса
#         animal = "dog"
#
#         def __init__(self, breed: str, color: str):  # атрибут экземпляра
#             # instance attribute
#             self.breed = breed
#             self.color = color
#
#         def bark(self):
#             print(f"dog {self.color} {self.breed} barks")
#
#
# hatiko = Dog("Akita", "brown")
# buzo = Dog("Bulldog", "black")
# print(hatiko.breed)
# print(hatiko.color)
# print(hatiko.animal)
# print(Dog.animal)
# print(hatiko.__class__)
# print(hatiko.__dict__)
# print(Dog.__dict__)
# Dog.animal = "cat"
# print(hatiko.animal)
# print(buzo.animal)
# Dog.animal = "dog"
# hatiko.animal = "cat"
# print(hatiko.animal)
# print(buzo.animal)
#
# hatiko = Dog("Akita", "brown")
# buzo = Dog("Bulldog", "black")
# hatiko.bark()
# buzo.bark()
# Dog.bark(hatiko)
#
#
# class Citizen:
#     city = "Springfield"
#
#     def __init__(self, full_name: str):
#         self.full_name = full_name
#
#     @classmethod
#     def change_city_name(cls, new_name: str):
#         cls.city = new_name
#
#
# mayor = Citizen("Joe Quimby")
# homer = Citizen("Homer Simpson")
#
# print(mayor.full_name)
# print(mayor.city)
# mayor.change_city_name("Tokyo")
#
# print(mayor.city)
# print(homer.city)
# print(mayor.__dict__)
# print(homer.__dict__)
# print(Citizen.__dict__)
#
# staticmethod
#
#
# class Car:
#     def __init__(self, max_speed_km: int):
#         self.max_speed_km = max_speed_km
#
#     def print_max_speed_km(self):
#         print(f"Car's max speed is {self.max_speed_km} km/h")
#
#     def print_max_speed_miles(self):
#         print(f"Car's max speed is {self.km_to_miles(self.max_speed_km)} miles/h")
#
#     @staticmethod
#     def km_to_miles(km):
#         # 1 km = 0.62137119 miles
#         return round(km * 0.62137119, 2)
#
#
# tesla_roadster = Car(max_speed_km=400)
# tesla_roadster.print_max_speed_miles()
# tesla_roadster.print_max_speed_km()
#
#
# class Grow:
#     def __init__(self, stem_diff: float = 0.0, leaf_diff: float = 0.0):
#         self.stem_diff = stem_diff
#         self.leaf_diff = leaf_diff
#
#     def __add__(self, other):
#         if not isinstance(other, Grow):
#             raise TypeError(f"Grow + {type(other)}")
#         return Grow(
#             stem_diff=self.stem_diff + other.stem_diff,
#             leaf_diff=self.leaf_diff + other.leaf_diff
#         )
#
#     def __repr__(self):
#         return f"Grow(stem_diff = {self.stem_diff}, leaf_diff = {self.leaf_diff}"
#
#     # def __str__(self):
#     #     return repr(self)
#
#
# day_1 = Grow(stem_diff=2.5)
# day_2 = Grow(stem_diff=2.0)
# day_3 = Grow(stem_diff=1.0, leaf_diff=1.5)
# day_4 = Grow(stem_diff=0.8, leaf_diff=1.2)
#
# plant
# plant = day_1.add(day_2).add(day_3).add(day_4)
# print(plant)
# print(plant.stem_diff)
# print(plant.leaf_diff)
#
# plant = day_1 + day_2 + day_3 + day_4
# print(plant.stem_diff)
# print(plant.leaf_diff)
# y = day_1 + 5
# print(y)
# print(dir(Grow))
#
# print((day_1 + day_2))
# import math
#
#
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         return Complex(
#             real=self.real + other.real,
#             imag=self.imag + other.imag
#         )
#
#     def __sub__(self, other):
#         return Complex(
#             real=self.real - other.real,
#             imag=self.imag - other.imag
#         )
#
#     def __mul__(self, other):
#         return Complex(
#             # ac - bd
#             real=self.real * other.real - self.imag * other.imag,
#             # bc + ad
#             imag=self.imag * other.real + self.real * other.imag
#         )
#
#     def __repr__(self):
#         return f"real: {self.real}, " \
#                f"imag: {self.imag}"
#
#     def __str__(self):
#         return f"{self.real} + {self.imag}i"
#
#     def __eq__(self, other):
#         return self.real == other.real and self.imag == other.imag
#
#
# first = Complex(1, 2)
# second = Complex(-2, 3)
# first + second
# print(str(first + second))
# print(str(first - second))
# print(str(first * second))
# print(str(first * 5))
# print(dir(5))
# a = 5
# print(a.real)
# print(a.imag)
#
# print(first == second)
# third = Complex(1, 2)
# print(first == third)
#
# print(math.sqrt(
#     math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(
#         math.sqrt(
#             math.sqrt(
#                 0.207878957)))))))))))))
#
# if __name__ == "__main__":
#     pass
#
# annotations
# from __future__ import annotations
#
#
# class Age:
#     def __init__(self, value: int) -> None:
#         self.value = value
#
#     def __add__(self, other: Age | int):
#         if isinstance(other, Age):
#             return Age(self.value + other.value)
#
#         return Age(self.value + other)
#
#     def __str__(self) -> str:
#         return f"Age: {self.value}"
#
#
# if __name__ == "__main__":
#     print(Age(25) + Age(13))
#     print(Age(25) + 10)
#     print(Age(25) + "12345")
#
# test
#
#
# class Magic:
#     def __init__(self):
#         print("Hello, I'm magic method!")
#
#
# print(dir(Magic))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', … ]

# class Magic:
#     def __init__(self):
#         print("Hello, I'm magic method!")
#
#
# print(dir(Magic)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', … ]
#
# x = 10
# y = x.__add__(5)
# print(y)

#
# class Employee: #the __new__() method is called before the __init__() method.
#     def __init__(self):
#         print ("__init__ magic method is called")
#         self.name='Satya'
#
#     def __new__(cls):
#         print ("__new__ magic method is called")
#         inst = object.__new__(cls)
#         return inst
#
#
#
# vas = Employee()
# print(vas.name)
# x = -122
# print(x.__trunc__(self))
#
# class User:
#     def __init__(self, name: str, surname: str):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#
# user = User("Joseph", "Farrell")
#
# print(user) # Joseph Farrell


# class TestClass:
#     test_atr = "1"
#
#     def __init__(self, name):
#         self.name = name
#
#
# tester1 = TestClass("John")
#
# tester2 = TestClass("Bob")
#
# tester1.test_atr = "3"
# TestClass.test_atr = "2"
# print(tester1.test_atr)
# print(tester2.test_atr)


# class Student:
#     academy = "Mate academy"  # class attribute #  All the instances of the class will share them
#
#     def __init__(self, name: str, course: str):
#         self.name = name  # instance attribute
#         self.course = course  # instance attribute
#
#     @classmethod  # The class method can be called both by the class and its object
#     def class_method(
#             cls):  # class method that accepts a single parameter cls and not self that we usually accept
#         pass
#
#     class Car:
#         @staticmethod  # A static method is also a method that is bound to the class and not the object of the class
#         # This method can’t access or modify the class state
#         # It is present in a class because it makes sense for the method to be present in class.
#         # The static method can be called both by the class and its object as well:
#         def miles_to_km(miles: int):
#             print(round(miles * 1.61, 2))
#
#
# fe_student = Student("Joseph", "Frontend")
# py_student = Student("John", "Python")
#
# print(fe_student.name)  # Joseph
# print(py_student.name)  # John


# from __future__ import annotations
#
#
# class RockBand:
#     def __init__(self, name: str, members: list) -> None:
#         self.name = name
#         self.members = members
#
#     def add_new_member(self, new_member: str) -> None:
#         if new_member in self.members:
#             print(f"{new_member} is already in the band!")
#         else:
#             self.members.append(new_member)
#
#     def __add__(self, other: RockBand) -> RockBand:
#         return RockBand(
#             f"{self.name} {other.name} United",
#             list(set(self.members + other.members))
#         )
#
#
# the_beatles = RockBand(
#     "The Beatles",
#     ["John Lennon", "Paul McCartney", "George Harrison"]
# )
# first_band = RockBand("First", ["Ivan", "Sergey"])
# second_band = RockBand("Second", ["Sergey", "Max"])
# united = first_band + second_band
# print(united.name, united.members)  # "First Second United" ["Ivan", "Sergey", "Max"]

# import math
#
#
# class Point:
#     points = []
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.points.append(self)
#
#     def distance_to_origin(self):
#         return round(math.dist([self.x, self.y],
#                                [0, 0]), 2)
#
#     def distance_to_point(self, point):
#         return round(math.dist([self.x, self.y],
#                                [point.x, point.y]), 2)
#
#     def distance_to_x_axis(self):
#         return abs(self.y)
#
#     def distance_to_y_axis(self):
#         return abs(self.x)
#
#     def find_closest_point(self):
#         closest_point = None
#         min_distance = None
#         for point in self.points:
#             if point != self:
#                 if min_distance is None:
#                     min_distance = self.distance_to_point(point)
#                     closest_point = point
#                     if self.distance_to_point(point) < min_distance:
#                         min_distance = self.distance_to_point(point)
#                         closest_point = point
#         return closest_point

# import math
#
#
# class Point:
#     points = []
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.points.append(self)
#
#     def distance_to_origin(self):
#         return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)
#
#     def distance_to_point(self, point):
#         return round(math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2), 2)
#
#     def distance_to_x_axis(self):
#         return round(abs(self.y), 2)
#
#     def distance_to_y_axis(self):
#         return round(abs(self.x), 2)
#
#     def find_closest_point(self):
#         closest_distance = float('inf')
#         closest_point = None
#         for point in Point.points:
#             if point != self:
#                 distance = self.distance_to_point(point)
#                 if distance < closest_distance:
#                     closest_distance = distance
#                     closest_point = point
#         return closest_point
#
#
#
#
#
#
#
#
#
#
#
# from __future__ import annotations
#
#
# class Point:
#     points = []
#
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#         self.__class__.points.append(self)
#
#     def distance_to_origin(self) -> float:
#         return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)
#
#     def distance_to_point(self, point: Point) -> float:
#         return round(
#             ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2
#         )
#
#     def distance_to_x_axis(self) -> int:
#         return abs(self.y)
#
#     def distance_to_y_axis(self) -> int:
#         return abs(self.x)
#
#     def find_closest_point(self) -> Point:
#         closest_point = None
#         closest_distance = None
#         for point in self.__class__.points:
#             if point is not self:
#                 if closest_distance is None:
#                     closest_distance = self.distance_to_point(point)
#                     closest_point = point
#                 elif self.distance_to_point(point) < closest_distance:
#                     closest_distance = self.distance_to_point(point)
#                     closest_point = point
#         return closest_point


# import math
#
#
# class Point:
#     points = []
#
#     def __init__(self, x: float, y: float) -> None:
#         self.x = x
#         self.y = y
#         Point.points.append(self)
#
#     def distance_to_origin(self) -> None:
#         return round(math.dist([self.x, self.y],
#                                [0, 0]), 2)
#
#     def distance_to_point(self, point: list) -> None:
#         return round(math.dist([self.x, self.y],
#                                [point.x, point.y]), 2)
#
#     def distance_to_x_axis(self) -> None:
#         return abs(self.y)
#
#     def distance_to_y_axis(self) -> None:
#         return abs(self.x)
#
#     def find_closest_point(self) -> None:
#         closest_distance = float("inf")
#         closest_point = None
#         for point in Point.points:
#             if point != self:
#                 distance = self.distance_to_point(point)
#                 if distance < closest_distance:
#                     closest_distance = distance
#                     closest_point = point
#         return closest_point
#########################################

# students = {"Al1":1,"Al2":2,"Al3":3,"Al4":4}
# students = ["Al1", "Al2", "Al3", "Al4", ]
# students = "1234"
# for student in students:
#     print(student)

# iterator = iter(students)
# print(iterator)
# print(iterator.__iter__())
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(iterator.__next__())
# print(iterator.__next__()) #StopIteration err
#
# iterable = students
# iterator = iter(iterable)
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         print("error occured")
#         break

# ITERATOR
# students = ["Al1", "Al2", "Al3", "Al4", "Al5"]
#
#
# class EachSecondElement:
#     def __init__(self, elements):
#         self.elements = elements
#
#     def __iter__(self):
#         self.current_element = 1
#         return self
#
#     def __next__(self):
#         # if self.current_element >= len(self.elements):
#         #     raise StopIteration
#
#         result = self.elements[self.current_element]
#         self.current_element += 2
#         self.current_element %= len(self.elements)
#         return result
#
#
# each_second_person = EachSecondElement(students)
# iterator = iter(each_second_person)
# print(next(iterator))
# print(next(iterator))


# for student in EachSecondElement(students):
#     print(student)
#
#
# for word in EachSecondElement("Hello, world!"):
#     print(word)


# print(type(iterator))


# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# gen = simple_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# GENERATOR
# def add_substract_multiply_divide(num: int):
#     start = 10
#     after_addition = start + num
#     print(type(after_addition))
#     yield after_addition
#
#     after_substraction = after_addition - num
#     yield after_substraction
#
#     after_multiplication = after_substraction * num
#     yield after_multiplication
#
#     after_division = after_multiplication / num
#     yield after_division
#
#
# operations_with_5 = add_substract_multiply_divide(5)
# print(next(operations_with_5))
# print(next(operations_with_5))
# print(next(operations_with_5))
# print(next(operations_with_5))
# #print(next(operations_with_5)) # stopiteration error
#
# operations_with_7 = add_substract_multiply_divide(7)
# print(next(operations_with_7))
# print(next(operations_with_7))
# print(next(operations_with_7))
# print(next(operations_with_7))
# #print(next(operations_with_7)) # stopiteration error
#
# test = add_substract_multiply_divide(3)
#
# for elem in test: # for elem in add_substract_multiply_divide(3)
#     print(elem)
# students = ["Al1", "Al2", "Al3", "Al4", "Al45" ]
#
#
# class EachSecondElement:
#     def __init__(self, elements):
#         self.elements = elements
#
#     def __iter__(self):
#         self.current_element = 1
#         return self
#
#     def __next__(self):
#         if self.current_element >= len(self.elements):
#             raise StopIteration
#
#         result = self.elements[self.current_element]
#         self.current_element += 2
#         return result
#
#
# def each_second_element(elements):
#     current_element = 1
#     while current_element < len(elements):
#         yield  elements[current_element]
#         current_element += 2
#
# for elem in EachSecondElement(students):
#     print(elem)
# for elem in each_second_element(students):
#     print(elem)
#
# each_second_element_obj = EachSecondElement(students)
# iterator = iter(each_second_element_obj)
# print(next(iterator))
#
# #print(next(it)) # error
#
# gen = each_second_element(students)
# print(next(gen))
# print(next(gen))
# print(next(gen)) # error
# print(next(iterator))
# print(next(iterator)) # error


# range is not iterator
# range is not generator
# range = iterable

# test = {"q","w","e"}
# test = frozenset(test)
# print(type(test))
# for i in test:
#     print(i)


# def subjects():
#     yield "machine learning"
#     yield "business analytics"
#     yield "java"
#     yield "python"
#
#
# subjects_library = subjects()
# print(next(subjects_library))
# print(next(subjects_library))
# print(next(subjects_library))
# print(next(subjects_library))
#
#

# What will be the output of this code?
# my_number = 12345
# my_number_iter = iter(my_number)
# print(next(my_number_iter))
# TypeError: 'int' object is not iterable
#
#
# Choose all correct statements:
# ls = [1, 2, 3]
# my_range = range(1, 5, 2)
# my_range is an iterable object
# ls is an iterable object
#
#
# What are iteration in Python?
# Iteration is the process of searching the elements of an object in a loop
# Repeated execution of a set of statements is called iteration
#
#
# Choose all correct statements:
# my_var = {1: "1", 2: "2", 3: "3"}.__iter__()
#
# my_var is an iterator
# my_var is an iterable object
#
#
#
# What will be the output of this code?
# ls = [0, 1, 2, 3]
# my_gen = (i for i in ls)
# my_gen_sliced = my_gen[1:3]
# print(my_gen_sliced)
#
# TypeError: 'generator' object is not subscriptable
#
#
#
# Choose all correct statements:
# my_var = (i for i in range(10))
#
#
# my_var is a generator
# my_var is an iterable object
# my_var is an iterator
#
#
# Choose all correct statements:
# my_var = iter("string")
# my_var is an iterator
# my_var is an iterable object
#
#
#
# What will be the output of this code?
# my_range = iter(range(0))
# print(next(my_range))
# StopIteration
#
#
# What are generators in Python?
# Any function that has "yield" statement in it
#
#
# What are iterators in Python?
# Any object that implements __iter__ method and __next__ methods


# import random
# from typing import Generator
#
#
# def dice_player(n_rounds: int) -> Generator[int, None, None]:
#     for i in range(n_rounds * 2):
#         yield random.randint(1, 6)
#
#
# def dice_game(n_rounds: int) -> str:
#     player_1_score, player_2_score = 0, 0
#     player_1_throw = dice_player(n_rounds)
#     player_2_throw = dice_player(n_rounds)
#     for throw in range(n_rounds):
#         current_player_1_throw = next(player_1_throw)
#         current_player_2_throw = next(player_2_throw)
#         print(current_player_1_throw, current_player_2_throw)
#         if current_player_1_throw > current_player_2_throw:
#             player_1_score += 1
#         if current_player_2_throw > current_player_1_throw:
#             player_2_score += 1
#         else:
#             pass
#     if player_1_score > player_2_score:
#         return "First"
#     if player_2_score > player_1_score:
#         return "Second"
#     else:
#         return "Draw"


# import base64
# print(base64.b32encode(bytearray("Hello world!", 'ascii')).decode('utf-8'))

# def str_to_base32(s):
#     base32_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
#
#     bit_str = ''.join([bin(ord(c))[2:].zfill(8) for c in s])
#     padding = len(bit_str) % 5
#     if padding > 0:
#         bit_str += '0' * (5 - padding)
#
#     base32_str = ''
#     for i in range(0, len(bit_str), 5):
#         chunk = bit_str[i:i+5]
#         index = int(chunk, 2)
#         base32_str += base32_alphabet[index]
#
#     return base32_str
#
#
# print(str_to_base32("Hello world!"))


# from __future__ import annotations
#
# from typing import Iterator, Union
#
#
# class NumberIterator:
#     def __init__(self, numbers: list) -> None:
#         self.numbers = numbers
#
#     def __iter__(self) -> NumberIterator:
#         self.it = 0
#         return self
#
#     def __next__(self) -> Union[int, StopIteration]:
#         if self.it >= len(self.numbers):
#             raise StopIteration
#         result = self.numbers[self.it]
#         self.it += 1
#         return result
#
#
# def fetch_numbers(iterator: Iterator, number: int) -> list:
#     result = []
#     while number > 0:
#         result.append(next(iterator))
#         number -= 1
#     return result
#
#
# iter_ = iter(NumberIterator([1, 2, 3, 4, 5]))
# next(iter_)
# print(fetch_numbers(iter_, 3))


# def time_range(time_start: tuple, time_end: tuple) -> tuple:
#     # write your code here
#     pass

#
# def fibonacci_generator(num):
#     fibonacci_start_pack = [0, 1]
#     current_fibonacci_index = -1
#     to_add = 0
#     while num > 0:
#         num -= 1
#         current_fibonacci_index += 1
#         print(f"fibonacci_start_pack = {fibonacci_start_pack} \n"
#               f"current_fibonacci_index = {current_fibonacci_index}")
#         fibonacci_start_pack.append(
#             fibonacci_start_pack[current_fibonacci_index] +
#             fibonacci_start_pack[current_fibonacci_index + 1])
#         print(f"fibonacci_start_pack = {fibonacci_start_pack}")
#
#         yield fibonacci_start_pack[current_fibonacci_index]
#
#
# fib_generator = fibonacci_generator(10)
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
# print(next(fib_generator))
#
#
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#
#
# def fibonacci_generator(num: int) -> int:
#     fib_list = [0, 1]
#     fib_index = -1
#     while num > 0:
#         num -= 1
#         fib_index += 1
#         fib_list.append(
#             fib_list[fib_index] + fib_list[
#                 fib_index + 1])
#         yield fib_list[fib_index]


# class Cycle:
#     def __init__(self, iterable) -> None:
#         self.iterable = iterable
#
#     def __iter__(self) -> Cycle:
#         self.it = 0
#         return self
#
#     def __next__(self) -> Any:
#         result = self.iterable[self.it]
#         self.it += 1
#         return result
#
#
# iterator = Cycle("abc")
# print(next(iterator))

# class NumberIterator:
#     def __init__(self, numbers: list) -> None:
#         self.numbers = numbers
#
#     def __iter__(self) -> NumberIterator:
#         self.it = 0
#         return self
#
#     def __next__(self) -> Union[int, StopIteration]:
#         if self.it >= len(self.numbers):
#             raise StopIteration
#         result = self.numbers[self.it]
#         self.it += 1
#         return result
#
# iterator = NumberIterator([0, 1, 2, 3])

# from collections.abc import Iterable
# from typing import Any, Iterable
#
#
# class Cycle:
#     def __init__(self, iterable: Iterable) -> None:
#         self.iterable = iterable
#
#     def __iter__(self) -> :
#         self.iteration = -1
#         return self
#
#     def __next__(self) -> Any:
#         if len(self.iterable) == 0:
#             raise StopIteration
#         self.iteration += 1
#         if self.iteration == len(self.iterable) - 1:
#             self.iterable[self.iteration]
#             self.iteration = -1
#         return self.iterable[self.iteration]
#
#
# obj = Cycle("qw")
# iterator = iter(obj)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
#
#
# from typing import Any, Iterable
#
#
# class Cycle:
#     def __init__(self, iterable: Iterable) -> None:
#         self.iterable = iterable
#
#     def __iter__(self) -> "Cycle":
#         self.iteration = -1
#         return self
#
#     def __next__(self) -> Any:
#         if len(self.iterable) == 0:
#             raise StopIteration
#         self.iteration += 1
#         if self.iteration == len(self.iterable) - 1:
#             self.iterable[self.iteration]
#             self.iteration = -1
#         return self.iterable[self.iteration]

# def text_to_base32(text):
#     # Define the base32 alphabet
#     base32_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
#
#     # Encode the text string in UTF-8 format
#     utf8_bytes = text.encode('utf-8')
#
#     # Initialize variables
#     bit_string = ''
#     base32_string = ''
#
#     # Convert the UTF-8 bytes to a bit string
#     for byte in utf8_bytes:
#         bits = bin(byte)[2:].rjust(8, '0')
#         bit_string += bits
#
#     # Add padding bits if necessary to make the bit string length a multiple of 5
#     padding_length = (5 - len(bit_string) % 5) % 5
#     bit_string += '0' * padding_length
#
#     # Convert the bit string to base32 format
#     for i in range(0, len(bit_string), 5):
#         bits = bit_string[i:i+5]
#         index = int(bits, 2)
#         base32_char = base32_alphabet[index]
#         base32_string += base32_char
#
#     # Add padding characters if necessary to make the output length a multiple of 8
#     padding_length = (8 - len(base32_string) % 8) % 8
#     base32_string += '=' * padding_length
#
#     # Return the base32 string
#     return base32_string
#
# text = "Hello, world!"
# base32_text = text_to_base32(text)
# print(base32_text)


# class LowerPrime:
#
#     @staticmethod
#     def prime_number_gen(number):
#         prime_numbers_list = []
#         for i in range(2, number + 1):
#             is_prime = True
#             for x in range(2, int(i ** 0.5) + 1):
#                 if i % x == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 prime_numbers_list.append(i)
#         return prime_numbers_list
#
#     def __init__(self, number: int) -> None:
#         self.number = number
#         self.prime_numbers_list = self.prime_number_gen(self.number)
#         self.start_len = len(self.prime_number_gen(self.number))
#
#     def __iter__(self) -> "LowerPrime":
#         return self
#
#     def __next__(self) -> int:
#         result = self.prime_numbers_list[-1]
#         self.prime_numbers_list.remove(result)
#         current_len = len(self.prime_numbers_list)
#         if self.start_len - current_len >= 2:
#             raise StopIteration
#
#         return result
#
#
# lower_prime = LowerPrime(number=11)
# lower_prime_it = iter(lower_prime)
# next(lower_prime_it) == 7
# next(lower_prime_it) == 5
# lower_prime_it.number == 11

#
# class LowerPrime:
#     def __init__(self, number: int) -> "LowerPrime":
#         self.number = number
#         self.cuurent = None
#
#     def __iter__(self) -> "LowerPrime":
#         self.cuurent = None
#         return self
#
#     def __is_prime(self, n) -> bool:
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     def __next__(self) -> int:
#         if self.number <= 2:
#             raise StopIteration
#         if self.cuurent is None:
#             current = self.number - 1
#         else:
#             current = self.current - 1
#         while not self.__is_prime(current):
#             current -= 1
#             if current < 2:
#                 raise StopIteration
#         self.current = current
#         return current
#
#
# class LowerPrime:
#     def __init__(self, number: int) -> None:
#         self.number = number
#         self.current = None
#
#     def __iter__(self) -> None:
#         self.current = None
#         return self
#
#     def __is_prime(self, n: int) -> bool:
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     def __next__(self) -> int:
#         if self.number <= 2:
#             raise StopIteration
#         if self.current is None:
#             current = self.number - 1
#         else:
#             current = self.current - 1
#         while not self.__is_prime(current):
#             current -= 1
#             if current < 2:
#                 raise StopIteration
#         self.current = current
#         return current


# def time_range(
#         time_start: tuple,
#         time_end: tuple
# ) -> tuple:
#     start = [elem for elem in time_start]
#     end = [elem for elem in time_end]
#
#     while start != end:
#         yield tuple(start)
#         start[2] += 1
#         if start[2] >= 60:
#             start[2] = 0
#             start[1] += 1
#             if start[1] >= 60:
#                 start[1] = 0
#                 start[0] += 1
#                 if start[0] >= 24:
#                     start[0] = 0
#
#
#
# t_range = time_range(time_start=(23, 59, 58),
#                      time_end=(0, 0, 3))
# print(next(t_range))
# test


# GETTER SETTER
# PROPERTY(GET, SET) sould have same name

# class GlassOfWater:
#     def __init__(self, temperature: int):
#         self.temperature = temperature
#
#     # temperature = property(temperature)
#     @property  # getter
#     def temperature(self):
#         print("get temp")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, temperature: int):
#         print("set temp")
#         if not (0 <= temperature <= 100):
#             raise Exception("Error: not in range 0 - 100")
#         self._temperature = temperature
#
#
#
#     # temperature = property(get_temperature,set_temperature)
#
#
# glass = GlassOfWater(temperature=1000)
#
# glass.temperature = 15
# glass.temperature = 25
# glass.temperature = 22
# glass.temperature = 21
# print(glass.temperature)
#
# print(glass.__dict__)




# Read-only attribute



# class Company:
#     def __init__(self,name):
#         self._name = name
#
#     @property
#     def name(self):
#         return f"This name is read_only: {self._name}"
# company = Company("Mate Academy")
#
#
#
#
# print(company.name)
# #company.name = "qwe" # AttributeError: property 'name' of 'Company' object has no setter
#
# print(company.__dict__)



# Descriptor = class if __get__ / __set__ / __delete__ overloaded
#
# class Two:
#     def __get__(self, instance, owner):
#         print("Get called")
#         return 2
#
# class Example:
#     x = 5
#     y = Two()
#
#
# example = Example()
# print(example.x)
# print(example.y)
#



# PROPERTY > descriptors if its possible to use



# class ArraySize:
#     def __get__(self, instance, owner):
#         return len(instance.arr)
#
#
# class Array:
#     size = ArraySize()
#
#     def __init__(self,arr):
#         self.arr = arr
#
#
# array_obj = Array([1,2,3])
#
# print(array_obj.size)
# array_obj.arr.append(5)
# print(array_obj.size)


# class Temperature:
#     def __get__(self, instance, owner):
#         print("get temp")
#         return instance._temperature
#
#     def __set__(self,instance,value):
#         print("set temp")
#         if not (0 <= value <= 100):
#             print("temp not in range")
#             return None
#         instance._temperature = value
#
#
# class GlassofWater:
#     temperature = Temperature()
#
#     def __init__(self, temperature):
#         self.temperature = temperature
#
#     def heat(self):
#         self.temperature += 1 # self.temp = self.temp + 1
#
# glass = GlassofWater(98)
#
# print(glass.__dict__)
# glass.heat()
# glass.heat()
# glass.heat()
#
# print(glass.temperature)
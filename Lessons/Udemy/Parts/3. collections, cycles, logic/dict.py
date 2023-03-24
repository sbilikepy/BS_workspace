# Cписок пар ключ:значение записные книги, логин-пароли
# print('________________________')
# Поиск по ключу намного быстрее чем поиск по значению
# Поиск по ключу - мгновенный

# Summary
# Let me summarize what we found out with our performance tests:
#
# If you focus on performance, use {}
# When merging dictionaries (without changing either of them), use
# .copy().update() for dictionaries with more than 15 elements
# dict(a, **b) for smaller dictionaries


qwe = 'a'
test = {
    qwe: 1,
    'b': 2,
    'd': 4,
    'c': 3
}
players = {
    'Carlsen': 2842,  # КЛЮЧ - ЗНАЧЕНИЕ chess players name : elo           {} a : b,
    'Caruana': 2822,  # KEYS  - VALUES
    'Mamedyarov': 2801,
    'Ding': 2797,
    'Giri': 2780
}
print('________________________')
players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801, Ding=2797, Giri=2780)  # переназначение
print(players)
print('________________________')
top1 = players['Carlsen']
print(f"Top chess player's rating is {top1}")
print(list(players))
print(sorted(players))  # сортировка по названию
print('________________________')
print(list(test))
print(sorted(test))
print(('Carlsen' in players))

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print(dict({('sape', 4139), ('guido', 4127), ('jack', 4098)}))

print(players.get('Carlsen'))
players['so'] = 2780
print(players)
print('so' in players)
print(players)
del players['so']
print(players)
keys = players.keys()
print(type(keys))
print(keys)
l = list(players.keys())
print(type(l))
print(sorted(players.keys()))
print('Carlsen' in players)
print('Kramnik' not in players)
vals = players.values()
print(type(vals))

vals = list(players.values())
print(type(vals))
print(sorted(players.values()))
players_copy = players.copy()
print('________________________')
print(players_copy)

for k, v in players.items():
    print(k, v, 'q')

items = players.items()
print(type(items))
players.pop('Giri')
print(players)
print(players.popitem())
print(players)
print(len(players))
players.setdefault('Karjakin')  # .SETDEFAULT если запрашиваемого элем.
# нет, то ключ добавляется, а значение становится NONE
print(players)
print(('_________________________________'))
print(('_________________________________'))
print(('_________________________________'))
print(('_________________________________'))
#######################          DICT VS ORDERED DICT
#######################          DICT VS ORDERED DICT
#######################          DICT VS ORDERED DICT
#######################          DICT VS ORDERED DICT
#######################          DICT VS ORDERED DICT
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['b'] = 'B'  # Порядок ввода не важен, словари идентичны (начиная с пайтон 3.7)
d2['a'] = 'A'
d2['c'] = 'C'

d3 = {}
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'

print(d1 == d2)
print(d1 == d3)

for k, v in d1.items():
    print(k, v)
for k, v in d2.items():
    print(k, v)
for k, v in d3.items():
    print(k, v)

from collections import OrderedDict
d1 = OrderedDict()
d1 ['a'] = 'A'
d1 ['b'] = 'B'
d1 ['C'] = 'C'

d2 = OrderedDict()                     # Пары ключ-значение идентичны, но из за очередности они НЕ РАВНЫ
d2 ['b'] = 'B'                         # OrderedDict контролирует порядок пар ключ - значение
d2 ['a'] = 'A'
d2 ['C'] = 'C'

d3 = OrderedDict()
d3 ['a'] = 'A'
d3 ['b'] = 'B'
d3 ['C'] = 'C'
print (d1==d2)
print (d1==d3)


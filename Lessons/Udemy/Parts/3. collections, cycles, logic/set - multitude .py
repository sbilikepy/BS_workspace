# тип сет содержит уникальные элементы
my_set = set()  # set() - конструктор
print(my_set)
print(type(my_set))
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(2)  # вторая двойка не добавляется так как она не уникальна
print(my_set)
my_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, ]
s = set(my_list)
print(s)

print(len(s))

print(1 in s)
print(5 in s)
print('___')
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # что входит.issubset(куда входит)
print(set2.issuperset(set1))  # куда входит.issuperset(что входит)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # возвращает TRUE если совпадений нет

set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5}
set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)  # находит одинаковые значения в множествах
print(set3)

set1 = {0, 1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5}

set3 = set1.difference(set2)  # показывает чего нет из первого множества во втором
print(set3)
set4 = set1.symmetric_difference(set2)  # показывает чего нет из первого во втором и из второго в первом
print(set4)

set1.update(set2)  # update как union, но он не возвращает новое множество, а модифицирует то
# на котором вызван метод update
print(set1)

#   .remove .discrad . pop  - методы удаления элементов из множеств
set1.remove(1)
print(set1)
# print(set1.remove(42)) # возникла бы ошибка, так как числа нет в множестве
set1.discard(2)
print(set1)
set1.discard(42)     # ошибки не возникло
print(set1)
popped_out_element = set1.pop()
print(popped_out_element)  # по документации .Pop удаляет СЛУЧАЙНЫЙ ЭЛЕМЕНТ

set1.clear()          # полностью вычищает список
print(set1)
int_list = [1, 2, 3]
mixed_list = [1, 2.0, "string"]
print(type(int_list))
print(len(int_list))
print(int_list[0])
print(int_list[-1])
print(int_list[0::2])
names1 = ["John", "Bob", "Alice"]
names2 = ["Tracy", "Elijah", "Mason"]
names_combined = names1 + names2
print(names_combined)
names1[0] = "Liam"
print(names1)
names_combined = names1 + names2
print(names_combined)
names1.append("William")
names1.append("James")
print(names1)
popped = names1.pop()
print(popped)
print(names1)
names1.pop(0)
print(names1)
names1.append("James")
names1.sort()  # СОРТИРОВКА
print(names1)
letters = ["ac", "ab", "aa"]
letters.sort()
print(letters)
letters = ["abc", "a", "ab"]
letters.sort(key=len)  # сортировка по длинне
print(letters)
numbers = [3, 2, 8, 5, 0, 3, 4, 1, 1]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print("_________________")
numbers44 = [3, 2, 8, 5, 0, 3, 4, 1, 1]
print(numbers44)
numbers44.reverse()
print(numbers44)
numbers44.sort(reverse=True)
print(numbers44)
print("_______")
print(numbers)
numbers.insert(0, 22)
print(numbers)
listtest = ["1", "2", "3"]
listtest.append("321")
print(listtest)
print(numbers.index(5))  # вписываем значение, которое ищем,
# получаем индекс
print(numbers.count(3))  # вписываем значение, которое ищем,
# получаем количество
copy = numbers.copy()  # делает бекап списка в переменной,
# но содержит изменяемый тип данных,
#                          то есть он может поменяться

print(copy)
numbers.append("1441")
print(numbers)
print(copy)
numbers.clear()
print(numbers)

# трансформация последовательности в другую

def square(*args):
    return [x * x for x in args]


print(square(1, 2, 3, 4, 5))


def triple(*args):
    return [x * 3 for x in args]


print(triple(1, 2, 3, 4, 5))

print('________________map function_________________')  # проходится по двум функциям


def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)
print(result)

for i in result:
    print(i)

print(type(result))

print(list(map(square, numbers)))


def is_adult(age):
    return age >= 18


ages = [14, 18, 21, 16, 30]

adult_result = filter(is_adult, ages)      # фильтр возвращает объект, в него передаётся фильтр,
                                           # который возвращает тру или фалс, если фалс - он исключается
                                           # из последовательности и результатат

print(adult_result)
print(list(filter(is_adult, ages)))

print(('________________lambda expressions________лямбда выражения_________'))


is_adult = lambda age: age >= 18
print(list(filter(is_adult, ages)))


multiplier = lambda x,y : x*y
print(multiplier(2, 3))



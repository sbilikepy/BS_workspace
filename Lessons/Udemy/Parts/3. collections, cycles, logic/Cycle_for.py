numbers = [1,2,3,4,5]
print(numbers)
for i in numbers:
    print(i)

for i in numbers:
    print (i*i)

numbers = range(1,6)          # последняя граница не включается в вывод
print(type(numbers))

for i in numbers:
    print (i)

for i in range(1,6):
    print(i)

for i in range(1,6):
    if i % 2 == 0:
        print((f'{i} is even'))
    else:
        print((f'{i} is odd'))

print('______')


numbers = [1,3,5,7,9]
for i, item in enumerate(numbers):
    numbers[i] *= 2
print(numbers)


print('_________________________________')

name = "John"
for i in name:
    print(i)

for _ in range(5):                  # _ если нет необходимости именовать
    print('Povitryana tryvoga!')



person = "John", 'Silver', 22
for _ in person:
    print (_)



print('_________________________________')

persons = [('John', 22,), ('Bob', 32), ('Dave', 20)]
print(len(persons))

# tuple unpacking
for (name, age) in persons:
    print(f'{name} is {age} year\'s old')

print('_________________________________')


players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801)
for name in players:
    print(name)

for item in players.items():
    print(item)

for k,v in players.items():            # 1-я переменная кей, а вторая ЗНАЧЕНИЕ В ДИКТЕ
    print(f'{k} have {v} elo')

for v in players.values():             # 1-я переменная кей, а вторая ЗНАЧЕНИЕ В ДИКТЕ
    print(v)


#find all pairs sum of wich equals 0
list1 = [2,4,-5,6,8,-2]
list2 = [2,-6,8,3,5,-2]
pairs = []
for x in list1:
    for y in list2:
        if x+y == 0:
            print('______________________')
            print(f'{x} + {y} = 0')
            pair = [x,y]
            pairs.append((pair))

print(f'\n what we have for now:\n{pairs}')

print(type(pairs))






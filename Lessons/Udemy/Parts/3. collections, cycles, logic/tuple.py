# кортеж, неизменяемый список        = ('', '', '')   используется для защиты от изменений
strings = ('str1', 'str2', 'str3')
strings2 = ['str1', 'str2', 'str3']
print(strings[0])
print(type(strings))
print('___')
person = ('John', 'Silver', 22)
print(type(person))
print(len(person))
print(person[0])
print(person[-1])
print(strings2[-1])
print(strings2)
strings2[0] = 'Bob'
print(strings2)
print(person.count('John'))
print(person.index('John'))
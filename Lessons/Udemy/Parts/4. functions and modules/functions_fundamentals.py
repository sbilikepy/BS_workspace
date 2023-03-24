def greeting():  # def Название():
    '''
    DOCSTRING: info about the function
    INPUT: no input...
    OUTPUT: Hello!
    '''
    print('HellO!')


greeting()
help(greeting)


def print_name(a):
    print(a)


print_name('Baga')


def print_name(name):
    print(name)


print_name(123)

print('_________________________________')


def print_name(name='Default'):  # в случае если ничего не передаем то значение будет по умолчанию
    print(name)


print_name(123)

print('_________________________________')
result = print_name()
print(result)
print(type(result))

print('_________________________________')


def get_greeting(name):
    return 'Hello ' + name


greeting = get_greeting('Baga')

print(greeting)

print('_________________________________')


def get_sum(a, b):
    return a + b
result = get_sum(10, 2)
print(result)

print('_________________________________')


def is_adult(age):
    return age >= 18
is_adult = is_adult(20)
print(is_adult)

print('_________________________________')

def is_palindrom(text):
    return text == text[::-1]
print(is_palindrom('aabaa'))
print(is_palindrom('aaba2a'))

print('_________________________________')

def calc_taxes(p1,p2,p3):
    return sum((p1,p2,p3)) * 0.06


print(calc_taxes(10, 20, 30))

print('_________________________________')
def calc_taxes(p1,p2,p3):
    print(sum((p1,p2,p3)) * 0.06)

calc_taxes(10, 20, 30)


print('_________________________________')

def calc_taxes(p1,p2,p3):
    return sum((p1,p2,p3)) * 0.06


print(calc_taxes(10, 20, 30))


print('_________________________________') ############### бесконечное кол-во аргументов

def calc_taxes(*args):
    for x in args:
        print (f'Got payment = {x}')
    return sum(args) * 0.06


print(calc_taxes(10,20,30,40))


def save_players(**kwargs):        # значит что сюда передаются N пар ключ: значение
    for k,v in kwargs.items():
        print(f'player {k} has ratio {v}')

save_players(carlsen = 2800, giri = 2780)


# def func_importan(a,b,c,d,*args, *kwargs)  # позиционные элементы,
                                            # затем аргс (болшое кол-во аргументов)
                                            # а затем кваргс (клю: значение), большая редкость
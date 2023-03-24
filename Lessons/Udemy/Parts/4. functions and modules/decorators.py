#  продвинутая тема
# функция в питоне - полноценный объект


def hello_world():
    print('Hello world')


hello_world()

hello2 = hello_world  # () = вызов
print(hello2())


def hello_world():
    def internal():
        print('Hello world')

    return internal


hello2 = hello_world()

print(hello2)
hello2()

print('________________функция в качестве аргумента принимает другую функцию_________________')


def say_something(func):
    func()


def hello_world():
    print('Hello world')


say_something(hello_world)


def log_decorator(func):
    def wrap():
        print(f'calling func: {func}')
        func()
        print(f'func {func} finished, its wkr')

    return wrap


def hello():
    print('hello world')


wrappedbylogger = log_decorator(hello)
wrappedbylogger()


@log_decorator
def hello():
    print('hello')


hello()

print('________________Замер скорости выполнения функций_________________')

from timeit import default_timer as timer
import math
import time


def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f'{func.__name__} tool {end - start} for execution')

    return inner

@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))

factorial(10)
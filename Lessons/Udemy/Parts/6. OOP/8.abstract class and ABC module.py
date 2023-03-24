# для запрещения вызова метод raise

import math
from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod  # объявление абстрактным
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        print('calc perimeter')
        # pass

    def drag(self):
        print('basic dragging functionality')


class Triangle(Shape):  # Наследует абстрактный класс
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f"drawing triangle with sides = {self.a}, {self.b}, {self.c}")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def drag(self):
        super().drag()
        print('Additional action')


t = Triangle(10, 10, 10)
print(t.perimeter())
t.drag()

# везде где включаются абстрактные методы, мы можем определить базовый функционал

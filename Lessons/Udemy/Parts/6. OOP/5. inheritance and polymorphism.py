class Shape:
    def __init__(self):
        print("Shape created.")

    def draw(self):
        print("Drawing shape")

    def area(self):
        print("Calc area")

    def perimeter(self):
        print("Calculating perimeter")


class Rectangle(Shape):  # наследник Shape, мы имеет доступ к атрибутам класса Shape
    def __init__(
        self, width, height
    ):  # так же можем переопределять реализацию родительских методов
        Shape.__init__(self)
        self.width = width
        self.height = height

        print("Rectangle created.")
        Shape.area(self)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print("Drawing rectangle with weight and height")


rect = Rectangle(10, 15)

print(rect.area())
print(rect.perimeter())
rect.draw()

import math


class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c

        print("Triangle created")

    def draw(self):
        print(f"Drawing triangle with sides: {self.a},{self.b},{self.c}")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        are = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(are)

    def perimeter(self):
        periansw = self.a + self.b + self.c
        print(periansw)


print("---------")
tritest = Triangle(10, 10, 10)
tritest.draw()
tritest.area()
tritest.perimeter()

for shape in [rect, tritest]:
    shape.draw()

# если 2 класса имеют методы с одинаковыми названиями, то можно использовать концепцию полиморфизма

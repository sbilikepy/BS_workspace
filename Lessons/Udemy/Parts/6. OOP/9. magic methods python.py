class Point:
    def __init__(self, x, y):  # init конструктор класса
        self.x = x
        self.y = y

    def __str__(self):  # строковое представление экземпляра класса
        return f"point x = {self.x} and y = {self.y}"


p = Point(3, 4)
print(p)


class Road:
    def __init__(self, len):
        self.len = len

    def __len__(self):
        return self.len

    def __str__(self):
        return f"a road len : {len(self)}"

    def __del__(self):
        print(f"The road has been destroyed")


r = Road(100)
print(len(r))

print(r)

# when lil class have more then 1 giga class

class Animal():
    def die(self):
        print('bye ;(')
        self.health = 0


class Carnivour():
    def hunt(self):
        print('eating')
        self.satiety = 100


class Dog(Animal, Carnivour):
    def bark(self):
        print('woof-woof')


dogo = Dog()
dogo.bark()
dogo.hunt()
dogo.die()

print('_________________________________')


# class Animal:                        #deadly diamond of death example
#     def set_health(self,health):
#         print('set in animal')
#
# class Carnivour(Animal):
#     def set_health(self,health):
#         print('set in carnivour')
#
# class Mammal (Animal):
#     def set_health(self,health):
#         print('set in mammal')
#
#
# class Dog(Carnivour, Mammal):          # НАСЛЕДУЕТ ПЕРВОЕ в случае, если у предка одинаковые методы
#     pass
#
print('_________________________________')

print('_________________________________')

# dogo = Dog()
# dogo.set_health(10)

# class Animal:                        #deadly diamond of death example
#     def set_health(self,health):
#         print('set in animal')
#
# class Carnivour(Animal):
#     def set_health(self,health):
#         print('set in carnivour')
#
# class Mammal (Animal):
#     def set_health(self,health):
#         print('set in mammal')
#
#
# class Dog(Carnivour, Mammal):          # НАСЛЕДУЕТ ПЕРВОЕ в случае, если у предка одинаковые методы
#     def set_health(self,health):
#         Mammal.set_health(self, health)
#         Carnivour.set_health(self, health)
#         Animal.set_health(self, health)
#
# dogo = Dog()
# dogo.set_health(10)

print('_________________________________')

print('_________________________________')

# class Animal:  # deadly diamond of death example
#     def set_health(self, health):
#         print('set in animal')
#
#
# class Carnivour(Animal):
#     def set_health(self, health):
#         super().set_health(health)
#         # Animal.set_health(self, health)
#         print('set in carnivour')
#
#
# class Mammal(Animal):
#     def set_health(self, health):
#         super().set_health(health)
#         # Animal.set_health(self, health)
#         print('set in mammal')
#
#
# class Dog(Carnivour, Mammal):  # НАСЛЕДУЕТ ПЕРВОЕ в случае, если у предка одинаковые методы
#     def set_health(self, health):
#         super().set_health(health)  # ГАРАНТИЯ ПОСЛЕДОВАТЕЛЬНОСТИ снизу вверх(глубина), слева направо
#         # Mammal.set_health(self, health)
#         # Carnivour.set_health(self, health)
#         print('set in dog')
#
#
# dogo = Dog()
# dogo.set_health(10)

# функция super даёт гарантию последовательности выхова

print('_________________________________')

print('_________________________________')

class Animal():
    def __init__(self):
        self.health = 100

    def hit(self,damage):
        self.health -= damage

class Carnivour(Animal):
    def __init__(self):
        super().__init__()
        self.legs = 4

c = Carnivour()
c.hit(10)

print(c.health)
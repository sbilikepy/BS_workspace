# # OOP Single Inheritance
# def vowel_count(sentence: str) -> int:
#     return len(
#         [i for i in sentence if i in ["a", "e", "i", "o", "u"]]
#     )
#
#
# #     16  -->  1 + 6 = 7
# #    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# # 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
#
#
# # def sum_of_digits(number: int) -> int:
# #     while True:
# #         temp = [i for i in str(number)]
# #         number = sum([int(i) for i in temp])
# #         if len(str(number)) == 1:
# #             return number
# #
# #
# #
# # sum_of_digits(16)
# # sum_of_digits(942)
# # sum_of_digits(132189)
# # sum_of_digits(493193)
#
#
# def data_compression(data: str) -> str:
#     print(f"len = {len(data)}")
#     if len(data) == 0:
#         return ""
#     if len(data) == 1:
#         return f"1{data}"
#
#     result = []
#     for i in range(0,len(data)):
#         counter = 1
#         prev = None
#         curr = data[i]
#         print("************************************")
#         print(f"prev {prev} | curr= {curr} || {i}, {data[i]}")
#
#         if i > 0:
#             prev = data[i - 1]
#             curr = data[i]
#             print(f"prev {prev} | curr= {curr} || {i}, {data[i]}")
#
#         if prev == curr:
#             counter += 1
#
#         else:
#             result.append(counter)
#             result.append(prev)
#             counter = 1
#             result.append(counter)
#             result.append(data[i])
#
#     print("DATA",result)
#
#
#
#
#
#
# print(data_compression("AAABBBAAABA")) #-> 2A2B2A1b1A1b1a


# INHERITANCE animal -> cat dog
# ENCAPSULATION
# POLYMORPHISM
# ABSTRACTION
# class Employee:
#     bonus_coefficient = 1.1
#
#     def __init__(self, base_salary):
#         self.base_salary = base_salary
#
#
#     def calculate_salary(self):
#         return self.base_salary * Employee.bonus_coefficient
#
#
# x = Employee(1000)
# print(x.calculate_salary())
#
# #vs
# base = 1000
# bonus = 1.1
# def calc(base):
#     return base*bonus
#
#
# print(calc(base))
#
#
#
#
#
# # INHERITANCE1
#
# class Animal:
#     def eat(self):
#         print("eating")
#
# class Cat(Animal):
#     def sleep(self):
#         print("sleepo peepo")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("bark")
#
#
#
# dog = Dog()
# cat = Cat()
#
# cat.sleep()
# dog.bark()
#
# # INHERITANCE1


# class User:
#     role = "user"
#
#     def __init__(self, name, age = 0):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f"{self.name} is {self.age}")
#
#
# class Admin(User):
#     role = "admin"
#
#     def auth(self):
#         print(f"Admin {self.name} authorized")
#
#
# baga = User("Baga")
# petia = Admin("Petek")
#
# print(dir(baga))
# print(dir(petia))
#
# dir(baga)
# baga.age = 27
# baga.print_info()
# petia.print_info()


# class User:
#     role = "user"
#
#     def __init__(self, name, age = 0):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f"{self.name} is {self.age}")
#
#
# class Admin(User):
#     role = "admin"
#
#     def __init__(self, name,surname):
#         super().__init__(name)
#         self.surname = surname
#
#
#
#     def auth(self):
#         print(f"Admin {self.name} authorized")
#
#
#     def print_info(self):
#         super(Admin,self).print_info()
#         print("hi from Adm")
#
# baga = User("Baga")
# petia = Admin("Petek","Smith")
#
# print(dir(baga))
# print(dir(petia))
#
# dir(baga)
# baga.age = 27
# baga.print_info()
# petia.print_info()
# print(petia.surname)
# print(petia.__dict__)
# petia.print_info()
#
# isinstance(baga,User)
# print(isinstance(petia, User))
# print(isinstance(petia, Admin))
#
# print(issubclass(Admin,User))
# print(issubclass(User,Admin))


# class User(object):
#     pass
#
#
# print(issubclass(User, object)) # obj -> Class -> User
#
# user = User
# print(type(user))
# print(type(type))
# print(issubclass(type,object))
# print(dir(object))
#
#
#
# class Car:
#     def __init__(self, model):
#         self.model = model
#
#     @staticmethod
#     def create_car(name):
#         return Car(name)
#
#
# for k, v in Car.create_car("Porshe").__dict__.items():
#     print(k, v)
#
# ___________________________________________________________________________
# class Employee:
#     def __init__(self, name: str, surname: str):
#         self.name = name
#         self.surname = surname
#
#
# class Freelance(Employee):
#     def __init__(self, name: str, surname: str, email: str):
#         super().__init__(name, surname)                      #!!!!!!!!!!!!!
#         self.email = email
#
#
# freelance_employee = Freelance("Joseph", "Green", "josephgreen@gmail.com")
#
# print(freelance_employee.name)  # Joseph
# print(freelance_employee.surname)  # Green
# print(freelance_employee.email)  # josephgreen@gmail.com
#
# class Employee:
#     def print_info(self):
#         print("Hello, I'm Employee")
#
#
# class Freelance(Employee):
#     def print_info(self):
#         super().print_info()
#         print("Hello, I'm Freelance Employee")
#
#
# freelance_employee = Freelance()
# freelance_employee.print_info() # Hello, I'm an Employee
#                                 # Hello, I'm a Freelance Employee
#

# class Student:
#     def check_pass_fail(self):
#         if self.marks >=40:
#             return True
#         else:
#             return False
#
# student_1 = Student()
# student_1.name = "Harry"
# student_1.marks = 85
# did_pass = student_1.check_pass_fail()
# print(did_pass)
#
# print(student_1.__dict__)
#
# student_2 = Student()
#
#
# print(type(student_1))
# print(type(student_2))

# class Computer:
#
#     def __init__(self):
#         self.__maxprice = 900
#
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
# c = Computer()
# c.sell()
#
# # change the price
# c.__maxprice = 1000
# c.sell()
#
# # using setter function
# c.setMaxPrice(1000)
# c.sell()

# class Polygon:
#     # method to render a shape
#     def render(self):
#         print("Rendering Polygon...")
#
#     def hola(self):
#         print("hola")
#
# class Square(Polygon):
#     # renders Square
#     def render(self):
#         print("Rendering Square...")
#
# class Gubka_Bob(Square):
#     # renders circle
#     def render(self):
#         print("SQUARE PANTS")
#
#
# gbob = Gubka_Bob()
# print(isinstance(gbob, Polygon))
# gbob.hola()
# gbob.render()


# class Vehicle(object):
#     @staticmethod
#     def go(city: str) -> None:
#         print(f"Go to {city}")
#
#
# class Car(Vehicle):
#     @staticmethod
#     def wash() -> None:
#         print("Washing the car...")
#
#
# class Train(Vehicle):
#     @staticmethod
#     def buy_ticket() -> None:
#         print("Buying the ticket...")

# list_to_check = [issubclass(int, type), issubclass(int, object), issubclass(type, type), issubclass(type, object)]
#
#
#
# def functest(list_):
#     for i in list_:
#         print(i)
#
# functest(list_to_check)
#
#
# OOP multiple inheritance
# class A():
#     pass
#
# class B(A):
#     pass
#
# print(issubclass(B, A))
# print(isinstance())

# MRO - method resolution order  #.mro()

# class A():
#     def __init__(self):
#         pass
#
#     pass
#
#
# class B(A):
#     def __init__(self):
#         pass
#
#     pass
#
#
# class C(B, A):
#     def __init__(self):
#         pass
#
#
# print(C.mro())
#
#
# class RadioUserMixin():  # ____Mixin
#     pass
#
#
# class Car(Transport, RadioUserMixin):
#     pass
#

# class Dog(object):
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def __lt__(self, other):
#         return self.name < other.name
#
#
# dog1 = Dog("Name1", "Breed1")
# dog2 = Dog("Name2", "Breed2")
# print(dog1.__str__())
# # print(dog1<dog2) # error without def __lt__()
# print(dog1<dog2)


# #Multilevel Inheritance
# class Grandfather:
#     @staticmethod
#     def tell_good_stories():
#         print("Once, in old times")
#
#
# class Father(Grandfather):
#     @staticmethod
#     def go_fishing():
#         print("I'd like to go fishing")
#
#
# class Son(Father):
#     def __init__(self, name: str):
#         self.name = name
#
#     def print_name(self):
#         print(f"My name is {self.name}")
#
#
# joseph = Son("Joseph")
# joseph.print_name() # My name is Joseph
# joseph.go_fishing() # I'd like to go fishing
# joseph.tell_good_stories() # Once, in old times
#
#
# class Mother:
#     @staticmethod
#     def singing():
#         print("I'm singing")
#
#
# class Father:
#     @staticmethod
#     def go_fishing():
#         print("I'd like to go fishing")
#
#
# class Son(Father, Mother):
#     def __init__(self, name: str):
#         self.name = name
#
#     def print_name(self):
#         print(f"My name is {self.name}")
#
#
# joseph = Son("Joseph")
# joseph.print_name() # My name is Joseph
# joseph.go_fishing() # I'd like to go fishing
# joseph.singing() # I'm singing
#
# #Multiple Inheritance
# class Grandfather:
#     @staticmethod
#     def tell_good_stories():
#         print("Once, in old times")
#
#
# class Father(Grandfather):
#     @staticmethod
#     def go_fishing():
#         print("I'd like to go fishing")
#
#
# class Mother:
#     @staticmethod
#     def singing():
#         print("I'm singing")
#
#
# class Son(Father, Mother):
#     pass
#
#
# son = Son()
# son.tell_good_stories()  # Once, in old times
# son.go_fishing()  # I'd like to go fishing
# son.singing()  # I'm singing
#
#
# #Hierarchical Inheritance
# class Parent:
#     @staticmethod
#     def watching_tv():
#         print("I'm watching TV")
#
#
# class Son(Parent):
#     pass
#
#
# class Daughter(Parent):
#     pass
#
#
# son = Son()
# daughter = Daughter()
#
# son.watching_tv() # I'm watching TV
# daughter.watching_tv() # I'm watching TV
#
#
# #Hybrid Inheritance
# class Grandfather:
#     @staticmethod
#     def tell_good_stories():
#         print("Once, in old times")
#
#
# class Father(Grandfather):
#     @staticmethod
#     def go_fishing():
#         print("I'd like to go fishing")
#
#
# class Mother:
#     @staticmethod
#     def singing():
#         print("I'm singing")
#
#
# class Son(Father, Mother):
#     pass
#
#
# son = Son()
# son.tell_good_stories()  # Once, in old times
# son.go_fishing()  # I'd like to go fishing
# son.singing()  # I'm singing


# MRO — Method Resolution Order   print(CLASSNAME.mro())
# In the multiple inheritance scenario, any specified attribute is searched
# first in the current class. If not found, the search continues into parent
# classes in depth-first, left-right direction without searching the same
# class twice. So, in the example with the Son class, the search order is
# Son -> Father -> Mother- > object. Since all classes are child classes
# of the object, it is always the last class in the MRO. To view the MRO
# of a particular class, you can use the mro() method which returns a list:
# class Mother:
#     @staticmethod
#     def singing():
#         print("I'm singing The Beatles")
#
#
# class Father:
#     @staticmethod
#     def singing():
#         print("I'm singing Queen")
#
#
# class Son(Father, Mother):
#     def __init__(self, name: str):
#         self.name = name
#
#     def print_name(self):
#         print(f"My name is {self.name}")
#
#
# joseph = Son("Joseph")
# joseph.singing() # I'm singing Queen


# from __future__ import annotations
#
#
# class Bike(object):
#     def __init__(self, brand: str, model: str, max_speed: int) -> None:
#         self.brand = brand
#         self.model = model
#         self.max_speed = max_speed
#
#     @classmethod
#     def from_dict(cls, bike_dict: dict) -> Bike:
#         return cls(
#             brand=bike_dict["brand"],
#             model=bike_dict["model"],
#             max_speed=bike_dict["max_speed"],
#         )
#
#
# class MountainBike(Bike):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#
#
# class RoadBike(Bike):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#
#
# mountain_bike = MountainBike.from_dict({
#     "model": "C2000",
#     "brand": "Civia",
#     "max_speed": 35,
# })
#
# print(isinstance(mountain_bike, MountainBike))
# print(mountain_bike.brand)
# print(mountain_bike.model)
# print(mountain_bike.max_speed)


# class Espresso:
#     def __init__(self) -> None:
#         self.cup_with_coffee = []
#
#     def add_coffee(self) -> None:
#         self.cup_with_coffee.append("Coffee")
#
#     def add_water(self) -> None:
#         self.cup_with_coffee.append("Hot water")
#
#     def add_sugar(self) -> None:
#         self.cup_with_coffee.append("Sugar")
#
#     def add_milk(self) -> None:
#         """
#         No milk provided in espresso
#         """
#
#     def make_coffee(self) -> list:
#         self.add_coffee()
#         self.add_water()
#         self.add_sugar()
#         self.add_milk()
#         return self.cup_with_coffee
#
#
# class CaffeineFreeMixin:
#     def add_coffee(self) -> None:
#         self.cup_with_coffee.append('Caffeine free coffee')
#
#
# class DoubleWaterMixin:
#     def add_water(self) -> None:
#         self.cup_with_coffee.append("Hot water x2")
#
#
# class NoSugarMixin:
#     def add_sugar(self) -> None:
#         pass
#
#
# class MilkMixin:
#     def add_milk(self) -> None:
#         self.cup_with_coffee.append("Milk")
#
#
# class Americano(DoubleWaterMixin, Espresso):
#     pass
#
#
# class CaffeineFreeEspresso(CaffeineFreeMixin, Espresso):
#     pass
#
#
# class NoSugarMilkEspresso(NoSugarMixin, MilkMixin, Espresso):
#     pass
#
#
# class CaffeineFreeNoSugarMilkAmericano(CaffeineFreeMixin, NoSugarMixin, DoubleWaterMixin, MilkMixin, Espresso):
#     pass

# class Aboba:
#     def __init__(self, name):
#         self.name = name
#         self.q = "q"
#
#     def say_hi(self):
#         print(f"{self.name}: Hi!")
#
#
# class Boba(Aboba):
#     def __init__(self,name, age=13):
#         super(Boba, self).__init__(name)
#         self.age = age
#
# b = Boba("Sa")
# b.say_hi()
# print(b.q)
# print(b.age)
# print(b.__dict__)

# ENCAPSULATION         № PPP public. _protected. __private
# ENCAPSULATION         № PPP public. _protected. __private
# ENCAPSULATION         № PPP public. _protected. __private

# self.__? = private

#
# class Product:
#     def __init__(self, name, price, last_customer_rating=None):
#         self.__name = name
#         self.__price = price
#         self.last_customer_rating = last_customer_rating
#
#     def print_product_info(self):
#         print(
#             f"The {self.__name} price is {self.__price}"
#             f" (rating: {self.last_customer_rating})"
#         )
#
#
# book_secure = Product("Book", 50)
# book_secure.last_customer_rating = 444
# book_secure.print_product_info()
# book_secure.name = "Book cheated"
# book_secure.print_product_info()
# print(book_secure.__dict__)
# book_secure._Product__price = 0
# print(book_secure.__dict__)


# class Base:
#     def __init__(self, name):
#         self.name = name

#         self.public = "public"
#         # 1. Inside class
#         # 2. Inside child class
#         # 3. Outside class

#         self._protected = "protected"
#         # 1. Inside class
#         # 2. Inside child class

#         self.__private = "private"
#         # 1. Inside class
#
#     def __str__(self):
#         return f"{self.public}, {self._protected}, {self.__private}"
#
#     def _protected(self):
#         print("first")
#
#     def __private(self):
#         print("2nd")
#
#
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#
#         # ok because
#         # 1. Inside class
#         # 2. Inside child class
#         self._protected()
#
#         # bad practice because NOT Inside class
#         self.__private()


# POLYMORPHISM 1 interface, diff realisation
#
# print(len("hello"))
# print(len([1, 2, 3]))

# ABSTRACTION view from abstracted point?
# ABC, @abstractmethod
# ABC = Abstract Base Class         # everywhere except base class


# By default, Python does not provide abstract classes. Python comes with a
# module that provides the base for defining Abstract Base classes(ABC) and that
# module name is ABC. ABC works by decorating methods of the base class as
# abstract and then registering concrete classes as implementations of the
# abstract base. A method becomes abstract when decorated with the keyword
# @abstractmethod. For Example:
# Python program showing
# abstract base class work

# from abc import ABC, abstractmethod
#
#
# class Polygon(ABC):
#
#     @abstractmethod
#     def noofsides(self):
#         pass
#
#
# class Triangle(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
#
# class Pentagon(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")
#
#
# class Quadrilateral(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")
#
#
# # Driver code
# R = Triangle()
# R.noofsides()
#
# K = Quadrilateral()
# K.noofsides()
#
# R = Pentagon()
# R.noofsides()
#
# K = Hexagon()
# K.noofsides()


# Python program showing
# implementation of abstract
# class through subclassing


# class parent():
#     def geeks(self):
#         pass
#
#
# class child(parent):
#     def geeks(self):
#         print("child class")
#
#
# # Driver code
# print(issubclass(child, parent))
# print(isinstance(child(), parent))


# class ListStatistics:
#     def __init__(self, numbers: list) -> None:
#         if len(numbers):
#             self.__numbers = numbers
#         else:
#             self.__numbers = []
#
#     def __get_min_value(self) -> int:
#         return min(self.__numbers)
#
#     def __get_max_value(self) -> int:
#         return max(self.__numbers)
#
#     def __get_average(self) -> int:
#         return sum(self.__numbers) / len(self.__numbers)
#
#     def __get_median(self) -> int:
#         len_l = len(self.__numbers)
#         numo = sorted(self.__numbers)
#         if len_l % 2 == 0:
#             return (numo[:int(len_l / 2) + 1:]
#                     [-1] + numo[:int(len_l / 2):][-1]) / 2
#         return numo[:int(len_l / 2) + 1:][-1]
#
#     def calculate_statistics(self) -> dict:
#         return {
#             "min_value": ListStatistics.__get_min_value(self),
#             "max_value": ListStatistics.__get_max_value(self),
#             "average": ListStatistics.__get_average(self),
#             "median": ListStatistics.__get_median(self),
#         }
#
#
# listt = ListStatistics([80, 15, 66, 2, 8])
#
# print(listt.calculate_statistics())

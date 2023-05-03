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

# from abc import ABC, abstractmethod
#
#
# class Machine(ABC):
#     @abstractmethod
#     def do_work(self, *args, **kwargs) -> None:
#         pass
#
#     @abstractmethod
#     def stop_work(self, *args, **kwargs) -> None:
#         pass
#
#
# class Truck(Machine):
#     def do_work(self, *args, **kwargs) -> None:
#         print("Truck starts working")
#
#     def stop_work(self, *args, **kwargs) -> None:
#         print("Truck stopped working")
#
#
# class Bulldozer(Machine):
#
#     def do_work(self, *args, **kwargs) -> None:
#         print("Bulldozer starts working")
#
#     def stop_work(self, *args, **kwargs) -> None:
#         print("Bulldozer stopped working")
#
#
# class Excavator(Machine):
#
#     def do_work(self, *args, **kwargs) -> None:
#         print("Excavator starts working")
#
#     def stop_work(self, *args, **kwargs) -> None:
#         print("Excavator stopped working")
#
#
# def build() -> None:
#     machines = [Truck(), Bulldozer(), Excavator]
#     flag = False
#     for i in machines:
#         i.do_work(None)
#         flag = not flag
#     if flag is True:
#         for i in machines:
#             i.stop_work(None)


# GETTER SETTER
# PROPERTY(GET, SET) should have same name

# class GlassOfWater:
#     def __init__(self, temperature: int):
#         self.temperature = temperature
#
#     # temperature = property(temperature)
#     @property  # getter                                           #!!!!!!
#     def temperature(self):
#         print("get temp")
#         return self._temperature
#
#     @temperature.setter                #!!!!!! <getter_property_name>.setter
#     def temperature(self, temperature: int):
#         print("set temp")
#         if not (0 <= temperature <= 100):
#             raise Exception("Error: not in range 0 - 100")
#         self._temperature = temperature
#
#
#
#     # temperature = property(get_temperature,set_temperature)
#
#
# glass = GlassOfWater(temperature=1000)
#
# glass.temperature = 15
# glass.temperature = 25
# glass.temperature = 22
# glass.temperature = 21
# print(glass.temperature)
#
# print(glass.__dict__)


# Read-only attribute


# class Company:
#     def __init__(self,name):
#         self._name = name
#
#     @property
#     def name(self):
#         return f"This name is read_only: {self._name}"
# company = Company("Mate Academy")
#
#
#
#
# print(company.name)
# #company.name = "qwe" # AttributeError: property 'name' of 'Company' object has no setter
#
# print(company.__dict__)


# Descriptor = class if __get__ / __set__ / __delete__ overloaded
#
# class Two:
#     def __get__(self, instance, owner):
#         print("Get called")
#         return 2
#
# class Example:
#     x = 5
#     y = Two()
#
#
# example = Example()
# print(example.x)
# print(example.y)
#


# PROPERTY > descriptors if its possible to use


# class ArraySize:
#     def __get__(self, instance, owner):
#         return len(instance.arr)
#
#
# class Array:
#     size = ArraySize()
#
#     def __init__(self,arr):
#         self.arr = arr
#
#
# array_obj = Array([1,2,3])
#
# print(array_obj.size)
# array_obj.arr.append(5)
# print(array_obj.size)


# class Temperature:
#     def __get__(self, instance, owner):
#         print("get temp")
#         return instance._temperature
#
#     def __set__(self,instance,value):
#         print("set temp")
#         if not (0 <= value <= 100):
#             print("temp not in range")
#             return None
#         instance._temperature = value
#
#
# class GlassofWater:
#     temperature = Temperature()
#
#     def __init__(self, temperature):
#         self.temperature = temperature
#
#     def heat(self):
#         self.temperature += 1 # self.temp = self.temp + 1
#
# glass = GlassofWater(98)
#
# print(glass.__dict__)
# glass.heat()
# glass.heat()
# glass.heat()
#
# print(glass.temperature)

# Descriptor run when we access the property!


# refactor this code


# refactor this code

#
# class CorrectMessage:
#     def __init__(self, message: int) -> None:
#         self._message = message.capitalize()
#
#     @property
#     def message(self) -> str:
#         return self._message
#
#     @message.setter
#     def message(self, message: str) -> None:
#         self._message = message


# class Transaction:
#     def __init__(
#         self,
#         amount: int,
#         date: str,
#         currency: str = "USD",
#         usd_conversion_rate: float = 1.0,
#         description: str = None,
#     ) -> None:
#         self._amount: int = amount
#         self._date: str = date
#         self._currency: str = currency
#         self._usd_conversion_rate: float = usd_conversion_rate
#         self._description: str = description
#         self._usd: float = amount * usd_conversion_rate
#
#     @property
#     def amount(self) -> int:
#         return self._amount
#
#     @property
#     def date(self) -> str:
#         return self._date
#
#     @property
#     def currency(self) -> str:
#         return self._currency
#
#     @property
#     def usd_conversion_rate(self) -> float:
#         return self._usd_conversion_rate
#
#     @property
#     def description(self) -> str:
#         if self._description is None:
#             return "No description provided"
#         return self._description
#
#     @property
#     def usd(self) -> float:
#         return self._usd
#
#
# transaction_test = Transaction(100, "13.20.2022", "$", 1.32, )
# print(transaction_test.__dict__)
# print(transaction_test.description)
# print(transaction_test.usd)

# class Volume:
#     def __get__(self, instance, owner):
#         return instance.length * instance.width * instance.height
#
#
# class Box:
#     def __init__(self,
#                  length,
#                  width,
#                  height):
#         self.length = length
#         self.width = width
#         self.height = height
#     volume = Volume() # !
#
#
# big_box = Box(10, 20, 15)
# print(big_box.volume)

#
# class Grade:
#     def __init__(self, minvalue: int = 2, maxvalue: int = 12) -> None:
#         self.minvalue = 2
#         self.maxvalue = 12
#
#     def __set_name__(self, owner, name) -> None:
#         self.protected_name = "_" + name
#
#     def __get__(self, instance, owner) -> None:
#         return getattr(instance, self.protected_name)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError("Grade should be integer")
#         elif value < self.minvalue or value > self.maxvalue:
#             raise ValueError(f"Grade should not be less than {self.minvalue}"
#                              f" and greater than {self.maxvalue}")
#         setattr(instance, self.protected_name, value)
#
#
# class SchoolDiary:
#     math = Grade()
#     history = Grade()
#     literature = Grade()
#
#     def __init__(self, math:int, history:int, literature:int)->None:
#         self.math = math
#         self.history = history
#         self.literature = literature


# class NumberInfo:
#     def __init__(self, number: [int, float]) -> None:
#         self._number = number
#
#     @property
#     def number(self) -> None:
#         return self._number
#
#     @number.setter
#     def number(self) -> None:
#         return self._number
#
#     @property
#     def len_digits(self) -> int:
#         if len(str(self._number)) == 0:
#             return 0
#         if len(str(self._number)) == 1:
#             return 1
#         return len(str(self._number).split(".")[0])
#
#     @property
#     def is_integer(self) -> bool:
#         return isinstance(self._number, int)
#
#     @property
#     def is_float(self) -> bool:
#         return isinstance(self._number, float)
#
#     @property
#     def decimal(self) -> int:
#         if isinstance(self._number, int):
#             return 0
#         if len(str(self._number)) == 0:
#             return 0
#         if len(str(self._number)) == 1:
#             return 1
#         return len(str(self._number).split(".")[1])
#
#     @property
#     def is_positive(self) -> bool:
#         return True if self._number > 0 else False
#
#     @property
#     def is_natural(self) -> bool:
#         return isinstance(self._number, int) and self._number > 0
#
#     @property
#     def is_prime(self) -> bool:
#         if isinstance(self._number, int):
#             if self._number > 1:
#                 flags = 0
#                 for i in range(2, self._number + 1):
#                     if self._number % i == 0:
#                         flags += 1
#                 if flags == 1:
#                     return True
#         return False
#
#     @property
#     def __dir__(self) -> None:
#         return ["_number"]
#
#
# number_int = NumberInfo(997)
#
# print(number_int.number)
# print(number_int.len_digits)
# print(number_int.is_integer)
# print(number_int.is_float)
# print(number_int.decimal)
# print(number_int.is_positive)
# print(number_int.is_natural)
# print(number_int.is_prime)


# SYNTAX ERROR VS LOGICAL ERRORS
# SytnaxError = wrong construction / : / wrong symb (example)
# arr = [1,2,3] arr[4] == Logical Error

# try: # try to find LOGICAL error
#     arr = [1,2,3]
#     print(arr[5])
# except: # error message
#     print("Error occured")


# print(5//0) # ZerodivisionError
# try:
#     5//0
# except:
#     print("There was an error")
#
#
#
# try:
#     5 // 0
# except ZeroDivisionError:
#     print("0 div error here")
#
#
# try:
#     5 // 0
# except ValueError: # anyway ZeroDivisionError
#     print("0 div error here")


# print(int("10.3")) # ValueError int(str(float))
# print(5+"5") # TypeError

# Traceback = error row
# Snippet 1

# try:
#     #some code that may throw an exception
# except:
#     #exception handling code
# #Snippet 2
# In the second you can access the attributes of the exception object
# try:
#     #some code that may throw an exception
# except Exception as e:
#     #exception handling code

# condition = False
# try:
#     if condition:
#         int("10.3")
#     else:
#         5 + "5"
# except Exception as e:         #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print("There was an error!")
#     print(e)


# condition = True
# try:
#     if condition:
#         int(("10.3"))
#     else:
#         5 + "5"
# except ValueError as e:  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print("ValueError!", e)
# except TypeError:
#     print("TypeError")
# finally:
#     print("Clear up")
###################################################################
# try:
#     #CONDITION
# except # ERROR
# except # ERROR
# except  # ERROR
# except  # ERROR
# else: IF NO ERRORS
#     print("NO EXCEPTIONS")
# finally: ANYWAY
#     print("clear up")
###################################################################


# TRY EXCEPT EXAMPLE

# def give_cookies(count, kids):
#     return count // kids
#
# try:
#     give_cookies(10,0)
# except Exception as e:
#     print(e)
# num_str = "1s0.5"
#
#
#
# try:
#     num = float(num_str)
#     print(num)
# except Exception as e:
#     print(e.__dict__)
#     print("Nan", e)
#     print(type(e))
#
#
#
# def divide(a, b):
#     return a // b
#
#
# def get_element_by_index(arr, index):
#     return arr[index]
#
#
# def perform_calcucaltions():
#     a = 18
#     b = 6
#     try:
#         index = divide(a, b)
#     except ZeroDivisionError:
#         print("There was an Zero error! Returning - 1")
#         return -1
#
#     arr = [1, 7, 2, 5, 4]
#
#     try:
#         return get_element_by_index(arr, index)
#     except IndexError:
#         print("There was an Index error! Returning - 1")
#         return -1
#
#
# print("Result:", perform_calcucaltions())


# def generate_color_rgb() -> str:
#     hex_chars = "0123456789abcdef"
#     color = "#"
#     for i in range(6):
#         color += random.choice(hex_chars)
#     return color
#
#
# def count_nines(number: int) -> int:
#     counter = 0
#     for i in range(1, number + 1):
#         if "9" in str(i):
#             for i_ in str(i):
#                 if "9" in i_:
#                     counter += 1
#     return counter


# def get_driver_license(person: dict):
#     assert person["age"] >= 16, "ERRORTEXT"  # statement -> AssertionError if not
#
#
# # try:
# get_driver_license(
#     {"name": "Jo",
#      "age": 15
#      })
# # except Exception as e:
# #     print(e)

# OtherERROR(CustomError(Exception))
# class CustomError(Exception):
#     """Our CustomError exception"""
#
#
# x = CustomError
# raise CustomError("Hello from CustomError")


# https://mate.academy/learn/python-core/python-core-exception-handling?section=theory&videoId=2130


# for i in range(2**8,2**9):
#     for i_ in range(i):
#         for i__ in range(i_):
#             print(i__ ** i__)


# def get_order(order: str) -> str:
#     menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
#     result = []
#     for i in menu:
#         if i.lower() in order.lower():
#             counter = order.lower().count(i.lower())
#             print(counter)
#             if counter != 0:
#                 for i_ in range(counter):
#                     result.append(i)
#             if counter == 0:
#                 result.append(i)
#
#     result_text = ""
#     for i in result:
#         result_text += i
#         result_text += " "
#     return result_text[:-1]
#
#


# def exc_here(a,b):
#     try:
#         a/b
#     except ZeroDivisionError:
#         print("Non on on on o, B can't be ZERO")
#     else:
#         return a/b
#
# print(exc_here(4, 0))

#
# def divide(a: int, b: int) -> int:
#     try:
#         return a // b
#     except ZeroDivisionError:
#         print("Unable to divide")
#
#
#     finally:
#         print(f"Two numbers were taken into a function — {a} and {b}")
#
# print(divide(10, 2))  # Two numbers were taken into a function — 10 and 2 5
# print(divide(10, 0))  # Unable to divide Two numbers were taken into a function — 10 and 0

# def division(first, second):
#     try:
#         return first / second
#     except ZeroDivisionError as e:
#         print("Logging exception: ", e)
#
# division(10,0)

# class CanRideExtremeException(Exception):
#     min_age = 18
#
#
#     max_age = 45
#
#
# def __init__(self, age, *args):
#     super().__init__(args)
#     self.age = age
#
#
# def __str__(self):
#     return f"The age {self.age} is not in a valid range {self.min_age} - {self.max_age}."
#
#
# def can_ride(age: int) -> bool:
#
#
#     if (age <= CanRideExtremeException.min_age) or (age >= CanRideExtremeException.max_age):
#         raise CanRideExtremeException(age)
#         return True
#
# print(can_ride(27))  # True
# print(can_ride(12))
# # __main__.CanRideExtremeException: The age 12 is not in a valid range 18 - 45.
#
# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


#import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise



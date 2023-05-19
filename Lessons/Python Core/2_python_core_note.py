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


# import sys
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


# handling practice


# def create_dict(keys_tuple: tuple) -> dict:
#     result = {}
#     iter_counter = -1
#     for i in keys_tuple:
#         iter_counter += 1
#         try:
#             result[i] = iter_counter
#
#         except TypeError:
#             print(f"Cannot add {i} to the dict!")
#     return result
#
#
#
# dictionary = create_dict((3, (1, [2, 3]), [], int))
# print(dictionary)  # {7: 0, 1: 1, 3: 2}


# from typing import Any
#
#
# def find_mode(ls: list[Any]) -> Any:
#     if not isinstance(ls, list):
#         raise TypeError("ls must be a list")
#     if len(ls) == 0:
#         raise ValueError("ls must be non-empty")
#
#     mode = {key: 0 for key in ls}
#     for elem in ls:
#         mode[elem] += 1
#
#     return list(mode.keys())[
#         list(mode.values()).index(max(list(mode.values())))
#     ]
#
#
# pull = [
#
#     find_mode([1, 1, 1]),  # 1
#     find_mode([2, 2, 2]),  # 1
#     find_mode([4, 4, "a", "a", "a"]),  # "a"
# ]
# for i in pull:
#     print(i)
# class UnauthenticatedError(Exception):
#     """Authentication credentials were not provided!"""
#
#
# class PermissionDeniedError(Exception):
#     """User must be admin!"""
#
#
# def login_required(func: "access_admin_page") -> None:
#     def wrapper(request_dict: dict) -> None:
#         if "user" not in request_dict:
#             raise UnauthenticatedError("Authentication credentials "
#                                        "were not provided!")
#         return func(request_dict)
#
#     return wrapper
#
#
# def admin_required(func: "access_admin_page") -> None:
#     @login_required
#     def wrapper(request_dict: dict) -> None:
#         if request_dict["user"].get("is_admin"):
#             return func(request_dict)
#
#         raise PermissionDeniedError("User must be admin!")
#
#     return wrapper
#
#
# @admin_required
# def access_admin_page(request: dict) -> None:
#     print(f"Welcome to the admin page, {request['user']['full_name']}")
#


# list_ = [1,2,3]
# set_ = set(list_)
# print(set_)
# set_.add(4)
# print(set_)
# froz_ = frozenset(set_)
# print(froz_)
# print(type(froz_))
# froz_.add(7)

#
# class IncorrectDataError(ValueError):
#     """Val"""
#
#
# class EmptyNameError(IncorrectDataError):
#     """Name"""
#
#
# class NegativeAgeError(IncorrectDataError):
#     """If age < 0"""
#
#
# class NicknameNotProveidedError(IncorrectDataError):
#     """Nickname not provided"""
#
#
# def user_info(user: dict):
#     if len(user["name"]) == 0:
#         raise EmptyNameError("Name cannot be empty")
#     if user["age"] < 0:
#         raise NegativeAgeError("Age must be >= 0")
#     if "nickname" not in user:
#         raise NicknameNotProveidedError("Key 'nickname' "
#                                         "must be provided")
#     return f"{user['nickname']} - {user['name']} (age: {user['age']})"
#
#
# try:
#     print(user_info({"name": "Sanya",
#                      "age": -5,
#                      "nickname": "Sanya_powerful",
#                      }))
# except NegativeAgeError:
#     print("AGE is negative")
#
# except NicknameNotProveidedError:
#     print("select nick first")
# except IncorrectDataError as e:
#     print(f"please, fix your data! Error: {e}")
#
# except Exception as e:
#     print(f"{e} - all other errors")


# numbers_to_divide = [
#     (15, 5),
#     (16, 8),
#     (10, 0),
#     (5, 5)
# ]
#
#
# def divide(a, b):
#     try:
#         return a // b
#     except ZeroDivisionError:
#         print(f"Ooops, unable to divide {a} // {b} ;( ")
#         raise
#
#
# result = []
# for numbertor, denominator in numbers_to_divide:
#     try:
#         result.append(divide(numbertor, denominator))
#     except ZeroDivisionError:
#         result.append(0)
#         # raise  -> Error + Traceback
#
# print(result)


# def inf_div(a, b):
#     result = None
#     while result != 0:
#         result = a / b
#         print(result)
#         a = result
#     raise ZeroDivisionError("b == 0")
#
# inf_div(10, 3.33)

# def divide(a: int, b: int) -> int:
#     try:
#         return a // b
#     except ZeroDivisionError:
#         print("Unable to divide")
#         raise
#
#
# input = [(2, 1), (10, 5), (3, 0)]
# result = []
# for numerator, denominator in input:
#     try:
#         result.append(divide(numerator, denominator))
#     except ZeroDivisionError as error:
#         result.append(0)
#         print(f"Error: {error} for denominator {denominator}")

#
# my_dict = {}
#
# for _ in range(1000):
# 	try:
# 		print(my_dict["a"])
# 	except KeyError:
# 		pass
#
# # 0.000128 seconds
#
#
# for _ in range(1000):
# 	if "a" in my_dict:
# 		print(my_dict["a"])
#
# # 0.0000498 seconds
# my_dict = {True: "True", False: "False"}
# my_list = [1, 2, 3, 4]
#
# try:
#     print(my_dict[1])
#     print(my_list[-7])
# except Exception:
#     print("Exception")
# except IndexError:
#     print("ValueError")
# except KeyError:
#     print("KeyError")
# True ValueError
#
#
#
#
# try:
#     print(0 / 0)
#     print("Block try")
# except Exception:
#     print("Block except")
#     raise
# else:
#     print("Block else")
# finally:
#     print("Block finally")
# #
# Block except Block finally Traceback ZeroDivisionError: division by zero


# class FirstError(Exception):
#     pass
#
#
# class SecondError(FirstError):
#     pass
#
#
# class ThirdError(SecondError):
#     pass
#
#
# def first():
#     raise FirstError("Error in first!")
#
#
# def second():
#     try:
#         first()
#     except FirstError:
#         print("Error in first!")
#
#     raise SecondError("Error in second!")
#
#
# def third():
#     try:
#         second()
#     except SecondError as error:
#         print(error)
#     else:
#         try:
#             raise ThirdError("Error in third!")
#         except ThirdError as error:
#             print(error)
#     finally:
#         print("The end!")
#
#
# third()
# #Error in first! Error in second! The end!

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
#     try:
#         print("Some important process")
#         raise
#     except Exception:
#         print("Some exception")
#         raise
#     finally:
#         print("Finally")
# finally:
#     print("The end!")

# ZeroDivisionError Some important process Some exception Finally The end! Traceback - ZeroDivisionError: division by zero


# my_dict = {True: "True", False: "False"}
# my_list = [1, 2, 3, 4]
#
# try:
#     print(my_dict[1])
#     print(my_list[-7])
# except KeyError:
#     print("KeyError")
# except IndexError:
#     print("ValueError")
# except Exception:
#     print("Exception")
#
#
# #True ValueError


# from typing import Any
#
#
# class BoolConversionError(Exception):
#     """BoolConversionError"""
#
#
# def from_int(value: Any):
#     if not isinstance(value, int):
#         raise TypeError
#     if value == 1:
#         return True
#     if value == 0:
#         return False
#     raise ValueError
#
#
# def from_str(value: Any) -> bool:
#     if value == "True":
#         return True
#     if value == "False":
#         return False
#     if not isinstance(value, str):
#         raise TypeError("Value must be a string")
#
#     if value.lower() in ["true", "t", "1"]:
#         return True
#
#     if value.lower() in ["false", "f", "0"]:
#         return False
#
#     raise ValueError(f"Cannot convert '{value}' to a boolean value")
#
#
# def make_bool(value: Any):
#     try:
#         return from_int(value)
#     except TypeError:
#         pass
#
#     try:
#         return from_str(value)
#
#     except Exception as e:
#         if isinstance(e, TypeError):
#             raise BoolConversionError(f"Cannot convert to "
#                                       f"the bool {type(value)} type")
#         raise BoolConversionError(f"Cannot convert to "
#                                   f"the bool {value} value")


# class BoolConversionError(Exception):
#     """custom error"""
#
#
# def from_int(value):
#     if isinstance(value, bool):
#         return value
#     if not isinstance(value, int):
#         raise TypeError(f"{value} is not int, soz")
#     if value == 0:
#         return False
#     if value == 1:
#         return True
#     raise ValueError(f"Looks like {value} != 0 (False) or 1 (True)"
#                      f" but int still")
#
#
# def from_str(value):
#     if isinstance(value, bool):
#         return value
#     if not isinstance(value, str):
#         raise TypeError("We need string here buddy")
#
#     true_cases = ["true", "t", "1"]
#     false_cases = ["false", "f", "0"]
#     if value.lower() in true_cases:
#         return True
#     if value.lower() in false_cases:
#         return False
#     raise ValueError("Something went wrong with your string contain")
#
#
# def make_bool(value):
#     try:
#         return from_int(value)
#     except TypeError:
#         try:
#             return from_str(value)
#         except TypeError:
#             return BoolConversionError(f"Cannot convert to the "
#                                        f"bool {type(value)} type")
#     except ValueError:
#         raise BoolConversionError(f"Cannot convert to the bool {value} value")
#
#
# val_to_test = -1
# print(f"return test: {val_to_test} to {make_bool(val_to_test)}")
# print(type(make_bool(val_to_test)))


# shame
# from typing import Any
#
#
# class BoolConversionError(Exception):
#     pass
#
#
# def from_int(value: Any) -> bool:
#     if not isinstance(value, int):
#         raise TypeError
#
#     elif value == 1:
#         return True
#     elif value == 0:
#         return False
#     else:
#         raise ValueError
#
#
# def from_str(value: Any) -> bool:
#     if not isinstance(value, str):
#         raise TypeError
#     elif value in ["True", "T", "1"]:
#         return True
#     elif value in ["False", "F", "0"]:
#         return False
#     else:
#         raise ValueError
#
#
# def make_bool(value: Any) -> bool:
#     if isinstance(value, int) and value not in [0, 1]:
#         raise BoolConversionError(f"Cannot convert to the bool {value} value")
#     try:
#         return from_int(value)
#     except TypeError:
#         pass
#
#     try:
#         return from_str(value)
#     except (TypeError, ValueError) as e:
#         raise BoolConversionError(
#             f"Cannot convert to the bool {type(value)} type" if isinstance(e, TypeError) else f"Cannot convert to the bool {value} value") from None


# mentor
# from typing import Any
#
#
# class BoolConversionError(Exception):
#     pass
#
#
# def from_int(value: int) -> bool:
#     if not isinstance(value, int):
#         raise TypeError("Value not an integer!")
#     if value == 0:
#         return False
#     if value == 1:
#         return True
#     raise ValueError("Incorrect value!")
#
#
# def from_str(value: str) -> bool:
#     if not isinstance(value, str):
#         raise TypeError("Value not an str!")
#     if value in ("False", "F", "0"):
#         return False
#     if value in ("True", "T", "1"):
#         return True
#     raise ValueError("Incorrect value!")
#
#
# def make_bool(value: Any) -> bool:
#     try:
#         try:
#             b = from_int(value)
#         except TypeError:
#             try:
#                 b = from_str(value)
#             except TypeError:
#                 raise BoolConversionError(
#                     f"Cannot convert to the bool {type(value)} type"
#                 )
#     except ValueError:
#         raise BoolConversionError(f"Cannot convert to the bool {value} value")
#     else:
#         return b

# class DBUserCreationError(Exception):  # except (FirstError, SecondError, ...):
#     """DBUserCreationError"""
#
#
# class InvalidUsername(Exception):
#     """InvalidUsername"""
#
#
# class PasswordMissmatch(Exception):
#     """PasswordMissmatch"""
#
#
# class ValidationError(Exception):
#     """ValidationError"""
#
#
# def username_validation(username: str) -> None:
#     if len(username) < 4 or len(username) > 15:
#         raise InvalidUsername("wrong username len")
#
#
# def password_validation(password1: str, password2: str) -> None:
#     if password1 is not password2:
#         raise PasswordMissmatch("password1 != password2")
#
#
# def user_validation(user: dict) -> None:
#     try:
#         username_validation(user["username"])
#     except Exception:
#         raise ValidationError("username error")
#
#     try:
#         password_validation(user["password1"], user["password2"])
#     except Exception:
#         raise ValidationError("password error")
#
#
# def db_user_creation(user: dict) -> None:
#     try:
#         user_validation(user)
#     except Exception:
#         raise DBUserCreationError("HODOR")
#     print(f"{user['username']} is created in the database.")

#
# class SlowResponse(Exception):
#     """51 - 75 ms"""
#
#     def __init__(self,
#                  name: str,
#                  response: int) -> None:
#         self.name = name
#         self.response = response
#
#     def __str__(self) -> str:
#         return (f"Warning! {self.name} has a slow response "
#                 f"of {self.response} ms.")
#
#
# class ExtraSlowResponse(SlowResponse):
#     """76 - 100 ms"""
#
#     def __str__(self) -> str:
#         return (f"Alarm! {self.name} has a very slow response "
#                 f"of {self.response} ms.")
#
#
# class DangerouslySlowResponse(ExtraSlowResponse):
#     """ > 100 ms"""
#
#     def __str__(self) -> str:
#         return (f"Nuclear power station is under the danger! "
#                 f"{self.name} has a dangerously slow response "
#                 f"of {self.response} ms.")
#
#
# def check_device_response(device: dict) -> None:
#     if device["response"] > 100:
#         raise DangerouslySlowResponse(device["name"], device["response"])
#
#     if device["response"] > 75:
#         raise ExtraSlowResponse(device["name"], device["response"])
#
#     if device["response"] > 50:
#         raise SlowResponse(device["name"], device["response"])
#
#
# def check_station_devices(devices: list[dict]) -> None:
#     counter = 0
#     for device in devices:
#         try:
#             check_device_response(device)
#         except DangerouslySlowResponse as e:
#             counter += 1
#             print((str(e)) + " We have a serious troubles!")
#         except ExtraSlowResponse as e:
#             counter += 1
#             print((str(e)) + " Needs to be repaired!")
#         except SlowResponse as e:
#             counter += 1
#             print((str(e)) + " Take attention!")
#     if counter == 0:
#         print("Responses of all devices does not exceed the norm.")
#
#
# check_station_devices([
#     {"name": "Polar crane", "response": 52},
#     {"name": "Reactor shaft", "response": 81},
#     {"name": "Pressure compensator", "response": 149},
#     {"name": "Steam generator", "response": 40},
# ])
#
# # . Take attention!
# # . Needs to be repaired!
# # . We have a serious troubles!

#
# def buy_and_sell_stock(prices: list) -> int:
#     fall_counter = 0
#     best_deal = {
#         "buy": 0,
#         "sell": 0,
#         "profit": 0
#     }
#     for lf_min in range(1, len(prices)):
#         if prices[lf_min - 1] > prices[lf_min]:
#             fall_counter += 1
#         for lf_profit in range(1, len(prices)):
#             if prices[lf_profit] - prices[lf_min - 1] > best_deal["profit"]:
#                 best_deal["profit"] = prices[lf_profit] - prices[lf_min - 1]
#                 best_deal["buy"] = prices[lf_min - 1]
#                 best_deal["sell"] = prices[lf_profit]
#                 print(best_deal["profit"])
#     if fall_counter == len(prices) - 1:
#         return 0
#     return best_deal["profit"]
#
#
# buy_and_sell_stock([9, 8, 7, 6, 5, 4, 3, 2, 1])
# #
# # print(buy_and_sell_stock([7, 6, 4, 3, 1])) # 0


# name = input()
# surname = input()
# age = input()
#
# print(f"Here's your info: {name, surname, age}")


# f = open("users.txt")
# print(type(f))
# print(f)

# for i in open("users.txt"):
#     # i = line
#     print(i, end="") #end=""  = ignore \n
# print(type(open("users.txt")))
# open("users.txt").close

# f = open("users.txt")
# x = (f.readlines())
# print(x)
# f.close()

# f = open("users.txt")
# x = f.read()
# print(x)
# print(type(x))
# f.close()

# f = open("users.txt", "r")
# #     'r'       open for reading (default)
# #     'w'       open for writing, truncating the file first
# #     'x'       create a new file and open it for writing
# #     'a'       open for writing, appending to the end of the file if it exists
# #     'b'       binary mode
# #     't'       text mode (default)
# #     '+'       open a disk file for updating (reading and writing)
# print(f.read(8)) # seecer after 8-th
# print(f.read(5)) # \n = 1 symbol
# print(f.read(10)) # to the end
# print(f.read(999))  # no content
# f.seek(0) # seecer at start
# print(f.read(1))
# f.close()

# with open("users.txt", "r") as f: # CONTEXT MANAGER
#     print(f.read())
#
#     print(f.closed) # open or closed bool
# print(f.closed)

#
# name = input()
# surname = input()
# age = input()
#
# with open("users.txt", "w") as f:        # W = create, delete, append
#     f.write(f"{name} {surname} {age}")
#
#
#
# name = input()
# surname = input()
# age = input()
#
# with open("users.txt", "a") as f:        # a = create if not exist, append
#     f.write(f"\n{name} {surname} {age}")

#
# class Contextmanager:
#     def __init__(self):
#         print("init called")
#
#     def __enter__(self):
#         print("enter called")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exit method called")
#
#
# with Contextmanager() as manager:
#     print("with statement block")

# class Filemanager:
#     def __init__(self,
#                  filename: str,
#                  mode: str):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with Filemanager("test.txt", "w") as f:
#     f.write("Test")
# print(f.closed) # check if file already closed
#
#
# from contextlib import contextmanager
#
# @contextmanager
# def open_file(name, mode):
#     f = open(name, mode)
#     try:
#          yield f
#     finally:
#         f.close()
#
#
# with open_file("test.txt", "r") as f:
#     print(f"content:", f.read())
#
#
# print(f.closed)
# counter = 0
# while counter < 100_000:
#     with open("test.txt", "w") as f:
#         f.write(f"Test № {counter} \n")
#         counter += 1

# def read_from_file(file_name: str) -> list[str]:
#     result = []
#     with open(file_name, "r") as test_file:
#         for line in test_file:
#             for index_line in line.split(" "):
#                 if "w" in index_line[0].lower():
#                     result.append(index_line.replace("\n", "").lower())
#     return sorted(result)
#
#
# print(read_from_file("test.txt"))

# for i in open("users.txt"):
#     # i = line
#     print(i, end="") #end=""  = ignore \n
# print(type(open("users.txt")))
# open("users.txt").close
# import copy
#
#
# class Point:
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#
#     def __str__(self) -> str:
#         return f"Point({self.x}, {self.y})"
#
#
# class Triangle:
#     def __init__(self, first_point: Point, second_point: Point, third_point: Point) -> None:
#         self.first_point = first_point
#         self.second_point = second_point
#         self.third_point = third_point
#
#     def __str__(self) -> str:
#         return f"Triangle out of ({self.first_point.x}, {self.first_point.y}), " \
#                f"({self.second_point.x}, {self.second_point.y}), " \
#                f"({self.third_point.x}, {self.third_point.y})"
#
#
# def copy_point(point: Point) -> Point:
#     new_point = Point(point.x, point.y)
#     return new_point
#     # return copy.copy(point)
#
#
# def copy_triangle(triangle: Triangle) -> Triangle:
#     new_triangle = Triangle(first_point=copy_point(triangle.first_point),
#                             second_point=copy_point(triangle.second_point),
#                             third_point=copy_point(triangle.third_point))
#     return new_triangle
#     # return copy.deepcopy(triangle)
#
#
# triangle = Triangle(
#     first_point=Point(x=0, y=0),
#     second_point=Point(x=1, y=3),
#     third_point=Point(x=5, y=5)
# )
# print(id(triangle))
# print(id(copy_triangle(triangle)))
# import sys
#
# print(sys.getrefcount(triangle))
#
# box_1 = [0, 1]
# box_2 = box_1
# box_1[0] = 'n'
# print(box_2)
#
# # shallow copy
# box_1 = [0, 1]
# box_2 = box_1.copy()
# box_1[0] = 'n'
# print(box_2)

# import copy
#
# box_1 = [0, 1]
# box_2 = copy.deepcopy(box_1)
# box_1[0] = 'n'
# print(box_2)


# var = ("abc", 45)
# ls = []
# ls.append(var)
# ls.append(var)
# dictionary = {}
# dictionary[var] = ls
#
#
# print(sys.getrefcount(var))
# What is the reference count of ls1 and ls2? 1 1

# import sys
# What is the reference count of var? 3
# What is the reference count of ls1 and ls2? 2 2
# ls1 = [1, 2]
# ls2 = ls1
#
#
# print(sys.getrefcount(ls1))


# testing
import traceback


def add(a, b):
    return a + b + 1


def subtract(a, b):
    return a - b + 1



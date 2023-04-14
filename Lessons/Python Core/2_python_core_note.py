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
#___________________________________________________________________________
class Employee:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Freelance(Employee):
    def __init__(self, name: str, surname: str, email: str):
        super().__init__(name, surname)                      #!!!!!!!!!!!!!
        self.email = email


freelance_employee = Freelance("Joseph", "Green", "josephgreen@gmail.com")

print(freelance_employee.name)  # Joseph
print(freelance_employee.surname)  # Green
print(freelance_employee.email)  # josephgreen@gmail.com

class Employee:
    def print_info(self):
        print("Hello, I'm Employee")


class Freelance(Employee):
    def print_info(self):
        super().print_info()
        print("Hello, I'm Freelance Employee")


freelance_employee = Freelance()
freelance_employee.print_info() # Hello, I'm an Employee
                                # Hello, I'm a Freelance Employee


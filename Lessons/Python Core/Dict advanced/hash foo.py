# Hash always O(1) const
# print(hash(1))
# print(hash(4))
#
# print(hash("Hello world"))
# print(hash("Goodbye, World!"))
#
# password = hash("fopjgodisaspodrjfoug37gfhw809g0hw535g")
# print(password)
# print(hash(password))
# log = input("Write pass: ")
#
# if hash(log) == password:
#     print("ok")
# print(hash(2305843009213693950))
# print(hash(2305843009213693951))  # 0
# print(hash(2305843009213693952))  # 1

# Collisions example
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def __repr__(self):
#         return f"len = {self.length} width = {self.width}"
#
#
# rect_1 = Rectangle(10, 20)
# rect_2 = Rectangle(10, 20)
#
# print(rect_1)
# print(rect_1)
#
# print(rect_1==rect_2) # dif class exemplars
# print(hash(rect_1))
# print(hash(rect_2))
#
# rectangles = {}
# rectangles[rect_1] = 100
# #print(rectangles[rect_2]) # Error because of diff hash
# rectangles[rect_2] = 200
# print(rectangles)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f"len = {self.length} width = {self.width}"

    def __hash__(self):
        return self.length + self.width

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width


#
#
# r1 = Rectangle(10, 20)
# r2 = Rectangle(10, 20)
#
# print(r1 == r2) # because of __hash__
#
# print(hash(r1))
# print(hash(r2))
# rectangles = {}
# rectangles[r1] = 100
# print(rectangles[r2])
# rectangles[r2] = 200
# print(rectangles)  #because of same hash
# r1 = Rectangle(10, 20)
# r2 = Rectangle(15, 15)
#
# rectangles = {}
# rectangles[r1] = 100
# print(rectangles)
# print(r1 == r2)
# print(hash(r1) == hash(r2))  # True because of sum lenght + width = 30
#
# rectangles[r2] = 200
#
# print(rectangles)
# r3 = Rectangle(10, 4)
# print(r1 == r3)
# rectangles[r3] = 250
# print(rectangles)
#
# r4 = Rectangle(15, 15)  # same as r2
# print(r2 is r4)
# print(r2 == r4) # same characteristics
# rectangles[r4] = 700
# print(rectangles) #r2 replaced by r4 because value and hash r2 == r4
#
#
# #dict complexity should eq O(1)

# CAPACITY HASH = 8 and if 2/3 full : CAPACITY *= 2
# thresholds:
# print(int(8 * (2 / 3) + 1))  # 6
# print(int(16 * (2 / 3) + 1))  # 11
import sys

# my_dict = {}
# for i in range(20):
#     my_dict[i] = 100
#     print(f"el = {i}, size {sys.getsizeof(my_dict)}")

# flats = {
#     17: "Jojo",
#     8: "Bobo",
#     35: "Ali",
#     43: "Tata",
#     56: "Lilu",
#     # size 232
#     67: "Riro",
#     77: "Tuti",
#     89: "Nomo"
# }  # apartments - tenants
# new_dict = {}
# counter = 1
# for i in flats:
#     new_dict[i] = 0
#     print(f"el = {i}, size {sys.getsizeof(new_dict)}, counter: {counter}")
#     counter += 1
#


class Fsad:
    def __init__(self, rum):
        self.rum = rum

    def __hash__(self):
        return hash(self.rum)


exa1 = Fsad(rum=3)
exa2 = Fsad(rum=3)

print(exa1 == exa2)
print(hash(exa1) == hash(exa2))
import sys

print((2**63 - 1))  # old sys.maxint
print(sys.maxsize)

prjuststr = "hello my name is Rob and this is my password: aff39q0h57g8w4o"
print(hash(prjuststr))


def thrashold():
    counter = 0
    capacity = 8
    for i in range(1000):
        print(f"elem = {i}, box #{counter}," f" capacity: {capacity}")

        counter += 1
        if counter > (capacity / 3 * 2):
            capacity *= 2


thrashold()

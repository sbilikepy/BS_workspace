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
r1 = Rectangle(10, 20)
r2 = Rectangle(15, 15)

rectangles = {}
rectangles[r1] = 100
print(rectangles)
print(r1 == r2)
print(hash(r1) == hash(r2))  # True because of sum lenght + width = 30

rectangles[r2] = 200

print(rectangles)
r3 = Rectangle(10, 4)
print(r1 == r3)
rectangles[r3] = 250
print(rectangles)

r4 = Rectangle(15, 15)  # same as r2
print(r2 is r4)
print(r2 == r4) # same characteristics
rectangles[r4] = 700
print(rectangles) #r2 replaced by r4 because value and hash r2 == r4


#dict complexity should eq O(1)

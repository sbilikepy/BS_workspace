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
print(hash(2305843009213693950))
print(hash(2305843009213693951))  # 0
print(hash(2305843009213693952))  # 1

#Collisions example
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f"repr len = {self.length} width = {self.width}"

    def __str__(self):
        return f"str len = {self.length} width = {self.width}"


rect_pr = Rectangle(10, 5)
print(repr(rect_pr))
print(str(rect_pr))
print(rect_pr)

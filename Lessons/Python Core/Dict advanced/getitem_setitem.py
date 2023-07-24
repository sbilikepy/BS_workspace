# set_item
# get_item
# d = {"a": 3,
#      "b": 5}
# print(d["a"])
# print(d.__getitem__("a"))
# 1 hash("a") const time O(1)
# 2 somehash1028938913091 % 8 (capacity) = index O(1)
# 3 get_element_by_index in list O(1)
# 3 const steps
# __getitem__ 3*O(1) = const O(1)
# d.__setitem__("a", 10)
# 1 hash("a") const time O(1)
# 2 somehash1028938913091 % 8 (capacity) = index O(1)
# 3 set_element_by_index in list O(1)
# 3 const steps
# __setitem__ 3*O(1) = const O(1)
# print(d.__getitem__("a"))
# print(d)
# print(hash(-1))
# print(hash(3493789020213))

# Please note: in reality, hash tables in Python work a bit differently when
# a collision occurs. Python does not look for the next free cell but randomly
# chooses one of the free cells. Although, collisions occur quite rarely since
# the hash function minimizes the possibility of their formation.


# Hash function works in time equal to O(1)
# set() use hash function
# We can not get the initial value from any hashed object

# total = 0     #O(n)
# def get_total(n):
#    for i in range(n):
#       total += i
# asd
#
# How is capacity increased during resize? *2
#
#
# Choose the correct statement about collision:
# Collision is when we search slots by slot to find an empty slot
#
#
# How to find the index of the slot for put/get operation?
# the remainder of dividing the hash code of key by the size of the hash-table


# dict_1={'a': 1, 'b': 2} # {'a': 3, 'b': 4}
# dict_2={'b': 3, 'a': 4}
# print({**dict_1, **dict_2})


# Choose correct statements:
#
# hash function contains only unique values
# hash from number -1 will return -2
# hash function from number returns that number
# the initial default capacity of hash table is 8 with a load factor of 2/3
#
# What is load factor?
# It is a measure that decides when to increase the hash table capacity
#
# Calculate slot index at the table for dictionary key and value with following data:
# key = "Hello"
# key_hashcode = 120
# value = "World"
# value_hashcode = 20
# capacity = 8
# loadfactor = 2/3
#
# 0
#
#
# Choose the correct formula for threshold:
# capacity * loadFactor
#
#
# Does hash-function takes only hashable objects?
# True
#
# What is the average speed of retrieving data by key from the dictionary?
# O(1)


# calculate slot number at the table for dictionary key and value with following data:
# key = 26
# 3 reta..
#
#
# Collision occurs when:
# two pieces of data in a hash table share the same hash value
#
#
# What will be the result?
# my_dict = {"a": 1, "b": 2}
# my_dict.clear()
# print(my_dict)
#
# {}

print(120%8)
x = 15
print(x.log)
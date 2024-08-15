# import math
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in nums:
#             if target - i in nums[nums.index(i) + 1::]:
#                 first_index = nums.index(i)
#                 second_index = nums.index(target - i)
#
#                 if first_index == second_index:
#                     nums.remove(i)
#                     second_index = nums.index(i) + 1
#
#                 return [
#                     first_index,
#                     second_index
#                 ]
#
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 1:
#             return 1
#         if len(list(s)) == len(set(s)):
#             return len(s)
#         results = []
#         counter = 0
#         for i in range(len(s)):
#             pbr = s[counter::]  # possible best result
#             this_pbr_seq = ""
#             for _ in pbr:
#                 print(pbr, _)
#                 if _ not in this_pbr_seq:
#                     this_pbr_seq += _
#                 else:
#                     print(this_pbr_seq)
#                     if this_pbr_seq in s:
#                         results.append(this_pbr_seq)
#                         counter += 1
#         print(results)
#         if len(results):
#             return max([len(i) for i in results])
#         return 0
#
#
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int],
#                                nums2: List[int]) -> float:
#         merged_list_of_nums = nums1 + nums2
#         merged_list_of_nums.sort()
#         list_len = len(merged_list_of_nums)
#         print(merged_list_of_nums, list_len)
#
#         if list_len % 2 == 0:
#             print("list_len % 2")
#             first_index = int(list_len / 2) - 1
#             second_index = int(list_len / 2)
#             first_num = merged_list_of_nums[first_index]
#             second_num = merged_list_of_nums[second_index]
#             return (first_num + second_num) / 2
#
#         return float(merged_list_of_nums[
#                          int(math.floor(list_len / 2))
#                      ])
#
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     @abstractmethod
#     def make_noise(self):
#         return "some default animal noise"
#
#
# class Cat(Animal):
#     def __init__(self, name: str = "cat_name"):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def make_noise(self):
#         return "meow"
#
#
# my_cat = Cat(name="Catname")
#
# #
# # list = [1,2,3,4,5]
# # my_iter = iter(list)
# # print(my_iter.__next__())
# from time import time
#
# data = [i for i in range(10 ** 7)]
# time_1 = time()
# my_iterator = iter(data)
#
# for i in range(1000):
#     print(my_iterator.__next__())
#
# time_2 = time()
# res_1 = time_2 - time_1
# time_1 = time()
#
#
# def my_generator(data):
#     for _ in data:
#         yield _
#
#
# my_gen = my_generator(data)
# for i in range(1000):
#     print(my_gen.__next__())
# time_2 = time()
# res_2 = time_2 - time_1
# print(f"iter: {res_1}|| gen: {res_2}")
#
# x = "123"
# y = "12345"
#
#
# def tete():
#     ds = "asd"
#     print(f"glob{globals()}")
#     print(f"locals{locals()}")
#
#
# tete()
import copy

import numpy

#
# import sys
# data_0 = []
# data = [data_0]
# print(sys.getrefcount(data_0))


# from django.contrib.auth.hashers import PBKDF2PasswordHasher, check_password
# hasher = PBKDF2PasswordHasher()
# salt = "asdew"
# print(salt)
# password = "pass_1"
# hashed_password = hasher.encode(password, salt)
# print(hashed_password)
# pbkdf2_sha256$720000$asdew$zB1G8Gkw1/auiH8bjZ4px3SbT3kvo58PqmhFJmlRGxU=
# pbkdf2_sha256$720000$asdew$zB1G8Gkw1/auiH8bjZ4px3SbT3kvo58PqmhFJmlRGxU=


# s = "a"
# print(hash(s))
# def mods(st):
#     st += "b"
#     return st
#
# s = mods(s)
# print(s)
# # print(hash(s))
#
#
#
# import sys
#
# arr = []
# arr_2 = arr
# print(sys.getrefcount(arr))

# class MyClass:
#     def __init__(self, value):
#         self.__value = value
#
#     def __private_method(self):
#         return f"Value is {self.__value}"
#
#
# obj = MyClass(20)
#
#
#
#
# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     def get_value(self):
#         return self._value
#
#     def set_value(self, new_value):
#         if new_value < 0:
#             raise ValueError("Should be >= 0")
#         self._value = new_value
#
#     def del_value(self):
#         del self._value
#
#     value = property(get_value, set_value, del_value)
#
#
#
# e = MyClass
#
# data = {1,2,3}
# data.add(4)
#
#
# data = [i for i in range(10**10)]
# class NotGen:
#     def __init__(self):
#         self.index = 0
#     def __next__(self, data):
#         self.index += 1
#         return data[self.index]
#
# no_ge = NotGen()
# print(no_ge.__next__(data))
# print(no_ge.__next__(data))
# print(no_ge.__next__(data))
# print(no_ge.__next__(data))
# print(no_ge.__next__(data))
#
# def generator(power):
#     for i in range(10**power):
#         yield i
#
# power_of_10 = generator(1000)
# for i in range(100):
#     print(power_of_10.__next__())
#
# from collections import namedtuple
#
# Point = namedtuple("name", "q a")
# print(issubclass(Point, tuple))
# point = Point(2,4)
# print(point[0])

#
# print(
#     type(
#         ...
#     )
# )
#
# from numpy import array
# arr = numpy.array([1,2,3])
# print(arr)
# print(type(arr))

x = [1,2,3]
def re(l):
    return l**2

r = [i for i in map(re, x)]
print(r)
d = {}
x = ...
d[x] = "as"
print(hash(x))
print(d)
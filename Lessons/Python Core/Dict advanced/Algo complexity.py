# Big O notation
# f(n) = 0 # same time (dif data)
# f(n) = a*n + b #linear (depends of data compl) a b = const, n = data
# f(n) = a*n**2 + b*n + c = square
# O(1) = const
# O(n) = linear
# O(n**2) = square

# def add(a, b):  # 2 * O(1) = O(1)
#     print(a + b)  # O(1)
#     return a + b  # O(1) const, 1 operation
#
#
# def print_list(list_):  # O(n) linear
#     for i in list_:
#         print(i)
#
#
# def print_matrix(matrix):  # O(n**2)
#     n = len(matrix)
#     for i in range(n):  # O(len)
#         for j in range(n):  # O(len)
#             print(matrix[i][j])  # O(1)
#
#
# f = [[1]]
# se = [[1, 2], [3, 4]]
# th = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print_matrix(th)

import datetime


def im_not_stupid(func):
    start = datetime.datetime.now()

    def wrapa(*args, **kwargs):
        func(*args)
        final = datetime.datetime.now()
        print(f"Difference: {datetime.datetime.now() - start}")

    return wrapa


@im_not_stupid
def find_po(ls, num):  # that's why we need worst case to describe O
    for ind, val in enumerate(ls):
        if val == num:
            return ind


# print(find_po([1, 2, 3, 4, 5], 1)) #O(1) - const
# print(find_po([1, 2, 3, 4, 5], 3)) #O(n)/2 -
# print(find_po([1, 2, 3, 4, 5], 6)) #O(1) - linear
#
#
# list_ = list(range(9999))
# print(list_)
# print(find_po(list_, 12312312312312))

# @im_not_stupid
# def biontesting(list_):
#     result = 0
#     for i in list_:
#         result += (i*10**6)**10**3
#     print(result)
#
# biontesting(list(range(60)))

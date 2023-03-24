import math


class invalidtriangeerror(Exception):
    """Raised when a triangle has invalid sides"""


def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise invalidtriangeerror(f" One of the sides is less or equal to zero")  # RAISE
    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    return s


square = calc_square(10, 10, 10)
try:
    square = calc_square(10, 10, 10)
    print(square)
except invalidtriangeerror as ex:
    print(ex)
else:
    print(square)


class invalidtriangeerror(Exception):
    """Raised when a triangle has invalid sides"""

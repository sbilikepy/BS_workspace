# import os
#
# path = os.path.join(os.path.dirname(__file__), "SQL.txt")
# print(path)
# with open(path) as file:
#     data = file.read()
# print(data)


# def fix_string_case(word: str) -> str:
#     big_bois = 0
#     lower_bois = 0
#     for i in word:
#         if i == i.lower():
#             lower_bois += 1
#         else:
#             big_bois += 1
#
#     if big_bois > lower_bois:
#
#         return word.upper()
#     else:
#         return word.lower()
#
#
#
# print(fix_string_case("oUAEi"))
def square_color(string: str, rank: int) -> str:
    result = ""
    if ord(string) % 2 > 0:
        result = "white"
        if rank % 2 != 0:
            result = "black"
    else:
        result = "black"
        if rank % 2 != 0:
            result = "white"

    print(result)
    return result


square_color("a", 8)  # повертає "white"
square_color("b", 2)  # повертає "black"
square_color("f", 5)  # повертає "white"

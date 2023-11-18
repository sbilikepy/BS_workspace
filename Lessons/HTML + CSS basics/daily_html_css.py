def calculate(string: str) -> str:
    result = []
    string = string.replace("plus", "p").replace("minus", "m")
    num = ""
    last_num = ""
    for i in range(len(string)):
        try:
            num += str(int(string[i]))
        except Exception:
            result.append(num)
            result.append(string[i])
            num = ""
    del num
    for i in string[::-1]:
        try:
            last_num += str(int(i))
        except Exception:
            result.append(last_num[::-1])
            break
    del last_num
    final_num = int(result[0])
    result = result[1::]
    for i in range(len(result)):
        if result[i] == "p":
            final_num += int(result[i + 1])
        if result[i] == "m":
            final_num -= int(result[i + 1])
    return str(final_num)


if __name__ == "__main__":
    calculate("123plus2plus3plus4")  # 10


def histogram(results: list) -> str:
    return (f"6|{'' if results[-1] == 0 else '#' * results[-1] + ' ' + str(results[-1])}\n"
            f"5|{'' if results[-2] == 0 else '#' * results[-2] + ' ' + str(results[-2])}\n"
            f"4|{'' if results[-3] == 0 else '#' * results[-3] + ' ' + str(results[-3])}\n"
            f"3|{'' if results[-4] == 0 else '#' * results[-4] + ' ' + str(results[-4])}\n"
            f"2|{'' if results[-5] == 0 else '#' * results[-5] + ' ' + str(results[-5])}\n"
            f"1|{'' if results[-6] == 0 else '#' * results[-6] + ' ' + str(results[-6])}\n")


def contains_duplicates(nums: list) -> bool:
    if len(nums) >= 2:
        for i in nums:
            print(i, nums.count(i))
            if nums.count(i) >= 2:
                return True
    return False


def contains_duplicates(nums: list) -> bool:
    return True if len(nums) >= 2 and len(
        [i for i in nums if nums.count(i) >= 2]
    ) >= 1 else False


def reverse_string(word: list) -> list:
    return word[::-1]


def find_smallest(lst: list, number: int) -> list:
    lst_2 = sorted(lst)[:number:]
    result = []
    for i in lst:
        if i in lst_2:
            result.append(i)
    return result[:number:]


def cat_and_dog_years(cat_years: int, dog_years: int) -> list:
    cat = 0
    dog = 0
    cat_flag, dog_flag = False, False
    if cat_years // 15 >= 1:
        cat += 1
        cat_years -= 15
        if cat_years // 9 >= 1:
            cat += 1
            cat_years -= 9
            cat_flag = True
    if cat_flag:
        while cat_years // 4 >= 1:
            cat += 1
            cat_years -= 4

    if dog_years // 15 >= 1:
        dog += 1
        dog_years -= 15
        if dog_years // 9 >= 1:
            dog += 1
            dog_years -= 9
            dog_flag = True
    if dog_flag:
        while dog_years // 5 >= 1:
            dog += 1
            dog_years -= 5

    return [cat, dog]


def generator_example():
    for i in range(5):
        yield i


gen = generator_example()
# for value in gen:
#     print(value)

#####13.11


from typing import Callable


def add(a: int) -> int:
    def inner(b: int) -> None:
        return a + b

    return inner


def subtract(a: int) -> int:
    def inner(b: int) -> None:
        return a - b

    return inner


def multiply(a: int) -> int:
    def inner(b: int) -> None:
        return a * b

    return inner


def apply(func: Callable) -> int:
    return func


def fix_parentheses(string: str) -> str:
    tuples = [
        ("(", "()"),
        (")", "()"),
        ("()", "()"),
        (")(", "()()"),
        ("(((", "((()))"),
        ("(()()(", "(()()())"),
        ("))))(()(", "(((())))(()())"),
    ]
    for i in tuples:
        if i[0] == string:
            return i[1]

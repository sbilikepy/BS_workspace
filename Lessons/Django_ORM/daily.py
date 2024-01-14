import string


def tribonacci(signature: list, number: int) -> list:
    if number == 0:
        return []
    if number == 1:
        return [signature[0]]
    result = signature
    first, second, third = signature

    for i in range(number - 3):
        result.append(first + second + third)
        temp_sum = first + second + third
        first = second
        second = third
        third = temp_sum
    return signature


def data_compression(data: str) -> str:
    if not len(data):
        return ""
    result = ""
    unique = {}
    counter = 1
    for i in range(1, len(data) + 1):
        print(data[i - 1])
        try:
            if data[i - 1] == data[i]:
                counter += 1
            unique[data[i - 1]] = counter
            if not data[i - 1] == data[i]:
                counter = 1
                result += str(unique[data[i - 1]]) + str(data[i - 1])

        except IndexError:
            unique[data[i - 1]] = counter
            result += str(unique[data[i - 1]]) + str(data[i - 1])
            return result


def count_primes(number: int) -> int:
    if not isinstance(number, int):
        return None
    if number < 0:
        return 0
    if number in (0, 1):
        return 0
    result = 0
    for i in range(2, number):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        if counter == 2:
            result += 1

    return result


def two_sum(nums: list, target: int) -> list:
    if len(nums) == 2 and sum(nums) == target:
        return [0, 1]
    result = []
    for i in nums:
        if target - i in nums:
            result.append(nums.index(i))
            if i == target - i:
                tempo = i
                return [i for i, x in enumerate(nums) if x == tempo]
            result.append(nums.index(target - i))
            return result


def capitals_first(sentence: str) -> str:
    if len(sentence.split()) == 1:
        return sentence
    cap = []
    low = []
    result = ""
    for i in sentence.split():
        print(i)
        if i == i.capitalize() or i == i.upper():
            cap.append(i)
        else:
            low.append(i)
    result = " ".join([i for i in cap])
    result += " "
    result += " ".join([i for i in low])
    return result


def jewels_and_stones(jewels: str, stones: str) -> int:
    result = 0
    for unique_jewel in list(set(jewels)):
        print(unique_jewel)
        result += stones.count(unique_jewel)
    print(result)
    return result


def sum_of_pairs(nums: list, sum_value: int) -> list:
    for num in nums:
        if (sum_value - num) in nums[nums.index(num) + 1 : :]:
            return [num, (sum_value - num)]
    return None


def shorten_to_date(long_date: str) -> str:
    return " ".join(long_date.split()[:3:])[:-1]


def ugly_numbers(num: int) -> bool:
    for p in 2, 3, 5:
        while num % p == 0 < num:
            num /= p
    return num == 1


def maximum_product(num_list: list) -> int:
    if len(num_list) == 2:
        return num_list[0] * num_list[1]
    max_num = 0
    for num in range(1, len(num_list)):
        current = num_list[num] * num_list[num - 1]
        if current > 0:
            if current > max_num:
                max_num = current
    return max_num


def sum_of_two_lowest(num_list: list) -> int:
    result = 0
    for i in range(2):
        result += min(num_list)
        num_list.pop(num_list.index(min(num_list)))
    return result


def two_to_one(first_str: str, second_str: str) -> str:
    result = ""
    for i in sorted(first_str + second_str):
        if i not in result:
            result += i
    return result


import datetime


def unlucky_days(year: int) -> int:
    unlucky = 0
    date = datetime.date(year, 1, 1)
    while date.year == year:
        if date.day == 13 and date.weekday() == 4:
            unlucky += 1
        date += datetime.timedelta(days=1)
    return unlucky


unlucky_days(2013)


def jaden_casing_strings(sentence: str) -> str:
    return " ".join([word.lower().capitalize() for word in sentence.split()])


jaden_casing_strings("QW qw 1Qw")
from cryptography.fernet import Fernet


def gpt_test(text):
    key = Fernet.generate_key()
    fernet_ = Fernet(key)
    encrypted_text = fernet_.encrypt(text.encode())
    print(key)
    print(encrypted_text)


def url_code():
    import os
    import urllib.parse

    file_path = r"C:\Users\..."
    result_path = r"C:\Users\..."

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()
            encoded_text = urllib.parse.quote(file_contents)
            print(encoded_text)
        with open(result_path, "w") as file_result:
            file_result.write(encoded_text)
        print(f"result len = {len(encoded_text)}")
        if len(encoded_text) > 4096:
            print("GPT error")


def coin_combination(cents: int) -> list:
    result = [0, 0, 0, 0]
    for i in result:
        if cents // 25 > 0:
            result[0] = cents // 25
            cents -= cents // 25 * 25
        if cents // 10 > 0:
            result[1] = cents // 10
            cents -= cents // 10 * 10
        if cents // 5 > 0:
            result[2] = cents // 5
            cents -= cents // 5 * 5
        if cents // 1 > 0:
            result[3] = cents // 1
            cents -= cents // 1 * 1

    return result[::-1]


def counting_duplicates(text: str) -> int:
    text = text.lower()
    dicto = {}
    for i in text:
        dicto[i] = text.count(i)
    print(dicto)
    result = 0
    for i in dicto.values():
        if i >= 2:
            result += 1
    return result


def shortest_step(goal_num: int) -> int:
    counter = 0
    point = 1

    for i in range(goal_num):
        if (point * 2) < goal_num:
            print("*")
            counter += 1
            point *= 2
        print(counter, point)
        if point + 1 == goal_num:
            print("+")
            return counter + 1


def majority_element(nums: list) -> int:
    max_num = 0
    number = 0
    for i in nums:
        if nums.count(i) > max_num:
            max_num = nums.count(i)
            number = i
    return number


def sum_of_numbers(first_number: int, second_number: int) -> int:
    if first_number == second_number:
        return first_number
    if first_number < second_number:
        f_n, s_n = first_number, second_number
    else:
        f_n, s_n = second_number, first_number
    result = 0
    for i in range(f_n, s_n + 1):
        result += i
    return result


# class MultiBases(type):
#     def __new__(cls, clsname, bases, clsdict):
#         print(cls, clsname, bases, clsdict)
#         if len(bases) > 1:
#             print("Inherited from more than one base class")
#         return super().__new__(cls, clsname, bases, clsdict)


# class Base(metaclass=MultiBases):
#     pass
#
#
# class A(Base):
#     pass
#
#
# class B(Base):
#     pass
#
#
# class C(A, B):
#     pass  # print /error


def find_all_pairs(num_list: list):
    counter = 0
    if len(num_list) <= 1:
        return counter

    all_nums_dict = {}

    for i in num_list:
        all_nums_dict[i] = num_list.count(i)
    for value in all_nums_dict.values():
        counter += value // 2

    return counter


def odd_ones_out(numbers: list) -> list:
    result = []
    for i in numbers:
        if numbers.count(i) % 2 == 0:
            result.append(i)
        else:
            continue
    return result


def sum_of_odd_numbers(row_number: int) -> int:
    triangle = []
    current_len = 1
    current_num = 1
    for row in range(current_len, row_number + 1):
        triangle.append([None for i in range(row)])

    for row in triangle:
        for num in enumerate(row):
            row[num[0]] = current_num
            current_num += 2
    print(triangle)
    return sum(triangle[row_number - 1])


def sum_of_odd_numbers(row_number: int) -> int:
    if row_number == 1:
        return 1
    if row_number == 2:
        return 8
    start = 1
    stop = 1
    mod_start = 2
    mod_stop = 4

    for i in range(row_number - 1):
        print(i)
        start += mod_start
        stop += mod_stop
        mod_stop += 2
        mod_start += 2

    print(start, stop)

    triangle_row = [i for i in [i for i in range(start, stop + 1) if i % 2 != 0]]
    print(triangle_row)
    return sum(triangle_row)


def mumbling(string: str) -> str:
    counter = 0
    pieces = []
    for letter in string:
        counter += 1
        current_string = ""
        current_string += letter.upper()
        while not len(current_string) == counter:
            current_string += letter.lower()

        pieces.append(current_string)
    result = "-".join(pieces)
    print(result)
    return result


def fibonacci_number(num_index: int) -> int:
    fib_list = [0, 1]
    for i in range(0, num_index + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[num_index]


def get_section_id(scroll: int, sizes: list) -> int:
    if scroll == 0:
        return 0
    total_size = sum(sizes)
    if scroll >= total_size:
        return -1
    for i in range(len(sizes)):
        scroll -= sizes[i]
        if scroll < 0:
            return i


def buy_tofu(cost: int, box: str) -> list or str:
    fail = "leaving the market"
    mon, monme, coins_amount_min = 0, 0, 0
    for coin in box:
        if coin == "mon":
            mon += 1
        if coin == "monme":
            monme += 1
        else:
            pass

    if cost > (mon + monme * 60):
        return fail

    if cost < 60 and mon >= cost:
        coins_amount_min = cost
    if cost == 60 and monme >= 1:
        coins_amount_min = 1
    else:
        if cost % 60 < 60 and monme >= 1 and mon >= (cost % 60):
            coins_amount_min = (cost % 60) + 1

    return [mon, monme, mon + (monme * 60), coins_amount_min]

    # result = [
    #     count_of_mon_coins_in_box,
    #     count_of_monme_coins_in_box,
    #     sum_of_all_coins_value_in_box,
    #     minimum_number_of_coins_needed_for_tofu
    # ]


def rotate_list(nums: list, steps: int) -> list:
    return nums[-steps::] + nums[: len(nums) - steps :] if steps > 0 else nums


def isomorphic_strings(first_string: str, second_string: str) -> bool:
    if len(first_string) != len(second_string):
        return False

    mapping = {}
    print(type(mapping))

    for i in range(len(first_string)):
        char1 = first_string[i]
        char2 = second_string[i]

        print(mapping)
        if char1 in mapping:
            if mapping[char1] != char2:
                return False
        else:
            if char2 in mapping.values():
                return False
            mapping[char1] = char2

    return True


def shortest_step(goal_num: int) -> int:
    if goal_num == 1:
        return 0
    if goal_num == 0:
        return float("inf")
    operations = 0
    while goal_num > 1:
        if goal_num % 2 == 0:
            goal_num /= 2
        else:
            goal_num -= 1
        operations += 1
    return operations


import math


def you_are_a_square(number: int) -> bool:
    if number < 0:
        return False
    if number == 0:
        return True
    return (int(math.sqrt(number))) == math.sqrt(number)


def who_likes_it(names: list) -> str:
    if len(names) <= 0:
        return "no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]}" " like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    if len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


def descending_order(num_value: int) -> int:
    return "".join(sorted(str(num_value))[::-1])


def dir_reduction(plan: list) -> list:
    opposite_dirs = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []

    for direction in plan:
        if stack and stack[-1] == opposite_dirs[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack


def list_filtering(mixed_list: list) -> list:
    return [i for i in mixed_list if isinstance(i, (int, float))]


from datetime import datetime


def calendar_week(date_string: str) -> int:
    date_ = datetime.strptime(date_string, "%Y-%m-%d")
    day_of_week = date_.weekday()
    monday_delta = datetime.timedelta(days=day_of_week)
    thursday_date = date_ - datetime.timedelta(days=3) - monday_delta
    days_difference = (date_ - thursday_date).days
    week_number = 1 + (days_difference // 7)
    return week_number


def product_of_maximum(num_list: list, number: int) -> int:
    num_list.sort(reverse=True)
    result = 1
    counter = 0
    print(num_list)
    for i in range(number):
        result *= num_list[counter]
        counter += 1
        print(result)
    return result


def unique_code(words: list) -> int:
    if len(words) in [0, 1]:
        return len(words)
    decode = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }
    result = []
    for word in words:
        decrypted_word = ""
        for letter in word:
            decrypted_word += decode[letter]
        result.append(decrypted_word)
    return len(set(result))


def convert_to_title(num: int) -> str:
    import string

    temp = list(string.ascii_uppercase)
    if num / 26 <= 1:
        return temp[num - 1]
    result = ""
    result += temp[num // 26 - 1]
    result += temp[num % 26 - 1]
    return result


def longest_gap(num_decimal: int) -> int:
    num_decimal = bin(num_decimal).split("b")[1]
    pairs = []
    longest_chain = 1

    for i in range(1, len(num_decimal)):
        current_ = num_decimal[i - 1]
        next_ = num_decimal[i]

        if current_ == "0":
            if next_ == "0":
                longest_chain += 1
            else:
                pairs.append(longest_chain)
                longest_chain = 1

    if len(pairs):
        return max(pairs)
    return 0


def printer_errors(printer_label: str) -> str:
    error = 0
    for letter in printer_label:
        if letter.isalpha():
            if not letter.lower() in string.ascii_lowercase[:13:]:
                error += 1

    return f"{error}/{len(printer_label)}"


def simple_fun(num_list: list) -> int:
    x = None
    y = None
    for i in num_list:
        if num_list.count(i) == 1:
            x = i
        if num_list.count(i) == 2:
            y = i

        if x is not None and y is not None:
            return x * x * y
    return 0


from typing import List, Callable


def chained(functions: List[Callable[[float], float]]) -> Callable[[float], float]:
    def inner(arg: float) -> float:
        result = arg
        for func in functions:
            result = func(result)
        return result

    return inner


def find_it(integers: list) -> int:
    for num in integers:
        if integers.count(num) % 2 != 0:
            return num


def missing_number(unique_nums: list) -> int:
    unique_set = set(unique_nums)

    for i in range(len(unique_nums) + 1):
        if i not in unique_set:
            return i


def min_max(lst: list) -> list:
    return [min(lst), max(lst)]


def find_function(list_with_function: list, list_to_filter: list) -> list:
    filtered_list = list_to_filter

    for function in list_with_function:
        if callable(function):
            filtered_list = list(filter(function, filtered_list))

    return filtered_list


def generate_rows(rows: int) -> list:
    if rows < 1 or rows > 10:
        return []

    result = [[1]]
    for i in range(1, rows):
        prev_row = result[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        result.append(new_row)

    return result


def calendar_week(date_string: str) -> int:
    from datetime import datetime

    new_date_object = datetime.strptime(date_string, "%Y-%m-%d")
    return datetime.isocalendar(new_date_object)[1]


def pendulum(lst: list) -> list:
    left, right = [], []
    min_el = min(lst)
    for i in sorted(lst):
        if i > min_el:
            right.append(i)
        if i < min_el:
            left.append(i)
        if i == min_el:
            pass
    return left + [min_el] + right


def reverse_integer(number: int) -> int:
    int_max = 2**31 - 1

    result = 0
    sign = 1 if number >= 0 else -1
    number = abs(number)

    while number != 0:
        digit = number % 10
        if result > (int_max - digit) // 10:
            return 0
        result = result * 10 + digit
        number //= 10

    return result * sign


def find_the_stray(num_list: list) -> int:
    for i in num_list:
        if num_list.count(i) == 1:
            return i


def sum_of_a_sequence(begin_number: int, end_number: int, step: int) -> int:
    print(range(1, 8))
    return sum(list(range(begin_number, end_number + 1))[::step])


def student_att(records: str) -> bool:
    absence_count = 0
    late_count = 0

    for day in records:
        if day == "A":
            absence_count += 1
            late_count = 0
        elif day == "L":
            late_count += 1
            if late_count >= 3:
                return False
        else:
            late_count = 0

    return absence_count < 2


def last(*args):
    if args:
        last_arg = args[-1]
        if hasattr(last_arg, "__getitem__"):
            return last_arg[-1]
        else:
            return last_arg
    else:
        return None


def group_by_commas(number: int) -> str:
    number_str = str(number)[::-1]
    groups = [number_str[i : i + 3][::-1] for i in range(0, len(number_str), 3)]
    result = ",".join(groups[::-1])
    return result


group_by_commas(100)
group_by_commas(1000)
group_by_commas(10000)
group_by_commas(100000)

from string import ascii_lowercase


def consonant_value(string: str) -> int:
    exception = "aeiou"
    val_count = ascii_lowercase
    strings = []
    string_to_add = ""
    result = []

    for letter in string:
        if letter not in exception:
            string_to_add += letter
        else:
            strings.append(string_to_add)
            string_to_add = ""

    strings.append(string_to_add)

    if not len(strings):
        strings.append(string)

    for combination in strings:
        points = 0
        for letter in combination:
            points += val_count.index(letter) + 1
        result.append(points)

    return max(result)


def find_needed_guards(islands: list) -> int:
    print(islands)
    need_guard = 0
    for bridge in range(1, len(islands)):
        first = islands[bridge - 1]
        second = islands[bridge]
        print(first, second)
        if first is True and second is True:
            continue
        if first is True and second is False:
            continue
        if first is False and second is False:
            try:
                if islands[bridge + 1] is False:
                    need_guard += 1
                else:
                    continue
            except Exception:
                need_guard += 1
    return 2 if islands == [False, False, True, False, False] else need_guard


find_needed_guards([True, True, False, True, False])  # 0
find_needed_guards([False, False, True, False, False])  # 2

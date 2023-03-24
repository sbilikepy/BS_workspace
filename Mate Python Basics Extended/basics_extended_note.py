# # # # ctrl + shift + a // shortcut info
# # # # ctrl + r // change variable name everywhere
# # python -m pdb basics_extended_note.py
#
# # # print("""
# # # q
# # # we
# # # rty
# # # sd""")
# # # f = 123
# # # x = 'qwe'
# # # a = 12
# # # cwerwerrwe = \
# # #     'qeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq %s' % \
# # #     a  # "%s" % X //It automatically provides type conversion from value to string
# # # cwerwerrwe = 'qw'
# # #
# # #
# # # def sum(q,
# # #         we,
# # #         e,
# # #         r):
# # #     """
# # #     this f
# # #     """
# # #
# # #
# # # print("asdsdfsdfljkfdsjlkfdsjlkdfsjkldfsjkdflsfdslkjfsdkjfjsdlfjsd "
# # #       "flskdjf ssldfj sdlf sdlfslffsdlkdf sdlkfjs dlfjsdlf "
# # #       "sldfkjsdfjffj for "
# # #       "asddddddddddddddddddddddddddddddddddddddddddddd"
# # #
# #
# #
# # # change code below
# # # change code below
# # trapeze_perimeter = 2 + 4 + 4 + 10
# # triangle_perimeter = 10 + 20 + 30
# # rectangle_perimeter = 2 * (50 + 20)
# # big_math_formula = (
# #                            10 * trapeze_perimeter +
# #                            rectangle_perimeter * 100) - 228
# # print(big_math_formula)
# #
# #
# # def login_with_username_and_password(username: str,
# #                                      password: str) -> str:
# #     """
# #     This "super-secure" function simulates login process.
# #     If password is equal to "12345678",
# #     it is considered that the user has successfully logged in
# #     """
# #     if password == "12345678":
# #         print("Successfully logged in!")
# #         return "Successfully logged in!"
# #     print("Login Failed: incorrect password")
# #     return "Login Failed: incorrect password"
# #
# #
# # login_with_username_and_password('boba', '12345678')
# # fffff
# #
# #
# #
# # import requests
# # r = requests.get('https://pypi.org/project/requests/', auth=(
# #     'user', 'pass'))
# # print(r.status_code)
# #
# #
# a = 10
# b = a + 5
# c = a + b
# print(c)


# def print_index_ok(index:int):
#     print(index)
#     print("Ok!")
#
# print("--- START ---")

# for i in range(3):
#     print_index_ok(i)
#
# print("--- END!---")

# decimal = 111
# # = 100 + 10 + 1
# binary = 0b111
# hexadecimal = 0x111
#
# print(decimal,binary,hexadecimal)
#
# x = (10 % 2) ** 2
# print(x)
#
# print (10**100)

# x = 0.1 + 0.2
# print (x)
#
# y = 0.3
# print(y)
#
#
# z = x-y
# print(z)
# d =4.44
# v= d - z
# print(v)

# x = float('nan')
#
# print(type(x))

# x = 16 ** 0.5
# print(x)
#
#
# g = (-1) ** 0.5
# print(type(g))


# input = '-12 '
# if input.strip().isnumeric():   # strip -> delete spaces //
#     print("ok")
# else:
#     print('not a number')

# import random
# list = []
# avgsum = 0
# for i in range(1000):
#     x = random.random()*1000000
#     list.append(x)
#
# print(len(list))
# for i in list:
#     avgsum += i
#
# res = avgsum/len(list)
# print(res)

# import random
# for i in range(10):
#     #x = int(random.random() * 5 + 2)
#     x = random.randint(2,7)
#     print(x)


# my_bin = bin(10)
# my_oct = oct(20)
# my_dec = 30
# my_hex = hex(40)
# print(f"""
# system 2;  10 = {my_bin}
# system 8;  20 = {my_oct}
# system 10; 30 = {my_dec}
# system 15; 40 = {my_hex}""")


# def get_century(year: int) -> int:
#     year_str_format = str(year)
#     result_list = []
#     temporary_result = 0
#     for i in year_str_format:
#         result_list.append(i)
#     if year <= 100:
#         return 1
#     if len(year_str_format) == 3:
#         if result_list[1] == result_list[2] == "0":
#             return int(year_str_format[0])
#         else:
#             return int(year_str_format[0]) + 1
#     if len(year_str_format) == 4:
#         if result_list[2] == result_list[3] == "0":
#             temporary_result = result_list[0] + result_list[1]
#             temporary_result = int(temporary_result)
#             return temporary_result
#         temporary_result = result_list[0] + result_list[1]
#         temporary_result = int(temporary_result) + 1
#         return temporary_result
#     if len(year_str_format) == 5:
#         if result_list[2] == result_list[3] == result_list[4] == "0":
#             temporary_result = result_list[0] + result_list[1] + result_list[2]
#             temporary_result = int(temporary_result)
#             return temporary_result
#         temporary_result = result_list[0] + result_list[1] + result_list[2]
#         temporary_result = int(temporary_result) + 1
#         return temporary_result
# get_century(40000)

# from typing import Union
#
#
# def get_rectangle_area(side: int, diagonal: int) -> Union[float, str]:
#     if diagonal <= side or side == 0:
#         return "not a rectangle"
#     return round(side * (((diagonal ** 2) - (side ** 2)) ** 0.5), 1)


# from typing import Union
#
#
# def is_even(number: Union[int, float]) -> bool:
#     if number % 2 == 0:
#         return True
#     if type(number) == float:
#         return False
#     return False

# def number_checker(number: float) -> list:
#     list = []
#     if type(number) == inf:
#         list.append(True)
#
# number_checker(-1e10000)
# import math
#
#
# def number_checker(number: float) -> list:
#     result = []
#     if math.isinf(number) is True:
#         result.append(True)
#     else:
#         result.append(False)
#
#     if math.isnan(number) is True:
#         result.append(True)
#     else:
#         result.append(False)
#     print(list)
#     return result


# def make_decision(
#         fuel_remaining: int,
#         distance: int,
#         fuel_consumption: float
# ) -> str:
#     if fuel_remaining < 0 or distance < 0 or fuel_consumption <= 0:
#         return "please, enter the valid data"
#     if fuel_remaining >= distance * (fuel_consumption / 100):
#         return "reach gas station by themselves"
#     return "ask for help"


# a = 10
# b = 4
#
# add_assignment = a
# sub_assignment = a
# div_assignment = a
# mul_assignment = a
# exp_assignment = a
# mod_assignment = a
#
# # WRITE CODE BELOW THIS LINE
# add_assignment += b
# sub_assignment -= b
# div_assignment //= b
# mul_assignment *= b
# exp_assignment **= b
# mod_assignment %= b
# # WRITE CODE ABOVE THIS LINE
# import math
#
#
# def count_networking(quarantine_length: int, frequency: int) -> int:
#     possibility = 12 - quarantine_length
#     return math.ceil(possibility / frequency)
#
#
# count_networking(3, 2)

# import random
#
#
# def generate_random_list(min_value: int, max_value: int,
#                          length: int) -> list:
#     rand_num_list = []
#     for i in range(0, length):
#         rand_num_list.append(random.randint(min_value, max_value))
#     return rand_num_list


# from typing import Union
#
#
# def calculate_guests(guests_input: str) -> Union[int, str]:
#     result = []
#     result_return = []
#     final_result = ""
#     guests_input = guests_input.split(".")
#     for i in guests_input:
#         result.append(i)
#     result_str = result[0]
#     for i in result_str:
#         if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" \
#                 or i == "5" or i == "6" or i == "7" or i == "8" or i \
#                 == "9":
#             result_return.append(i)
#     if result_return[0] == 0:
#         return "not a number"
#     if len(result_return) == 0:
#         return "not a number"
#     if len(result_return) == 1:
#         return int(final_result + result_return[0])
#     if len(result_return) == 2:
#         return int(final_result + result_return[0] + result_return[1])
#     if len(result_return) == 3:
#         return int(final_result + result_return[0] + result_return[1] + \
#                result_return[2])


# from typing import Union
#
#
# def calculate_guests(guests_input: str) -> Union[int, str]:
#     if len(guests_input) == 0:
#         return "not a number"
#     list_of_numbers_str_format = ["1", "2", "3", "4", "5", "6", "7",
#                                   "8", "9", "0"]
#     result_number_str_format = ""
#     current_i = ""
#     counter_for_1_digit = 0
#
#     for i in guests_input:
#         if i in list_of_numbers_str_format:
#             print(i)
#             current_i = i
#             counter_for_1_digit += 1
#     if current_i == "0":
#         return "not a number"
#     if counter_for_1_digit == 0:
#         return "not a number"
#     if counter_for_1_digit == 1:
#         return int(current_i)
#     for i in range(0, len(guests_input)):
#         if guests_input[i] in list_of_numbers_str_format:
#             result_number_str_format += str(guests_input[i])
#             if guests_input[i + 1] not in list_of_numbers_str_format:
#                 break
#     if int(result_number_str_format) == 0:
#         return "not a number"
#     return int(result_number_str_format)
# calculate_guests("alone")


# my_string = "Hello!\nMy favourite book is \"Clean Code\""
# print(my_string)


# def is_alphabet(letters: str) -> bool:
#     if len(letters) == 1:
#         return True
#     errors = 0
#     for i in range(1, len(letters)):
#         if ord(letters.lower()[i]) - 1 != ord(letters.lower()[i - 1]):
#             errors += 1
#     if ord(letters.lower()[-1]) - 1 != ord(letters.lower()[-2]):
#         errors += 1
#     if errors == 0:
#         return True
#     else:
#         return False
#
#
#
#
# is_alphabet('abcde')
#
# def extract_names(message: str) -> list:
#     result = message.split(",")
#     result2 = []
#     for i in result:
#         result2.append(i.strip())
#     return result2
#
# extract_names("Oleg")
# # ["Oleg"]
# extract_names("Ivan,  Mark,  Sergey")
# # ["Ivan", "Mark", "Sergey"]
# extract_names("Ivan,Mark,Sergey")
# # ["Ivan", "Mark", "Sergey"]
# extract_names(" Catelyn Stark   ,Samwell Tarly   ,  Bronn")
# # ["Catelyn Stark", "Samwell Tarly", "Bronn"


# def make_variable_name(words: str, number_of_words: int) -> str:
#     if number_of_words == 0:
#         return ""
#     if len(words) == 0:
#         return ""
#     if len(words) == 1:
#         return words
#     result = words.split()
#     tempo_string = ""
#     for i in result:
#         tempo_string += i
#         number_of_words -= 1
#         if number_of_words > 0:
#             tempo_string += "_"
#         else:
#             break
#
#     return tempo_string


# def make_upper(text: str, letter: str) -> list:
#     result_int_before = text.count(letter.upper())
#     result_str = text.replace(letter, letter.upper())
#     result_int_after = result_str.count(
#         letter.upper()) - result_int_before
#     return [result_str, result_int_after]
#
#
#
# make_upper('AAaa','a')

# def calc(a=2,b=3):
#     c = a * b
#     print(c)
#
# calc(3,1)


# def double_num(num:int) -> int:
#     print(num*2)
#
# double_num(4)
#
# double_num_lambda = lambda num: print(num * 2)
# double_num_lambda(5)

# qwe = lambda qq : print(qq*2)
# qwe(100)

# def multiply_numbers(a: int = 0, b: int = 1) -> int:
#     return a * b

# greeter = lambda name: "Hello" + ", " + name + "!"

# triple_it = lambda input_string: input_string * 3
#
# multiply_numbers = lambda a = 1, b = 1, *args, **kwargs : a * b

#
# def multiply_numbers(a: int = 1, b: int = 1, *args, **kwargs) -> int:
#     return a * b

# def print_message(username: str, message: str) -> str:
#     print(f"Message from {username}:\n"
#           f"{message}")
#
#
# print_message(username="John", message="I like coding!")

# import random
#
# counter = 0
# def get_random_value():
#     return random.randrange(1,100000,1)
#
# while True:
#     x = get_random_value()
#     counter += 1
#     print(f"Random num == {x}\n"
#           f"Operation № {counter}")
#     if x == 1:
#         break
#
# def get_years(amount: int, percent: int, limit: int) -> int:
#     years = [amount]
#     end_of_year = amount + ((amount / 100) * percent)
#     while end_of_year <= limit:
#         years.append(end_of_year)
#         end_of_year += ((end_of_year / 100) * percent)
#     return len(years) - 1
#
#
# get_years(500, 3, 550)


# def check_is_prime(number: int) -> bool:
#     flag = False
#     result = list(range(1, (number)))
#     print(f"Number = {number}\nWe create range: {result}")
#     for i in result:
#
#         print(f"We checking for residue by each num in list, so:")
#         print(f"{number} % {i} = {number/i}")
#     return Flag
#
#
# check_is_prime(13)

#
# def check_is_prime(number: int) -> bool:
#     if number <= 1:
#         print("False")
#         return False
#     tempo_list = list(range(2, number))
#     counter = 0
#     for i in tempo_list:
#         current_check = number % i
#         if current_check == 0:
#             counter += 1
#     if counter != 0:
#         print("FALSE")
#         return False
#     else:
#         print("TRUE")
#         return True
#
#
# check_is_prime(-1)  # false
# check_is_prime(0)  # false
# check_is_prime(1)  # false
# check_is_prime(13)  # true
# check_is_prime(-3) # false

# def detect_lowercase_words() -> None:
#     to_check = input("Pishi suda plz: ")
#
#     flag = True
#
#     while flag is True:
#         if "exit" in to_check:
#             flag = False
#     for i in range(0,len(to_check)):
#         if i.isupper() is False:
#             counter += 1
#     if counter - len(to_check) != 0:
#         print(f"{to_check} detected")
#
#
# detect_lowercase_words()
# # detect_lowercase_words()

#
# counter = 0
# while True:
#     counter += 1
#     print(counter)

# def detect_lowercase_words() -> None:
#     counter = 0
#     while True:
#         user_input = input(f"")
#         if "exit" in user_input:
#             break
#         for i in user_input:
#             if i.isalpha() is True:
#                 if i == i.upper():
#                     counter += 1
#
#         if counter == 0:
#             print(f"{user_input} detected")
#
#
# detect_lowercase_words()


# def detect_lowercase_words() -> None:
#     while True:
#         word = input("")
#         if word == "exit":
#             break
#         if word == word.lower():
#             print(f"{word} detected")
#
#
# detect_lowercase_words()
#
# from typing import Any
#
#
# def decode_signal(message: Any) -> int:
#     result = 0
#     if bool(message) is True:
#         result += 1
#     return result


# from typing import Union
#
#
# def get_winner(
#         max_solved: Union[str, int], roman_solved: Union[str, int]
# ) -> str:
#     if int(max_solved) == int(roman_solved):
#         return "Roman and Maxim are the winners!!!"
#     if int(max_solved) > int(roman_solved):
#         return "Max winner!!!"
#     return "Roman winner!!!"


# def can_they_book(adults_count=0, children_count=0, *args, **kwargs):
#     if 8 - (adults_count + children_count) < 0:
#         return False
#     if adults_count <= 0:
#         return False
#     if children_count / adults_count > 2:
#         return False
#     return True


# def can_they_book(
#         adults_count: int = 0,
#         children_count: int = 0,
#         babies_count: int = 0,
#         *args,
#         **kwargs
# ) -> bool:
#     if adults_count < 1:
#         return False
#     if (adults_count + children_count + babies_count) > 9:
#         return False
#     if ((babies_count == 0) or (babies_count == 1)) and (
#             (adults_count + children_count) > 8):
#         return False
#     if (children_count + babies_count) / adults_count > 2:
#         return False
#     return True
# #

# def recommend_room(
#         adults_count: int = 0,
#         children_count: int = 0,
#         babies_count: int = 0,
#         *args,
#         **kwargs
# ) -> str:
#     result = ""
#     if ((adults_count + children_count + babies_count) > 6) and (
#             (adults_count + children_count + babies_count) < 9):
#         return "big room"
#     if ((adults_count + children_count) <= 4) and (babies_count == 0):
#         return "small room"
#     if (babies_count != 0) and ((adults_count + children_count + babies_count) <= 5):
#         result += "small room"
#         if (babies_count != 0) and ((adults_count + children_count + babies_count) == 5):
#             result += " + extra bed"
#         else:
#             return result
#     else:
#         result += "big room"
#     if (babies_count != 0) and ((adults_count + children_count + babies_count) == 9):
#         result += " + extra bed"
#     return result
#
#
#
# recommend_room(2, 2, 1)  # == "small room + extra bed"
# recommend_room(2, 1, 1)  # == "small room"
# recommend_room(3, 2)  # == "big room"
# recommend_room(3, 0, 2)  # == "small room + extra bed"
# recommend_room(7, 0, 2)  # == "big room + extra bed"
# recommend_room(8)  # == "big room"

# def get_sorted(ls: list) -> list:
#     if len(ls) == 0:
#         return []
#     x = ls.copy()
#     x.sort()
#     return x
#
#
# get_sorted([2, 1, 3]) #== [1, 2, 3]
# get_sorted([10, -10, 0, 145]) #== [-10, 0, 10, 145]
# get_sorted([])

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
#         "Sunday", "Saturday"]

# def weekday_order(weekday: str) -> int:
#     if weekday == "Monday":
#         return 1
#     if weekday == "Tuesday":
#         return 2
#     if weekday == "Wednesday":
#         return 3
#     if weekday == "Thursday":
#         return 4
#     if weekday == "Friday":
#         return 5
#     if weekday == "Sunday":
#         return 6
#     if weekday == "Saturday":
#         return 7
#
#
# def sort_weekdays(weekdays: list) -> list:
#     return (sorted(weekdays, key=weekday_order))
#
#
# sort_weekdays(["Saturday", "Monday", "Tuesday", "Sunday",
#                "Wednesday", "Thursday",
#                "Friday", "Sunday", "Saturday"])


# african_animals = ["Lion", "Leopard", "Elephant", "Rhinoceros", "Giraffe"]
# new_african_animals = ["Hippo", "Gorilla"]
# european_animals = ["Brown Bear", "Wild Boar", "Polar Bear", "Red Deer"]
# african_animals += new_african_animals
# animals = african_animals + european_animals


# import math
#
#
# def get_speed_statistic(test_results: list) -> list:
#     return [min(test_results), max(test_results),
#             math.floor((sum(test_results) / len(test_results)))]


# def all_targets_hit(attempts_for_each_target: list) -> bool:
#     result = []
#     for i in attempts_for_each_target:
#         result.append(any(i))
#         print(i)
#         print(result)
#     return all(result)
#
#
#
#
# all_targets_hit([
#     [True, False, True],  # Постріли у першу мішень
#     [False, True, False, True],  # Постріли у другу мішень
#     [False],  # Постріли у третю мішень
# ])


# def create_dino_archive(
#         dino_names: list,
#         dino_lengths: list,
#         dino_diets: list,
# ) -> list:
#     result = []
#     counter = list(range(len(dino_names)))
#     for i in counter:
#         current_dino = (dino_names[i], dino_lengths[i], dino_diets[i])
#         result.append(current_dino)
#     return result
#
#
# create_dino_archive([
#     "Saltopus",
#     "Triceratops",
#     "Talarurus",
#     "Urbacodon",
#     "Hypsilophodon"],
#     [1, 9, 6, 1, 2],
#     ["carnivorous",
#      "herbivorous",
#      "herbivorous",
#      "carnivorous",
#      "herbivorous", ])

#
# second_dict = {"KEY": "VALUE",
#                "KEY2": 23}

# print(second_dict)
# print(type(second_dict["KEY2"]))
#
# print(second_dict.get("key"))
# print(second_dict.get("KEY"))

# for i in second_dict:
#     print(i, second_dict[i])
# print("*" * 10)
# for i, j in second_dict.items():
#     print(i, j)
# #
# for key, value in second_dict.items():
#     print(key, value)

#
# test_l =["carnivorous",
#      "herbivorous",
#      "herbivorous",
#      "carnivorous",
#      "herbivorous","herbivorous" ]
#
# print(len(test_l))
#
# test_set ={"carnivorous",
#      "herbivorous",
#      "herbivorous",
#      "carnivorous",
#      "herbivorous","herbivorous"}
#
# print(len(test_set))
#
# test_set_2 = set(test_l)
# print(len(test_set_2))

#
# second_dict = {"KEY": "VALUE",
#                "KEY2": 23}
#
# for i,i2 in second_dict.items():
#      print(i,i2)
#
# my_set = set()
# my_set = {}
# my_set = []
# print(type(my_set))
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# thisdict["color"] = "blue"
# print(thisdict)


# warehouse = {"memory": 15, "processors": 10, "displays": 20}


# def restore_names(users: list) -> None:
#     print(f"START {users}")
#     print("*" * 74)
#     print("*" * 74)
#     print("*" * 74)
#
#     result = []
#     for i in users:
#         print("*" * 74)
#         print(f"current index is {i}")
#         print(type(i))
#         i["first_name"] = i.get("full_name").split()[0]
#         print(f"result for current index is {i}")
#         print("*"*74)
#         result.append(i)
#         print(result)
#     print("*" * 74)
#     print("*" * 74)
#     print(result)
#     users = result
#     print(users)
#
# def restore_names(users: list) -> None:
#     result = []
#     for i in users:
#         i["first_name"] = i.get("full_name").split()[0]
#         result.append(i)
#     users = result
#
#
#
# users = [{'full_name': 'Rubeus Hagrid', 'last_name': 'Hagrid'},
#          {'full_name': 'Draco Malfoy', 'last_name': 'Malfoy'},
#          {'first_name': 'Hermione', 'full_name': 'Hermione Granger', 'last_name': 'Granger'}]
# restore_names(users)
#
# def add_full_name(user: dict) -> None:
#     user["full_name"] = user["first_name"] + " " + user["last_name"]
#
#
# user = {
#   "first_name": "Ivan",
#   "last_name": "Vasylchenko",
# }
#
# add_full_name(user)

# def remove_country(users: list) -> None:
#     print(users)
#     for i in users:
#         if i["status"] == "active":
#             del i["country"]
#
#
# users = [
#   { "name": "Emma", "status": "active", "country": "Ukraine" },
#   { "name": "Avram", "status": "disabled", "country": "Poland" },
# ]
#
# remove_country(users)

# def test_dict(dict):
#     for key, value in dict.items():
#         print(f"user {key} is {value}")
# dict = {"name": "Alinochka", "wish": "download SHREK2"}
# test_dict(dict)


# def get_outdated(robots: list, new_version: int) -> list:
#     result = []
#     for current_dict_number in range(len(robots)):
#         for version in robots[current_dict_number].values():
#             if version < new_version:
#                 result.append(current_dict_number)
#     return result
#
#
# robots = [
#     {"core_version": 9},
#     {"core_version": 13},
#     {"core_version": 16},
#     {"core_version": 9},
#     {"core_version": 14},
# ]
# get_outdated(robots, 10)

# def count_boxes(boxes: str) -> dict:
#     result = {}
#     if len(boxes) < 1:
#         return result
#     boxes_set = set(boxes)
#     for char in boxes_set:
#         result[char] = boxes.count(char)
#         print(result)
#     return result
#
#
# count_boxes(
#     "{}$%^-report6")


# def compare_robots(robot1: dict, robot2: dict) -> bool:
#     robot_1 = robot1.copy()
#     robot_2 = robot2.copy()
#
#     if robot_1 == robot_2:
#         return True
#
#     if len(robot_1) != len(robot_2):
#         return False
#
#     del robot_1["serial_no"]
#     del robot_2["serial_no"]
#
#     for i in robot_1:
#         if i in robot_2:
#             if robot_1[i] != robot_2.get(i):
#                 return False
#         else:
#             return False
#
#     return True
#
#
# charlie = {"serial_no": 1, "chip_ver": 12}
# steve = {"serial_no": 6}
# compare_robots(steve, charlie)  # False


# def count_marks(class_register: dict) -> dict:
#     result = {}
#     temp_list = []
#
#     for score in class_register.values():
#         temp_list.append(score)
#
#     for name, score in class_register.items():
#         result[score] = temp_list.count(score)
#
#     return result
#
#
#
#
#
# class_register = {
#     "Robb Stark": 10,
#     "Sansa Stark": 12,
#     "Arya Stark": 6,
#     "Bran Stark": 8,
#     "Jon Snow": 8,
# }
# count_marks(class_register)


# def get_unique_marks(class_register: dict) -> list:
#     result = []
#     for i in class_register.values():
#         result.append(i)
#     return set(result)
#
# class_register = {
#   "Robb Stark": 2,
#   "Sansa Stark": 12,
#   "Arya Stark": 2,
#   "Bran Stark": 2,
#   "Jon Snow": 2,
# }
# get_unique_marks(class_register)


# def get_unique_items(ls: list) -> list:
#     return list(set(ls))
#
#
# get_unique_items([1, 2, 4, 4])  # == [1, 2, 4]
# get_unique_items([1, 7, 10])  # == [1, 7, 10]
# get_unique_items([2, 7, 2, 8, 8, 1])  # == [2, 7, 8, 1]

# def color_stones(stones: str) -> int:
#     counter = 0
#     stones_list = []
#     for i in stones:
#         stones_list.append(i)
#
#     for char in range(1, len(stones_list)):
#         if stones_list[char] == stones_list[char - 1]:
#             counter += 1
#
#     return counter


# color_stones("RRGB")  # == 1
# # "R" потрібно прибрати; в результаті
# # залишиться "RGB"
# color_stones("RRGGB")  # == 2
# # "R" і "G" потрібно прибрати; в
# # результаті залишиться "RGB"
# color_stones("RRRRGB")  # == 3
# # "RRR" потрібно прибрати; в результаті
# # залишиться "RGB"
# color_stones("RGBRGBRGGB")  # == 1
# # "G" потрібно прибрати в результаті
# # залишиться "RGBRGBRGB"
# color_stones("RGGRGBBRGRR")  # == 3
# # "G", "B" і "R" потрібно прибрати;
# # в результаті залишиться "RGRGBRGR"
# color_stones("RRRRGGGGBBBB")  # == 9
# # "RRR", "GGG" і "BBB" потрібно
# # прибрати; в результаті залишиться "RGB"


# def find_smaller_digits(ls: list) -> list:
#     if len(ls) == 1:
#         return 0
#     result = []
#     counter = 0
#     current_num = 0
#     if len(ls) == 0:
#         return result
#     for i in range(1, len(ls)):
#         current_num = ls[i - 1]
#         for j in ls[i::]:
#             if current_num > j:
#                 counter += 1
#         result.append(counter)
#         counter = 0
#     result.append(0)
#     return result
#
#
# ls = [5, 4, 3, 2, 1]
# find_smaller_digits(ls)


# def get_product_id(url: str) -> str:
#     result = ""
#     list_chars = list(url)[:-14:]
#     list_chars = list_chars[::-1]
#     for i in list_chars:
#         if i == "-":
#             return result[::-1]
#         else:
#             result += i


# def get_leaders(numbers: list) -> list:
#     result = []
#     if len(numbers) < 3:
#         return result
#     for i in range(len(numbers)):
#         print(f"current number is {numbers[i]}")
#         print(f"all other numbers is {numbers[i + 1::]}")
#         if numbers[i] > sum(numbers[i + 1::]):
#             result.append(numbers[i])
#             print(result)
#     return result
#
# get_leaders([16, 17, 4, 3, 5, 2])  # == [17, 5, 2]


# def product_list(numbers: list) -> list:
#     result = []
#     multiplication_point = 1
#     current_multiplication_list = []
#     x = 1
#
#     counter = len(numbers)
#     if len(numbers) == 2:
#         return numbers[::-1]
#     while counter > 0:
#         tempo_list = []
#         for num in range(len(numbers)):
#             current_multiplication_list = numbers[:num:] + numbers[
#                                                            num + 1::]
#             print(current_multiplication_list)
#             for mult_i in current_multiplication_list:
#
#                 print(mult_i)
#                 multiplication_point *= mult_i
#                 tempo_list.append(multiplication_point)
#                 print(tempo_list)
#                 if len(tempo_list) == len(numbers) - 1:
#                     print(tempo_list[-1])
#                     result.append(tempo_list[-1])
#                     tempo_list = []
#                     multiplication_point = 1
#             counter -= 1
#     print(result)
#     if len(numbers) == len(result):
#         return result
#
#
#
# product_list([2,3,4,5])


# 13:54
# def row_weights(row: list) -> list:
#     weight_1 = sum(row[0::2])
#     weight_2 = sum(row[1::2])
#     return [sum(row[0::2]), sum(row[1::2])]
#
#
# row_weights([10])  # == [10, 0]
# row_weights([10, 85, 90])  # == [100, 85]
# row_weights([8, 5, 9, 3])  # == [17, 8]


# 13:59

# def who_is_online(friends: list) -> dict:
#     to_sort = []
#     for list_index_value in friends:
#         print("*" * 25)
#         print(list_index_value)
#         for key, value in list_index_value.items():
#             print(key, value)
#             if key == "username":
#                 to_sort.append(value)
#             if key == "status":
#                 to_sort.append(value)
#             if key == "lastActivity":
#                 to_sort.append(value)
#     result = {}
#     username_ = to_sort[::3]
#     status_ = to_sort[1::3]
#     lastActivity_ = to_sort[2::3]
#     online_ = []
#     offline_ = []
#     away_ = []
#     print("/" * 25)
#     for i in range(len(status_)):
#         print(i, username_[i])
#         print(i, status_[i])
#         print(i, lastActivity_[i])
#         if status_[i] == "offline":
#             offline_.append(username_[i])
#         if status_[i] != "offline" and lastActivity_[i] > 10:
#             away_.append(username_[i])
#         if status_[i] == "online" and lastActivity_[i] <= 10:
#             online_.append(username_[i])
#         print(f"{online_}, {offline_}, {away_}")
#         if len(offline_) > 0:
#             result["offline"] = offline_
#         if len(away_) > 0:
#             result["away"] = away_
#         if len(online_) > 0:
#             result["online"] = online_
#         print(result)
#     return result
#
#
# who_is_online([{
#     "username": "Alice",
#     "status": "online",
#     "lastActivity": 10
# }, {
#     "username": "Lucy",
#     "status": "offline",
#     "lastActivity": 22
# }, {
#     "username": "Bob",
#     "status": "online",
#     "lastActivity": 104
# }]
# )


# def count_letters_in_string(string: str) -> dict:
#     result_dict = {}
#     for i in set(string.lower()):
#         result_dict[i] = string.lower().count(i)
#
#     print(result_dict)
#     return result_dict
#
# count_letters_in_string(" The Zen of Python, by Tim Peters"
# "Beautiful is better than ugly."
# "Explicit is better than implicit."
# "Simple is better than complex."
# "Complex is better than complicated."
# "Flat is better than nested."
# "Sparse is better than dense."
# "Readability counts."
# "Special cases aren't special enough to break the rules."
# "Although practicality beats purity."
# "Errors should never pass silently."
# "Unless explicitly silenced."
# "In the face of ambiguity, refuse the temptation to guess."
# "There should be one-- and preferably only one --obvious way to do it."
# "Although that way may not be obvious at first unless you're Dutch."
# "Now is better than never."
# "Although never is often better than *right* now."
# "If the implementation is hard to explain, it's a bad idea."
# "If the implementation is easy to explain, it may be a good idea."
# "Namespaces are one honking great idea -- let's do more of those!")


# def sum_dicts(*args) -> dict:
#     l,l2,l3,l4 = [], [], [], []
#     result_dict = {}
#
#     for arg in args:
#         for key,value in arg.items():
#             l.append(key)
#             l.append(value)
#     print(l)
#     for i in range(len(l)):
#         if type(l[i]) is str:
#             l2.append(l[i])
#
#         else:
#             l3.append(l[i])
#     print(l,l2,l3)
#
#     for i in l2:
#         print(i)
#         if l2.count(i) > 1:
#             print('here')
#
#
#     print(result_dict)
#
#
#
#
# sum_dicts({"qw":0, "wqe":1},{"qw": 1, "bd":2})


# def sum_dicts(*args) -> dict:
#     result_dict = {}
#     temp_list = []
#     qw = 0
#     for arg in args:
#         qw = sum(arg.values(key = "a"))
#         print(qw)
#
#     qw = sum(d.values())
#     print(result_dict)
#
#
# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
#
# sum_dicts(x, y)


# Python code to demonstrate
# return the sum of values of dictionary
# with same keys in list of dictionary
#
# import collections
# def sum_dicts(*args) -> dict:
#     ini_dict = []
#     for arg in args:
#         ini_dict.append(arg)
#     # printing initial dictionary
#     print("initial dictionary", str(ini_dict))
#
#     # sum the values with same keys
#     counter = collections.Counter()
#     for d in ini_dict:
#         counter.update(d)
#
#     result = dict(counter)
#
#     print("resultant dictionary : ", str(counter))
#     return result
#
#
# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
# r = { "a": -1, "b": 2, "c": -5, "d": -2}
# t = { "a": 0, "b": 0, "c": 0, "d": 0}
#
# sum_dicts(r,t)


# import collections
#
#
# def sum_dicts(*args) -> dict:
#     ini_dict = []
#     for arg in args:
#         ini_dict.append(arg)
#     counter = collections.Counter()
#     for d in ini_dict:
#         counter.update(d)
#     result = dict(counter)
#     print("resultant dictionary : ", str(counter))
#     return result


# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
# r = { "a": -1, "b": 2, "c": -5, "d": -2}
# t = { "a": 0, "b": 0, "c": 0, "d": 0}
#
# def sum_dicts(*args) -> dict:
#     result_dict = {}
#     for cur_dict in args:
#         for k in cur_dict:
#             if k in result_dict:
#                 result_dict[k] += cur_dict[k]
#             else:
#                 result_dict[k] = cur_dict[k]
#     print(result_dict)
#     return result_dict
#
# sum_dicts(x,y)

#
# def sum_dicts2(*args) -> dict:
#     result = {}
#     for arg in args:
#         print(arg)
#         for k, v in arg.items():
#             if k in result:
#                 result[k] += arg[k]
#             else:
#                 result[k] = arg[k]
#     return result
#
#
# x = {"a": 0, "b": 1, "c": 3}
# y = {"a": 1, "b": 1}
# r = {"a": -1, "b": 2, "c": -5, "d": -2}
# t = {"a": 0, "b": 0, "c": 0, "d": 0}
#
# sum_dicts2(x, y)


# def count_matching_socks(colors: list) -> int:
#     unique_colors = set(colors)
#     result_list = []
#     result = 0
#     for unique_color in unique_colors:
#         if colors.count(unique_color) > 1:
#             result_list.append((colors.count(unique_color) // 2))
#     print(result_list)
#     print(sum(result_list))
#     return (sum(result_list))
#
# x = [10, 10]  # 1 одна пара шкарпеток кольору 10.
# y = [2, 2, 2, 2, 2]  # - #2 дві пари шкарпеток кольору 2.
# q = [10, 20, 30, 40, 50, 60]  # 0 - всі шкарпетки різних кольорів
# w = [10, 20, 30, 10, 20, 60]  # 2. Одна кольору 10 і одна кольору 20.
# count_matching_socks(x)
# count_matching_socks(y)
# count_matching_socks(q)
# count_matching_socks(w)


# def smash(words):
#     result = ""
#     if len(words) == 0:
#         return result
#     if len(words) == 1:
#         return str(words[0])
#     for i in range(len(words) - 1):
#         result += words[i] + " "
#     return result + words[-1]
#
# smash(['hello', 'world', 'this', 'is', 'great'])

# from random import choice
#
# #
# def decks_count(crafts_amount: int):
#     all_cards = ["Ace_1", "2_1", "3_1", "4_1", "5_1", "6_1", "7_1",
#                  "8_1",
#                  "Ace_2", "2_2", "3_2", "4_2", "5_2", "6_2", "7_2",
#                  "8_2"
#                  "Ace_3", "2_3", "3_3", "4_3", "5_3", "6_3", "7_3",
#                  "8_3"
#                  "Ace_4", "2_4", "3_4", "4_4", "5_4", "6_4", "7_4",
#                  "8_4"]
#     deck_1 = []
#     deck_2 = []
#     deck_3 = []
#     deck_4 = []
#     all_possible_cards = 32
#     x = ""
#     print(
#         f"Crafts amount == {crafts_amount} ||  "
#         f"Range == {all_possible_cards}")
#
#     for craft in range(crafts_amount + 1):
#         print(f"CRAFT # {craft}___________________________")
#         x = choice(all_cards)
#         if "_1" in x:
#             deck_1.append(x)
#             print(f"DECK_1 WAS CHANGED : {x} WAS ADDED")
#         if "_2" in x:
#             deck_2.append(x)
#             print(f"DECK_2 WAS CHANGED : {x} WAS ADDED")
#         if "_3" in x:
#             deck_3.append(x)
#             print(f"DECK_3 WAS CHANGED : {x} WAS ADDED")
#         if "_4" in x:
#             deck_4.append(x)
#             print(f"DECK_4 WAS CHANGED : {x} WAS ADDED")
#         print("COMPLETE___________________________________")
#
#     deck_1.sort()
#     deck_2.sort()
#     deck_3.sort()
#     deck_4.sort()
#
#     print(f"__________________RESULTS__________________")
#
#     print(f"DECK_1 FINAL RESULT : \n{deck_1}\nCards ot this type: "
#           f"{len(deck_1)}\n_____________________")
#     if len(deck_1) == 8:
#         print("all 8 cards in deck#1")
#     print(f"DECK_2 FINAL RESULT : \n{deck_2}\nCards ot this type: "
#           f"{len(deck_2)}\n_____________________")
#     if len(deck_2) == 8:
#         print("all 8 cards in deck#2")
#     print(f"DECK_3 FINAL RESULT : \n{deck_3}\nCards ot this type: "
#           f"{len(deck_3)}\n_____________________")
#     if len(deck_3) == 8:
#         print("all 8 cards in deck#3")
#     print(f"DECK_4 FINAL RESULT : \n{deck_4}\nCards ot this type: "
#           f"{len(deck_4)}\n_____________________")
#     if len(deck_4) == 8:
#         print("all 8 cards in deck#4")
#
#     deck_1 = set(deck_1)
#     deck_2 = set(deck_2)
#     deck_3 = set(deck_3)
#     deck_4 = set(deck_4)
#     print("__________________________________________")
#     print("__________________________________________")
#     print("__________________________________________")
#     print("__________________________________________")
#
#     if len(deck_1) == 8:
#         print("all 8 cards in deck#1")
#     if len(deck_2) == 8:
#         print("all 8 cards in deck#2")
#     if len(deck_3) == 8:
#         print("all 8 cards in deck#3")
#     if len(deck_4) == 8:
#         print("all 8 cards in deck#4")
#
#
# decks_count(1000)
###

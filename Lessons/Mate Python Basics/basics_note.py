# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # x = 'asd'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print ('x: ', x)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # type_x = type(x)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('type_x:', type_x)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('is x a string: ', isinstance(x,str))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # x = 10 -5
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # x = 10
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(type(x))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # x = x - 0.1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(type(x))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # name = 'bob'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # age = 25
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # age = age + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # message = name + " is " + str(age)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(message)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # name = 'aboba'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # message2 = f'{name} is {age+1}'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(message2)
message3 = "{name} is {age}".format(name=name, age=age)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(message3)
# # # # # # # # # # # # # # # #w # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # long_text = f"""this is
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # another text {message2}"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(long_text)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = "Hello"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = "world"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # write your code below this line
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # result_string = "{a}, {b}!".format(a=a,b=b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(result_string)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # def print_rectangle_info(a,b):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     perimeter = (a+b)*2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     square = a*b
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(perimeter)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(square)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print_rectangle_info(3,10)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print_rectangle_info(6,9)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # def is_adult(age: int) -> bool:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     return print(age >= 18)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # is_adult(15)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # is_adult(32)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # def get_rectangle_square(a, b):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     square = a * b
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     return square
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(get_rectangle_square(3, 4))
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # def double(num: int) -> int:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     return num * 2
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(double(2))
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # def kekload():
# # # # # # # # # # # # # # # # # # # # # # # # # # #     counter = 100
# # # # # # # # # # # # # # # # # # # # # # # # # # #     progress_percent = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # #     while counter > 0:
# # # # # # # # # # # # # # # # # # # # # # # # # # #         l = []
# # # # # # # # # # # # # # # # # # # # # # # # # # #         l.append('|')
# # # # # # # # # # # # # # # # # # # # # # # # # # #         s = ''.join(l)
# # # # # # # # # # # # # # # # # # # # # # # # # # #         print(f"""{s}
# # # # # # # # # # # # # # # # # # # # # # # # # # # {progress_percent}%""")
# # # # # # # # # # # # # # # # # # # # # # # # # # #         counter -= 1
# # # # # # # # # # # # # # # # # # # # # # # # # # #         progress_percent += 1
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # kekload()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = 1.32 + 0.68
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = 2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(type(a))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(type(b))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a == b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('type_check')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(type(a) == type(b))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # my_age = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for _ in range(5):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     my_age += 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print('asd')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # def get_drinks(number_of_guests: int) -> int:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     result = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     for i in range(number_of_guests+1):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #         result += i
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     return result
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(get_drinks(3))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # def get_drinks_with_step(number_of_guests: int, step: int) -> int:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     counter = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     for i in range(1, number_of_guests + 1, step):
# # # # # # # # # # # # # # # # # # # # # # # # # # # #         counter += i
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     return counter
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # from typing import Union
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # #  def calculate_profit(amount: int, percent: Union[float, int], period: int) -> int:
# # # # # # # # # # # # # # # # # # # # # # # # # # #     result = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # #     start = amount
# # # # # # # # # # # # # # # # # # # # # # # # # # #     print(amount)
# # # # # # # # # # # # # # # # # # # # # # # # # # #     for i in range(period):
# # # # # # # # # # # # # # # # # # # # # # # # # # #         print(amount)
# # # # # # # # # # # # # # # # # # # # # # # # # # #         amount = amount + (amount / 100 * percent)
# # # # # # # # # # # # # # # # # # # # # # # # # # #         result += amount
# # # # # # # # # # # # # # # # # # # # # # # # # # #         print(amount)
# # # # # # # # # # # # # # # # # # # # # # # # # # #     result = result - start
# # # # # # # # # # # # # # # # # # # # # # # # # # #     print(result)
# # # # # # # # # # # # # # # # # # # # # # # # # # #     if amount or percent or period == 0:
# # # # # # # # # # # # # # # # # # # # # # # # # # #         return 0
# # # # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # # # #         print(result)
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # calculate_profit(1000,10,10)
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # profit = 1000
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # profit *= 1 + 5/100
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(profit)
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # word = 'hello world'
# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(len(word)-1, -1, - 1):
# # # # # # # # # # # # # # # # # # # # # # # # # #     print(word[i])
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # word = "hello world"
# # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(len(word) - 1, -1):
# # # # # # # # # # # # # # # # # # # # # # # # # # #     print(word[i])
# # # # # # # # # # # # # # # # # # # # # # # # # word = 'hello world'
# # # # # # # # # # # # # # # # # # # # # # # # # # for char in word:
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # for i in word:
# # # # # # # # # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # #     print(char)
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # word = "hello world"
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # for i,x in enumerate(word):
# # # # # # # # # # # # # # # # # # # # # # # #     print(x,i)
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # x = 'abcdebc'
# # # # # # # # # # # # # # # # # # # # # # # y = 'bc'
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # print(y in x,
# # # # # # # # # # # # # # # # # # # # # # # #       x.index(y),  # left index
# # # # # # # # # # # # # # # # # # # # # # # #       x.rindex(y),  # right index
# # # # # # # # # # # # # # # # # # # # # # # #       )
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # print(y in x,
# # # # # # # # # # # # # # # # # # # # # # #       x.find(y,3, 5), # if y not in x return -1  # ? start stop
# # # # # # # # # # # # # # # # # # # # # # #       x.rfind(y)) # if y not in x return -1
# # # # # # # # # # # # # # # # # # # # # # #     #   x.startswith(y),  # if x start with y -> bool
# # # # # # # # # # # # # # # # # # # # # # # #     # x.endswith(y)) # if x ends with y
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # message = "Hello, Dania!"
# # # # # # # # # # # # # # # # # # # # # # # message = message.upper()
# # # # # # # # # # # # # # # # # # # # # # # print(message)
# # # # # # # # # # # # # # # # # # # # # # # # upper_message = message.upper()
# # # # # # # # # # # # # # # # # # # # # # # # message = message.upper()
# # # # # # # # # # # # # # # # # # # # # # # # print(upper_message)
# # # # # # # # # # # # # # # # # # # # # # # # lower_message = message.lower()
# # # # # # # # # # # # # # # # # # # # # # # # print(lower_message)
# # # # # # # # # # # # # # # # # # # # # # # # capitalized_message = message.capitalize()
# # # # # # # # # # # # # # # # # # # # # # # # print(capitalized_message)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # model = "Apple iPhone 13"
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # def find_model(search_text):
# # # # # # # # # # # # # # # # # # # # # #     condition = search_text.lower() in model.lower()
# # # # # # # # # # # # # # # # # # # # # #     if condition:
# # # # # # # # # # # # # # # # # # # # # #         print('found')
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # while True:
# # # # # # # # # # # # # # # # # # # # # #     search = input(str('searched: '))
# # # # # # # # # # # # # # # # # # # # # #     find_model(search)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # message = '01234567890'
# # # # # # # # # # # # # # # # # # # # # sl = slice(1,5)
# # # # # # # # # # # # # # # # # # # # # print(message[sl])
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # def remove_vowels(document: str) -> str:
# # # # # # # # # # # # # # # # # # # #     golosni = "aeiouy"
# # # # # # # # # # # # # # # # # # # #     result = ""
# # # # # # # # # # # # # # # # # # # #     for i in document.lower():
# # # # # # # # # # # # # # # # # # # #         if i in golosni:
# # # # # # # # # # # # # # # # # # # #             print(f'ALARM: Document contain "{i}" from forbiden list')
# # # # # # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # # # # # #             print(f'{i} - OK')
# # # # # # # # # # # # # # # # # # # #             result += i
# # # # # # # # # # # # # # # # # # # #     print(result)
# # # # # # # # # # # # # # # # # # # #     return result
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # remove_vowels('aeiouyqwrtp')
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # def make_abbr(words: str) -> str:
# # # # # # # # # # # # # # # # # # # #     result = ""
# # # # # # # # # # # # # # # # # # # #     space_d = " "
# # # # # # # # # # # # # # # # # # # #     result += words[0]
# # # # # # # # # # # # # # # # # # # #     slice_magic = slice(1)
# # # # # # # # # # # # # # # # # # # #     if space_d in words:
# # # # # # # # # # # # # # # # # # # #         print('____________________________________________________space found')
# # # # # # # # # # # # # # # # # # # #         for i in words:
# # # # # # # # # # # # # # # # # # # #             print(i)
# # # # # # # # # # # # # # # # # # # #             if i == " ":
# # # # # # # # # # # # # # # # # # # #                 print(words.index(space_d))
# # # # # # # # # # # # # # # # # # # #                 slice_magic = slice(i)
# # # # # # # # # # # # # # # # # # # #                 print(slice_magic)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #     print('_________________________________________________________________')
# # # # # # # # # # # # # # # # # # # #     print(f'"{words}" converted to "{result.upper()}"')
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # make_abbr('national aeronautics space administration')
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # my_string = '01234 6789 11 13'
# # # # # # # # # # # # # # # # # # # # lf = ' '
# # # # # # # # # # # # # # # # # # # # x=
# # # # # # # # # # # # # # # # # # # # sl = slice(0,x)
# # # # # # # # # # # # # # # # # # # # print(my_string[sl])
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # def make_abbr(words: str) -> str:
# # # # # # # # # # # # # # # # # # # #     result = ""
# # # # # # # # # # # # # # # # # # # #     result += words[0]
# # # # # # # # # # # # # # # # # # # #     while True:
# # # # # # # # # # # # # # # # # # # #         for i in words:
# # # # # # # # # # # # # # # # # # # #             print(i)
# # # # # # # # # # # # # # # # # # # #             if i == " ":
# # # # # # # # # # # # # # # # # # # #                 print('CUT HERE______________________')
# # # # # # # # # # # # # # # # # # # #                 nextelement = words.index(i)+1
# # # # # # # # # # # # # # # # # # # #                 print(f'{nextelement} IS THIS')
# # # # # # # # # # # # # # # # # # # #                 result += words[nextelement]
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #         return result.upper()
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # print(make_abbr('national aeronautics space administration'))
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # def make_abbr(words: str) -> str:
# # # # # # # # # # # # # # # # # # # #     result = ""
# # # # # # # # # # # # # # # # # # # #     result += words[0]
# # # # # # # # # # # # # # # # # # # #     for i in words:
# # # # # # # # # # # # # # # # # # # #         thiselem = i
# # # # # # # # # # # # # # # # # # # #         print(thiselem)
# # # # # # # # # # # # # # # # # # # #         nextelem = words[words.index(i)+1]
# # # # # # # # # # # # # # # # # # # #         print(nextelem)
# # # # # # # # # # # # # # # # # # # #         if i == " ":
# # # # # # # # # # # # # # # # # # # #             result += nextelem
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #     return result.upper()
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # print(make_abbr('national aeronautics'))
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # def make_abbr(words: str) -> str:
# # # # # # # # # # # # # # # # # # # #     result = ""
# # # # # # # # # # # # # # # # # # # #     result += words[0]
# # # # # # # # # # # # # # # # # # # #     x = 0 # for index adding
# # # # # # # # # # # # # # # # # # # #     for i in range(len(words)):
# # # # # # # # # # # # # # # # # # # #         print(f"{(i)} is {words[i]}")        # (i) - index      ; words[i] - value
# # # # # # # # # # # # # # # # # # # #         if words[i] == " ":
# # # # # # # # # # # # # # # # # # # #             x = (i)
# # # # # # # # # # # # # # # # # # # #             result += words[x+1]
# # # # # # # # # # # # # # # # # # # #     print(f"{words} converted to {result.upper()}")
# # # # # # # # # # # # # # # # # # # #     return result.upper()
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # print(make_abbr("national aeronautics space administration"))
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # # # # # # # # # # # # # # # # # # def make_abbr(words: str) -> str:
# # # # # # # # # # # # # # # # # # #     if words == "":
# # # # # # # # # # # # # # # # # # #         return ""
# # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # #         result = ""
# # # # # # # # # # # # # # # # # # #         result += words[0]
# # # # # # # # # # # # # # # # # # #         for i in range(len(words)):
# # # # # # # # # # # # # # # # # # #             if words[i] == " ":
# # # # # # # # # # # # # # # # # # #                 result += words[(i)+1]
# # # # # # # # # # # # # # # # # # #     return result.upper()
# # # # # # # # # # # # # # # # # # # #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # def is_werewolf(target: str) -> bool:
# # # # # # # # # # # # # # # # # # #     target = target.lower()
# # # # # # # # # # # # # # # # # # #     check_here = ''
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #     for i in target:
# # # # # # # # # # # # # # # # # # #         if i == " " or i == "," or i == ":" or i == ";" or i == "?" or i == "!":
# # # # # # # # # # # # # # # # # # #             None
# # # # # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # # # # #             check_here += i
# # # # # # # # # # # # # # # # # # #     print("_____________________________________________________")
# # # # # # # # # # # # # # # # # # #     print(f"-> {target} - > {check_here} - > {check_here[::-1]}")
# # # # # # # # # # # # # # # # # # #     print("_____________________________________________________")
# # # # # # # # # # # # # # # # # # #     if check_here.upper() == check_here[::-1].upper() \
# # # # # # # # # # # # # # # # # # #             and\
# # # # # # # # # # # # # # # # # # #         check_here.lower() == check_here[::-1].lower():
# # # # # # # # # # # # # # # # # # #         return True
# # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # #         return False
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # print(is_werewolf("rotator"))
# # # # # # # # # # # # # # # # # # # print(is_werewolf("home"))
# # # # # # # # # # # # # # # # # # # print(is_werewolf("racecar"))
# # # # # # # # # # # # # # # # # # # print(is_werewolf("red rum sir is murder"))
# # # # # # # # # # # # # # # # # # # print(is_werewolf("eva, can I see bees in a cave"))
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # def happy_birthday() -> None:
# # # # # # # # # # # # # # # # # #     name = input(f"What's your name?")
# # # # # # # # # # # # # # # # # #     print(f"Happy birthday, {name}!")
# # # # # # # # # # # # # # # # # #     return f"Happy birthday, {name}!"
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # print(happy_birthday())
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # def parity_checker() -> None:
# # # # # # # # # # # # # # # # #     number = int(input(f"What number do you want to check?"))
# # # # # # # # # # # # # # # # #     if number % 2 > 0:
# # # # # # # # # # # # # # # # #         print("Odd")
# # # # # # # # # # # # # # # # #     if number % 2 == 0:
# # # # # # # # # # # # # # # # #         print("Even")
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # parity_checker()
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # def get_success_rate(statistics: str) -> int:
# # # # # # # # # # # # # # # #     if len(statistics) == 0:
# # # # # # # # # # # # # # # #         return 0
# # # # # # # # # # # # # # # #     fail = 0
# # # # # # # # # # # # # # # #     success = 0
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     for i in statistics:
# # # # # # # # # # # # # # # #         if i == "0":
# # # # # # # # # # # # # # # #             fail += 1
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     success = len(statistics) - fail
# # # # # # # # # # # # # # # #     if success == 0:
# # # # # # # # # # # # # # # #         return 0
# # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # #         return round((len(statistics)-fail)/(len(statistics)/100))
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(get_success_rate("1010101010")) # 50% 5 -1 5 -0
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # def check_fermat(a, b, c, n):
# # # # # # # # # # # # # # # #     if n > 2 and (a**n + b**n == c**n):
# # # # # # # # # # # # # # # #         print("Holy smokes, Fermat was wrong!")
# # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # #         print("No, that doesn’t work.")
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # def check_numbers():
# # # # # # # # # # # # # # # #     a = int(input("Choose a number for a: "))
# # # # # # # # # # # # # # # #     b = int(input("Choose a number for b: "))
# # # # # # # # # # # # # # # #     c = int(input("Choose a number for c: "))
# # # # # # # # # # # # # # # #     n = int(input("Choose a number for n: "))
# # # # # # # # # # # # # # # #     return check_fermat(a, b, c, n)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # check_numbers()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # from random import Random
# # # # # # # # # # # # # # # from math import ldexp
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # class FullRandom(Random):
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     def random(self):
# # # # # # # # # # # # # # #         mantissa = 0x10_0000_0000_0000 | self.getrandbits(52)
# # # # # # # # # # # # # # #         exponent = -53
# # # # # # # # # # # # # # #         x = 0
# # # # # # # # # # # # # # #         while not x:
# # # # # # # # # # # # # # #             x = self.getrandbits(32)
# # # # # # # # # # # # # # #             exponent += x.bit_length() - 32
# # # # # # # # # # # # # # #         return ldexp(mantissa, exponent)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # fr = FullRandom()
# # # # # # # # # # # # # # # print(fr.random())
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # fr.random()
# # # # # # # # # # # # # # ################LISTS#####################
# # # # # # # # # # # # # # numbers = [10, True, "guga", 11,12,13]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(numbers[0])
# # # # # # # # # # # # # # print(len(numbers))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for index in range(len(numbers)):
# # # # # # # # # # # # # #     print(numbers[index])
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for num in numbers:
# # # # # # # # # # # # # #     print(num)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print ("_"*10)
# # # # # # # # # # # # # # x = 456
# # # # # # # # # # # # # # numbers[0] = 45
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # numbers.append(100)
# # # # # # # # # # # # # # for num in numbers:
# # # # # # # # # # # # # #     print(num)
# # # # # # # # # # # # # # numbers[0] = x
# # # # # # # # # # # # # # numbers.append(100)
# # # # # # # # # # # # # # for num in numbers:
# # # # # # # # # # # # # #     print(num)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # numbers.insert(3, 1000) # index, value
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for num in numbers:
# # # # # # # # # # # # # #     print(num)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # numbers[-1] = 15 # last elem
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # y = "afdfgjkldhfg aslkdf asldjfasf"
# # # # # # # # # # # # # # xt = list(y)
# # # # # # # # # # # # # # print(xt)
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # def make_stickers(details_count: int, robot_part: str) -> list:
# # # # # # # # # # # # #     if details_count == 0:
# # # # # # # # # # # # #         return []
# # # # # # # # # # # # #     result = []
# # # # # # # # # # # # #     print(result)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #     details_numbers = list(range(1,details_count + 1))
# # # # # # # # # # # # #     print(details_numbers)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     for i in range(1,details_count + 1):
# # # # # # # # # # # # #
# # # # # # # # # # # # #         print(i)
# # # # # # # # # # # # #         temporary = f"{robot_part} detail #{i}"
# # # # # # # # # # # # #         print(temporary)
# # # # # # # # # # # # #         result.append(temporary)
# # # # # # # # # # # # #     print(result)
# # # # # # # # # # # # #     return result
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # make_stickers(3, "Body")
# # # # # # # # # # # #
# # # # # # # # # # # # # x_direction = '_|'*10
# # # # # # # # # # # # # for i in x_direction:
# # # # # # # # # # # # #     print('q')
# # # # # # # # # # # # # print(x_direction)
# # # # # # # # # # # #
# # # # # # # # # # # # #___________________________________________________________________________________
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # def double_power(current_powers: list) -> list:
# # # # # # # # # # # #     result = []
# # # # # # # # # # # #     for i in current_powers:
# # # # # # # # # # # #         result.append(i*2)
# # # # # # # # # # # #     return result
# # # # # # # # # # #
# # # # # # # # # # # def is_sorted(box_numbers: list) -> bool:
# # # # # # # # # # #     new_list = []
# # # # # # # # # # #     for i in box_numbers:
# # # # # # # # # # #         new_list.append(i)
# # # # # # # # # # #     new_list.sort()
# # # # # # # # # # #     if box_numbers == new_list:
# # # # # # # # # # #         return True
# # # # # # # # # # #     else:
# # # # # # # # # # #         return False
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # print(is_sorted([1, 2, 3, 4, 5]))
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # is_sorted([1, 2, 3, 4, 5]) is True
# # # # # # # # # # # # is_sorted([0, 1, 1, 1, 2]) is True
# # # # # # # # # # # # is_sorted([1, 5, 7]) is True
# # # # # # # # # # # # is_sorted([1, 2, 11]) is True
# # # # # # # # # # # # is_sorted([5]) is True
# # # # # # # # # # # # is_sorted([]) is True
# # # # # # # # # # # # is_sorted([0, 3, 1, 2, 2, 2]) is False
# # # # # # # # # # # # is_sorted([1, 11, 2]) is False
# # # # # # # # # # # # is_sorted([5, 3]) is False
# # # # # # # # # # #
# # # # # # # # # # def get_location(coordinates: list, commands: list) -> list:
# # # # # # # # # #     for i in commands:
# # # # # # # # # #         result = coordinates
# # # # # # # # # #         if i == "forward":
# # # # # # # # # #             coordinates[1] += 1
# # # # # # # # # #         elif i == "back":
# # # # # # # # # #             coordinates[1] -= 1
# # # # # # # # # #         elif i == "right":
# # # # # # # # # #             coordinates[0] += 1
# # # # # # # # # #         else:
# # # # # # # # # #             coordinates[0] -= 1
# # # # # # # # # #         print(f"result {coordinates}")
# # # # # # # # # #     return coordinates
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # print(get_location([0, 5], ["back", "back", "back", "right", "left", "forward"]))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # import math
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def get_plan(current_production: int, month: int, percent: int) -> list:
# # # # # # # # #     result = []
# # # # # # # # #     for i in range(1, month + 1):
# # # # # # # # #         current_production = int(math.floor(current_production))
# # # # # # # # #         current_production = int(round(current_production))
# # # # # # # # #         current_production *= (1 + (percent / 100))
# # # # # # # # #         result.append(int(current_production))
# # # # # # # # #     return result
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(get_plan(1000, 6, 35))  # [1350, 1822, 2459, 3319, 4480, 6048]
# # # # # # # #
# # # # # # # # from math import floor
# # # # # # # #
# # def get_speed_statistic(test_results: list) -> list:
# #     if len(test_results) < 1:
# #         return [0,0,0]
# #     if len(test_results) == 1:
# #         return [test_results[0]]*3
# #     result = []
# #     avg_counter = 0
# #     print(f"inc looks like this: {test_results}")
# #     test_results.sort()
# #     print(f"result after sort: {test_results}")
# #     result.append(test_results[0])
# #     result.append(test_results[-1])
# #
# #
# #     for i in test_results:
# #         avg_counter += i
# #
# #     print(f"avg counter = {avg_counter}")
# #     avg_counter = (avg_counter / len(test_results))
# #     result.append(int(avg_counter))
# #     print(f"min: {result[0]}")
# #     print(f"max: {result[-1]}")
# #     print(f"avg = {avg_counter}")
# #     print(f"result looks like this: {result}")
# #     print('_'*10)
# #
# #     return result
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # print(get_speed_statistic([10, 10, 11, 9, 12, 8])) # [8, 12, 10]
# # # # # # # # print(get_speed_statistic([10])) #[10, 10, 10]
# # # # # # # # print(get_speed_statistic([])) #[0, 0, 0]
# # # # # # # # print(get_speed_statistic([8, 9, 9, 9])) #== [8, 9, 8]
# # # # # # # # print(get_speed_statistic([5])) #== [5, 5, 5]
# # # # # # #
# # # # # # #
# # # # # # # #_________________________________________________________________________________________
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # def split_string(string: str) -> list:
# # # # # # #     if len(string) == 1:
# # # # # # #         return [string[0]+"_"]
# # # # # # #     result = []
# # # # # # #     temporary_list = []
# # # # # # #     for i in string:
# # # # # # #         temporary_list.append(i)
# # # # # # #     for i in range(1,len(temporary_list)):
# # # # # # #         result.append(temporary_list[i-1] + temporary_list [i])
# # # # # # #     if len(temporary_list) % 2 == 0:
# # # # # # #         return result [::2]
# # # # # # #     last_elem = result[-1]
# # # # # # #     last_elem = last_elem[-1] + "_"
# # # # # # #     result = result[::2]
# # # # # # #     result.append(last_elem)
# # # # # # #     return result
# # # # # # #
# # # # # # #
# # # # # # # print(split_string("a"))
# # # # # # # print(split_string("abcdefg"))
# # # # # # #
# # # # # # #
# # # # # #
# # # # # # # __________________________________________________________________________________
# # # # # #
# # # # # #
# # # # # # def scrolling_text(string: str) -> list:
# # # # # #     result_list = [string.upper()]
# # # # # #     tempo_string = string
# # # # # #
# # # # # #     for i in string:
# # # # # #         tempo_string = tempo_string [1::]
# # # # # #         tempo_string = tempo_string.upper() + i.upper()
# # # # # #         result_list.append(tempo_string)
# # # # # #     result_list.pop()
# # # # # #     return result_list
# # # # # #
# # # # # # print(scrolling_text("robot"))
# # # # #
# # # # # def check_number(number: int) -> list:
# # # # #     result = []
# # # # #     if number > 0:
# # # # #         result.append(True)
# # # # #     else:
# # # # #         result.append(False)
# # # # #     if number % 2 == 0:
# # # # #         result.append(True)
# # # # #     else:
# # # # #         result.append(False)
# # # # #     if number % 10 == 0:
# # # # #         result.append(True)
# # # # #     else:
# # # # #         result.append(False)
# # # # #     return  result
# # # #
# # # #
# # # # def get_lists_sum(ls1: list, ls2: list) -> int:
# # # #     result = 0
# # # #
# # # #     for i in ls1:
# # # #         result += i
# # # #
# # # #     print("*"*10)
# # # #
# # # #     for i in ls2:
# # # #         result += i
# # # #
# # # #     return result
# # # #
# # # #
# # # # print(get_lists_sum([1, 2], [3, 4])) == 10  # 1 + 2 + 3 + 4 = 10
# # # # print(get_lists_sum([], [])) == 0
# # # #
# # #
# # #
# # #
# # # def combine_lists(ls1: list, ls2: list) -> list:
# # #     result = [0] * len(ls1)
# # #     print(result)
# # #     for i in range(len(result)):
# # #         result[i] += ls1[i] + ls2[i]
# # #         print(result[i])
# # #     return result
# # #
# # #
# # #         # result[0] += ls1[0] + ls2[0]
# # #         # result[1] += ls1[1] + ls2[1]
# # #         # result[2] += ls1[2] + ls2[2]
# # #
# # #     print(result)
# # #
# # #
# # #     # print(result)
# # #
# # #
# # # combine_lists([1, 2, 5], [3, 6, 1]) #== [4, 8, 6]
# # #
# #
# #
# # # всегда до конца 1-й строки по очереди
# # #
# #
# #
# # def spiral(resolution: int):
# #     result = [0] * resolution ** 2
# #     result[-1] = resolution ** 2
# #     result = result[::-1]
# #
# #     for i in range(1, len(result)):
# #         print(f"(i) = {(i)} // [i] = {[i]}")
# #         if result[i] < result[i - 1]:
# #             result[i] = result[i - 1] - 1
# #
# #     result = result[::-1]
# #
# #
# #
# #     #result.insert(resolution, "change direction")
# #     # for i in result[resolution-1::resolution+1]:
# #     #     result.insert(i,'change direction')
# #     # result.append('change direction')
# #     # print(f"result list at this stage: {result}")
# #
# #
# #
# #     print(f"result list at final stage: {result}")
# #     return result
# #
# # spiral(3)
#
# # def is_jumping(number: int) -> str:
# #     number = str(number)
# #     test = []
# #     errors = 0
# #     for i in number:
# #         test.append(i)
# #     if len(test) < 2:
# #         return "JUMPING"
# #     for i in range(1, len(test)):
# #         y = int(test[i])
# #         x = int(test[i - 1])
# #         if (x - y) == 1\
# #                 or (x - y) == -1\
# #                 or (x + y) == 1 \
# #                 or (x + y) == -1:
# #             errors += 0
# #         else:
# #             errors += 1
# #     if errors == 0:
# #         return "JUMPING"
# #     else:
# #         return "NOT JUMPING"
# #
# #
# # is_jumping(12543)
#
#
# def is_special_number(number: int) -> str:
#     special_numbers = [0,1,2,3,4,5]
#     list_but_number = []
#     to_compare = []
#     counter = 0
#     for i in str(number):
#         list_but_number.append(i)
#     for i in list_but_number:
#         to_compare.append(int(i))
#
#
#     print(special_numbers)
#     print(list_but_number)
#     print(to_compare)
#     for i in to_compare:
#         if i in special_numbers:
#             counter += 1
#     if counter == len(to_compare):
#         return "Special!!"
#     else:
#         return "NOT!!"

#
# def is_tidy(number: int) -> bool:
#     list_str = []
#     list_num = []
#     counter = 0
#     for i in str(number):
#         list_str.append(i)
#     for i in list_str:
#         list_num.append(int(i))
#     if len(list_num) == 1:
#         return True
#     for i in range(1, len(list_num)):
#         if list_num[i - 1] <= list_num[i]:
#             counter += 1
#     if counter +1 == len(list_num):
#         return True
#     else:
#         return False

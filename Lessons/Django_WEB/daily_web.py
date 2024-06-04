# import copy
# import math
# import random
# from typing import *
#
#
# def flatten_and_sort(lst: list) -> list:
#     if len(lst):
#         result = []
#         for nested in lst:
#             result += nested
#         return sorted(result)
#     return []
#
#
# def is_isogram(string: str) -> bool:
#     print(set(string))
#     print(string)
#     if len(set(string.lower())) == len(string.lower()):
#         return True
#     return False
#
#
# def longest_substring(string: str) -> int:
#     if len(string) == len(set(string)):
#         return len(string)
#     max_len = [0]
#     temp_str = ""
#     for i in string:
#         if i not in temp_str:
#             temp_str += i
#         else:
#             max_len.append(len(temp_str))
#             temp_str = temp_str[temp_str.index(i) + 1:] + i
#     return max(max_len)
#
#
# def pluck(dicts: list, name: str) -> list:
#     result = []
#     for cur_dict in dicts:
#         if name in cur_dict.keys():
#             result.append(cur_dict[name])
#         else:
#             result.append(None)
#     return result
#
#
# def xo(string: str) -> bool:
#     return True if string.lower().count("x") == string.lower().count(
#         "o") else False
#
#
# class PaginationHelper:
#     content = []
#     iter_index = 0
#
#     def __init__(self, collection: list, items_per_page: int) -> None:
#         self.collection = collection
#         self.items_per_page = items_per_page
#
#         for i in range(0, (len(self.collection) // items_per_page) + 1):
#             self.content.append(self.collection[
#                                 self.iter_index: self.iter_index + self.items_per_page:])
#             self.iter_index += items_per_page
#
#     def item_count(self) -> int:
#         return len(self.collection)
#
#     def page_count(self) -> int:
#         if len(self.collection) == 0:
#             return 0
#         if self.items_per_page == 0:
#             return 0
#         result = len(self.collection) % self.items_per_page
#         if result > 0:
#             return (len(self.collection) // self.items_per_page) + 1
#         return len(self.collection) // self.items_per_page
#
#     def page_item_count(self, page_index: int) -> int:
#         try:
#             return len(self.content[page_index])
#         except IndexError:
#             return -1
#
#     def page_index(self, item_index: int) -> int:
#         if item_index < 0:
#             return -1
#
#         if len(self.collection) == 0:
#             return -1
#         try:
#             for element in self.content:
#                 if self.collection[item_index] in element:
#                     return self.content.index(element)
#         except IndexError:
#             return -1
#
#
# def find_children(santas_list: list, children: list) -> list:
#     return sorted([kid for kid in children if kid in santas_list])
#
#
# def triangle(row: str) -> str:
#     if len(row) == 1:
#         return row[0]
#
#     colours = "RGB"
#     all_rows = [row]
#     next_row = ""
#
#     while len(all_rows) < len(row):
#         for iteration in range(1, len(all_rows[-1])):
#             prev = row[iteration - 1]
#             current = row[iteration]
#
#             if prev == current:
#                 next_row += prev
#             else:
#                 for colour in colours:
#                     if colour not in prev + current:
#                         next_row += colour
#
#         all_rows.append(next_row)
#         next_row = ""
#
#     return all_rows[-1]
#
#
# def compression(chars: list) -> str:
#     if len(chars) == 1:
#         return 1
#     unique_and_order = []
#     for i in chars:
#         if i not in unique_and_order:
#             unique_and_order.append(i)
#     print(unique_and_order)
#     result = ""
#     for i in unique_and_order:
#         if chars.count(i) == 1:
#             result += i
#         result += f"{i}{chars.count(i)}"
#     print(result)
#     return result
#
#
# def sum_of_a_beach(beach: str) -> int:
#     return sum(
#         [beach.lower().count(i) for i in ("sand", "water", "fish", "sun")])
#
#
# def valpa():
#     import random
#     result = ""
#     for i in range(30):
#         result += random.choice(
#             [str(random.randint(1, 2)), str(random.randint(1, 2)),
#              chr(random.randint(97, 122)).upper(),
#              chr(random.randint(97, 122)).lower(), ])
#     return result
#




import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    for filename in files:
        if os.path.isfile(os.path.join(folder_path, filename)):
            if "test pref" in filename:
                new_filename = filename.replace("test pref", "")
                src = os.path.join(folder_path, filename)
                dst = os.path.join(folder_path, new_filename)
                os.rename(src, dst)

folder_path = "D:/export iphone manga/Joshikousei to Seishokusha-san/"
rename_files(folder_path)















#
# def longest_vowel_chain(string: str) -> int:
#     if not len(string):
#         return 0
#     vowels = "aeiou"
#     result = 0
#     counter = 0
#     for i in string:
#         if i in vowels:
#             counter += 1
#         else:
#             if result < counter:
#                 result = counter
#             counter = 0
#
#     return result
#
#
# def shoot(results: list) -> str:
#     p1_score = 0
#     p2_score = 0
#     multiplier = 0
#     for every_try in results:
#         # [{P1:'XX'', P2:'XO'}, True]
#         multiplier = 2 if every_try[1] is True else 1
#         p1_score += every_try[0]["P1"].count("X") * multiplier
#         p2_score += every_try[0]["P2"].count("X") * multiplier
#     if not p1_score == p2_score:
#         if p1_score > p2_score:
#             return "Pete Wins!"
#         else:
#             return "Phil Wins!"
#     return "Draw!"
#
#
# class MinStack:
#     def __init__(self) -> None:
#         self.stack = []
#
#     def push(self, value: int) -> None:
#         self.stack.append(value)
#
#     def pop(self) -> None:
#         self.stack.pop(-1)
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def get_min(self) -> int:
#         return min(self.stack)
#
#
# def find_unknown_number(first: int, second: int, third: int) -> int:
#     for i in range(1, 200):
#         if i % 3 == first:
#             if i % 5 == second:
#                 if i % 7 == third:
#                     return i
#
#
# def discover_original_price(discounted_price: float,
#                             sale_percentage: float) -> float:
#     return round((discounted_price / (100 - sale_percentage)) * 100, 2)
#
#
# def buy_tofu(cost: int, box: str) -> list or str:
#     print(cost)
#     print(box)
#     box = box.split()
#     result = [box.count("mon"), box.count("monme"),
#               box.count("mon") + box.count("monme") * 60, ]
#     min_amount = 0
#     if result[1] > 0:
#         for i in range(result[1]):
#             if cost // 60:
#                 min_amount += 1
#                 cost -= 60
#     if result[0] >= cost:
#         min_amount += cost
#
#     result.append(min_amount)
#     if result[3] == 0:
#         return "leaving the market"
#     if cost % 60 > result[0]:
#         return "leaving the market"
#     return result
#
#
# def is_valid_ip(ip_address: str) -> bool:
#     ip_address = ip_address.split(".")
#     if len(ip_address) != 4:
#         return False
#     for i in ip_address:
#         try:
#             int(i)
#         except Exception:
#             return False
#         if " " in i:
#             return False
#         if int(i) < 0:
#             return False
#         if len(i) > 1:
#             if int(i[0]) == 0:
#                 return False
#         if not int(i) in range(255 + 1):
#             return False
#     return True
#
#
# def trotter(number: int) -> int | str:
#     if number == 0:
#         return "INSOMNIA"
#
#     digits_seen = set()
#     i = 1
#
#     while len(digits_seen) < 10:
#         current_number = i * number
#         digits_seen.update(set(str(current_number)))
#         i += 1
#
#     return current_number
#
#
# def longest_common_prefix(strings_list: list) -> str:
#     if not strings_list:
#         return ""
#
#     min_len = min(len(s) for s in strings_list)
#
#     for i in range(min_len):
#         char = strings_list[0][i]
#         if not all(s[i] == char for s in strings_list):
#             return strings_list[0][:i]
#
#     return strings_list[0][:min_len]
#
#
# def scramble(first_string: str, second_string: str) -> bool:
#     print(first_string)
#     print(second_string)
#     for i in second_string:
#         if i in first_string:
#             if not first_string.count(i) >= second_string.count(i):
#                 return False
#         else:
#             return False
#     return True
#
#
# def credit_card_mask(card_number: str) -> str:
#     return f"{'#' * len(card_number[:-4:])}{card_number[-4::]}"
#
#
# def is_solved(board: list) -> int:
#     param = 3
#     for i in range(3):
#         param -= 1
#         if board[0][i] == board[1][1] == board[2][param]:
#             if board[0][i] != 0:
#                 if board[0][i] == 1:
#                     return 1
#                 return 2
#
#         if len(set(board[i])) == 1:
#             if board[i][0] != 0:
#                 if board[i][0] == 1:
#                     return 1
#                 return 2
#
#     for row in board:
#         if 0 in row:
#             return -1
#     return 0
#
#
# def is_happy(number):
#     def get_next(n):
#         total_sum = 0
#         while n > 0:
#             n, digit = divmod(n, 10)
#             total_sum += digit ** 2
#         return total_sum
#
#     slow = number
#     fast = get_next(number)
#
#     while fast != 1 and slow != fast:
#         slow = get_next(slow)
#         fast = get_next(get_next(fast))
#
#     return fast == 1


# flake8: noqa E501


# "{'1-800-HOLY-COT', '1-800-INK-WANT', '1-800-HOLY-ANT'}"


# def make_readable(seconds: int) -> str:
#     if seconds > 359999:
#         return ""
#     result = ""
#     hours, minutes = 0, 0
#     while seconds >= 3600:
#         hours += 1
#         seconds -= 3600
#     while seconds >= 60:
#         minutes += 1
#         seconds -= 60
#
#     result = f"0{hours}:" if len(str(hours)) == 1 else f"{hours}:"
#     if minutes < 10:
#         result += f"0{minutes}:"
#     else:
#         result += str(minutes)
#         result += ":"
#
#     if seconds < 10:
#         result += f"0{seconds}"
#     else:
#         result += str(seconds)
#     print(result)
#     return result
#
#
# def pendulum(lst: list) -> list:
#     left = []
#     mid = []
#     right = []
#     counter = 0
#     print(sorted(lst, reverse=True))
#     for i in sorted(lst, reverse=True):
#         print(i)
#         if counter % 2 == 0:
#             left.append(i)
#         else:
#             right.append(i)
#         counter += 1
#     print(left + mid + right[::-1])
#     return left + mid + right[::-1]
#
#
# def tv_remote(word: str) -> int:
#     all_rows = [["a", "b", "c", "d", "e", "1", "2", "3"],
#                 ["f", "g", "h", "i", "j", "4", "5", "6"],
#                 ["k", "l", "m", "n", "o", "7", "8", "9"],
#                 ["p", "q", "r", "s", "t", ".", "@", "0"],
#                 ["u", "v", "w", "x", "y", "z", "_", "/"], ]
#     steps = 0
#     current_position = [0, 0]  # Починаємо з літери "a"
#
#     for letter in word:
#         for i, row in enumerate(all_rows):
#             if letter in row:
#                 letter_index = row.index(letter)
#                 steps += (abs(current_position[0] - i) + abs(
#                     current_position[1] - letter_index) + 1)  # +1 за крок OK
#                 current_position = [i, letter_index]
#                 break
#
#     return steps
#
#
# WORDS = ["ACT", "ADD", "ALL", "APE", "AND", "ANN", "ANY", "ANT", "ARE", "ART",
#          "ASS", "BAD", "BAR", "BAT", "BAY", "BEE", "BIG", "BIT", "BOB", "BOY",
#          "BUN", "BUT", "CAN", "CAR", "CAT", "COT", "COW", "CUT", "DAD", "DAY",
#          "DEW", "DID", "DIN", "DOG", "DON", "DOT", "DUD", "EAR", "EAT", "EEL",
#          "EGG", "ERR", "EYE", "FAG", "FAR", "FLY", "FOR", "FUN", "FUR", "GAY",
#          "GET", "GOT", "GUM", "GUN", "GUY", "GUT", "GYM", "HAS", "HAT", "HER",
#          "HEY", "HIM", "HIS", "HIT", "HOW", "HUG", "HUN", "ICE", "INK", "ITS",
#          "IVE", "JAN", "JET", "JOB", "JOT", "JOY", "KEY", "LAP", "LAY", "LIE",
#          "LET", "LOG", "MAN", "MAP", "MAY", "MEN", "MOM", "MUD", "MUM", "NAP",
#          "NEW", "NOD", "NOT", "NOW", "OAR", "ODD", "OFF", "OLD", "ONE", "OUR",
#          "OUT", "PAN", "PAL", "PAT", "PAW", "PEN", "PET", "PIG", "PIT", "POT",
#          "PRO", "PUT", "QUO", "RAG", "RAM", "RAN", "RAP", "RAT", "RED", "RIP",
#          "ROD", "ROT", "RUN", "RUT", "SAT", "SAW", "SAY", "SEA", "SEE", "SEX",
#          "SHE", "SOY", "SUN", "SUX", "TAN", "TAT", "TEA", "THE", "TIN", "TIP",
#          "TIT", "TON", "TOP", "TOO", "TWO", "URN", "USE", "VAN", "VET", "VIP",
#          "WAR", "WAS", "WAY", "WED", "WHO", "WHY", "WIN", "WON", "XXX", "YAK",
#          "YAM", "YAP", "YOU", "YUM", "ZAP", "ZIP", "ZIT", "ZOO", "ABLE",
#          "ACED",
#          "AGOG", "AHEM", "AHOY", "ALLY", "AMEN", "ANTI", "ANTS", "ANUS",
#          "APES",
#          "ARMY", "ARSE", "ARTY", "AVID", "AWED", "BABY", "BARS", "BATS",
#          "BAYS",
#          "BEAR", "BEES", "BILL", "BITE", "BITS", "BLOW", "BLUE", "BOLD",
#          "BONE",
#          "BOOB", "BOOM", "BOSS", "BOYS", "BUFF", "BUNG", "BUNS", "BUMS",
#          "BURP",
#          "BUST", "BUSY", "BUZZ", "CANS", "CANT", "CARS", "CART", "CATS",
#          "CHAP",
#          "CHIC", "CHUM", "CIAO", "CLAP", "COCK", "CODE", "COOL", "COWS",
#          "COZY",
#          "CRAB", "CREW", "CURE", "CULT", "DADS", "DAFT", "DAWN", "DAYS",
#          "DECK",
#          "DEED", "DICK", "DING", "DOGS", "DOTS", "DOLL", "DOLT", "DONG",
#          "DOPE",
#          "DOWN", "DRAW", "DUCK", "DUDE", "DUMB", "DUTY", "EARL", "EARN",
#          "EARS",
#          "EASY", "EATS", "EDGE", "EELS", "EGGS", "ENVY", "EPIC", "EYES",
#          "FACE",
#          "FAGS", "FANG", "FARM", "FART", "FANS", "FAST", "FEAT", "FEET",
#          "FISH",
#          "FIVE", "FIZZ", "FLAG", "FLEW", "FLIP", "FLOW", "FOOD", "FORT",
#          "FUCK",
#          "FUND", "GAIN", "GEEK", "GEMS", "GIFT", "GIRL", "GIST", "GIVE",
#          "GLEE",
#          "GLOW", "GOLD", "GOOD", "GOSH", "GRAB", "GRIN", "GRIT", "GROT",
#          "GROW",
#          "GRUB", "GUNS", "GUSH", "GYMS", "HAIL", "HAIR", "HALO", "HANG",
#          "HATS",
#          "HEAD", "HEAL", "HEIR", "HELL", "HELP", "HERE", "HERO", "HERS",
#          "HIGH",
#          "HIRE", "HITS", "HOLY", "HOPE", "HOST", "HUNK", "HUGE", "HUNG",
#          "HUNS",
#          "HURT", "ICON", "IDEA", "IDLE", "IDOL", "IOTA", "JAZZ", "JERK",
#          "JESS",
#          "JETS", "JINX", "JOBS", "JOHN", "JOKE", "JUMP", "JUNE", "JULY",
#          "JUNK",
#          "JUST", "KATA", "KEYS", "KICK", "KIND", "KING", "KISS", "KONG",
#          "KNOB",
#          "KNOW", "LARK", "LATE", "LEAN", "LICE", "LICK", "LIKE", "LION",
#          "LIVE",
#          "LOGS", "LOCK", "LONG", "LOOK", "LORD", "LOVE", "LUCK", "LUSH",
#          "MAKE",
#          "MANY", "MART", "MATE", "MAXI", "MEEK", "MIKE", "MILD", "MINT",
#          "MMMM",
#          "MOMS", "MOOD", "MOON", "MOOT", "MUCH", "MUFF", "MUMS", "MUTT",
#          "NAPS",
#          "NAZI", "NEAT", "NECK", "NEED", "NEWS", "NEXT", "NICE", "NICK",
#          "NOON",
#          "NOSE", "NOTE", "OARS", "OATS", "ONCE", "ONLY", "OPEN", "ORGY",
#          "OVAL",
#          "OVER", "PANS", "PALS", "PART", "PAST", "PATS", "PAWS", "PEAR",
#          "PERT",
#          "PENS", "PETS", "PHEW", "PIPE", "PIPS", "PLAN", "PLUM", "PLUS",
#          "POET",
#          "POOF", "POOP", "POSH", "POTS", "PROS", "PSST", "PUKE", "PUNK",
#          "PURE",
#          "PUSH", "PUSS", "QUAD", "QUAK", "QUID", "QUIT", "RANT", "RAPE",
#          "RAPS",
#          "RAPT", "RATE", "RAMS", "RATS", "REAP", "RICK", "RING", "RIPE",
#          "ROOT",
#          "ROSE", "ROSY", "ROTS", "RUNT", "RUTS", "SAFE", "SAGE", "SANE",
#          "SAVE",
#          "SAWS", "SEEK", "SEXY", "SHAG", "SHIT", "SICK", "SIGH", "SIRE",
#          "SLAG",
#          "SLIT", "SLUT", "SNAP", "SNOG", "SNUG", "SOFT", "SOON", "SOUL",
#          "SOUP",
#          "SPRY", "STIR", "STUN", "SUCK", "SWAG", "SWAY", "TACT", "TANK",
#          "TANS",
#          "THAT", "THIS", "TIME", "TINS", "TINY", "TITS", "TOES", "TONS",
#          "TONY",
#          "TOPS", "TOYS", "UBER", "URNS", "USED", "USER", "USES", "VAIN",
#          "VAMP",
#          "VARY", "VEIN", "VENT", "VERY", "VEST", "VIEW", "VIVA", "VOLT",
#          "VOTE",
#          "WAFT", "WAGE", "WAKE", "WALK", "WALL", "WANG", "WANK", "WANT",
#          "WARD",
#          "WARM", "WARP", "WARS", "WART", "WASH", "WAVE", "WEAR", "WEDS",
#          "WEED",
#          "WEEN", "WELD", "WHAT", "WHEE", "WHEW", "WHIP", "WHIZ", "WHOA",
#          "WIFE",
#          "WILL", "WIND", "WING", "WINK", "WINS", "WIRE", "WISH", "WITH",
#          "WORD",
#          "WORK", "WRAP", "XMAN", "XMEN", "XRAY", "XTRA", "XXXX", "YANK",
#          "YAKS",
#          "YAMS", "YAPS", "YARD", "YARN", "YELP", "YERN", "YOKE", "YOLK",
#          "YULE",
#          "ZANY", "ZAPS", "ZIPS", "ZITS", "ZERO", "ZOOM", "ZOOS", ]
#
#
# def check_1800(string: str) -> set:
#     panel = {"2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL", "6": "MNO",
#              "7": "PQRS", "8": "TUV", "9": "WXYZ", }
#     codes = {str(i): [] for i in range(10_000)}
#     for word in WORDS:
#         code = ""
#         for letter in word:
#             for number in panel:
#                 if letter in panel[number]:
#                     code += number
#         codes[code].append(word)
#     cleared = {k: codes[k] for k in codes.keys() if len(codes[k])}
#     del codes
#     code_from_string = ""
#     for word in string.split("-")[2::]:
#         for letter in word:
#             for button in panel:
#                 if letter in panel[button]:
#                     code_from_string += button
#     codes_to_process = [[code_from_string[:4:], code_from_string[4::]],
#                         [code_from_string[:3:], code_from_string[3::]], ]
#     result = []
#
#     for code_pair in codes_to_process:
#         code1, code2 = code_pair
#         words1 = cleared.get(code1, [])
#         words2 = cleared.get(code2, [])
#         combinations = [(word1, word2) for word1 in words1 for word2 in words2]
#         for combination in combinations:
#             result.append(f"1-800-{combination[0]}-{combination[1]}")
#
#     return set(result)
#
#
# def duplicate_arguments(*args) -> bool:
#     if len(args) == len(set(args)):
#         return False
#     else:
#         return True
#
#
# def str_in_str(haystack: str, needle: str) -> int:
#     if not len(needle):
#         return 0
#     try:
#         return haystack.index(needle)
#     except Exception:
#         return -1
#
#
# def count_ones(left: int, right: int) -> int:
#     return sum(bin(i).count("1") for i in range(left, right + 1))
#
#
# def coupon_code(entered_code: str, correct_code: str, current_date: str,
#                 expiration_date: str, ) -> bool:
#     from datetime import datetime
#
#     if entered_code == correct_code:
#         return datetime.strptime(expiration_date,
#                                  "%B %d, %Y") >= datetime.strptime(
#             current_date, "%B %d, %Y")
#     return False
#
#
# coupon_code(entered_code="123", correct_code="123",
#             current_date="July 9, 2015", expiration_date="July 9, 2015", )
#
#
# def count_and_say(number: int) -> str:
#     if number == 1:
#         return "1"
#
#     result = "1"
#
#     for _ in range(number - 1):
#         current_char = result[0]
#         count = 1
#         new_result = ""
#
#         for i in range(1, len(result)):
#             if result[i] == current_char:
#                 count += 1
#             else:
#                 new_result += str(count) + current_char
#                 current_char = result[i]
#                 count = 1
#
#         new_result += str(count) + current_char
#         result = new_result
#
#     return result
#
#
# def one_down(txt: str) -> str:
#     if not isinstance(txt, str):
#         return "Input is not a string"
#     result = ""
#     for letter in txt:
#         if ord(letter) == 32:
#             result += " "
#         else:
#             if letter == "A":
#                 result += "Z"
#                 continue
#             if letter == "a":
#                 result += "z"
#                 continue
#             else:
#                 result += chr(ord(letter) - 1)
#     return result
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         import datetime
#
#         start = datetime.datetime.now()
#         func(*args)
#
#         print(
#             f"Function {func.__name__} execution takes {datetime.datetime.now() - start} s.")
#
#     return wrapper
#
#
# @timer
# def some_func(x: int, y: int) -> int:
#     result = 0
#     for i in range(10):
#         result += x - y ** 2
#     print(result)
#     return result
#
#
# def middle_character(word: str) -> str:
#     if not (len(word)):
#         return ""
#     lenw = len(word)
#     if lenw == 2:
#         return word
#     if lenw == 1:
#         return word
#     if lenw % 2 == 0:
#         return word[int(lenw / 2) - 1] + word[int(lenw / 2)]
#     return word[int(lenw / 2 - 0.5)]
def create_database():
    conn = sqlite3.connect('spaceship.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passengers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            country TEXT,
            blood_pressure TEXT,
            cholesterol_level TEXT,
            chronic_condition TEXT
        )
    ''')

    passengers_data = [
        ('Alice', 30, 'Female', 'USA', 'Normal', 'Normal', 'None'),
        ('Bob', 45, 'Male', 'UK', 'High', 'High', 'Diabetes'),
        ('Charlie', 50, 'Male', 'USA', 'Normal', 'High', 'None'),
        ('Diana', 35, 'Female', 'Canada', 'Normal', 'Normal', 'Asthma'),
        # Добавьте больше данных по желанию
    ]

    cursor.executemany('''
        INSERT INTO passengers (name, age, gender, country, blood_pressure, cholesterol_level, chronic_condition)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', passengers_data)

    conn.commit()
    conn.close()


def average_age():
    import sqlite3

    conn = sqlite3.connect('spaceship.db')
    cursor = conn.cursor()

    cursor.execute('SELECT AVG(age) FROM passengers')
    average_age = cursor.fetchone()[0]

    conn.close()

    return average_age


def gender_distribution():
    import sqlite3

    conn = sqlite3.connect('spaceship.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM passengers WHERE gender = "Male"')
    male_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM passengers WHERE gender = "Female"')
    female_count = cursor.fetchone()[0]

    total_passengers = male_count + female_count
    male_percentage = (male_count / total_passengers) * 100
    female_percentage = (female_count / total_passengers) * 100

    conn.close()

    return male_percentage, female_percentage


def most_common_countries():
    import sqlite3

    conn = sqlite3.connect('spaceship.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT country, COUNT(*) AS count
        FROM passengers
        GROUP BY country
        ORDER BY count DESC
        LIMIT 3
    ''')

    countries = cursor.fetchall()

    conn.close()

    return countries


def risky_passengers():
    import sqlite3

    conn = sqlite3.connect('spaceship.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, blood_pressure, cholesterol_level
        FROM passengers
        WHERE blood_pressure = "High" AND cholesterol_level = "High"
    ''')

    risky_passengers = cursor.fetchall()

    conn.close()

    return risky_passengers


def passengers_with_chronic_conditions():
    import sqlite3

    conn = sqlite3.connect('spaceship.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, chronic_condition
        FROM passengers
        WHERE chronic_condition != "None"
    ''')

    passengers_with_chronic_conditions = cursor.fetchall()

    conn.close()

    return passengers_with_chronic_conditions
#
# def roman_to_int(roman: str) -> int:
#     result = 0
#     data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
#             "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, }
#
#     prev_value = 0
#
#     for numeral in reversed(roman):
#         current_value = data[numeral]
#         if current_value < prev_value:
#             result -= current_value
#         else:
#             result += current_value
#         prev_value = current_value
#
#     return result
#
#
# def find_number(start: int, stop: int, string: str) -> list:
#     result = []
#     data_list = [data for data in range(start, stop + 1)]
#     print(string)
#     for number in data_list:
#         if str(number) in string:
#             print(string)
#             string = string.replace(str(number), ".")
#             print(string)
#         else:
#             result.append(number)
#     if not len(result):
#         return []
#     return result
#
#
# def multiples_3_5(number: int) -> int:
#     if number < 3:
#         return 0
#     data = []
#     for i in range(3, number):
#         flag_3 = i % 3 == 0
#         flag_5 = i % 5 == 0
#         if flag_3 or flag_5:
#             data.append(i)
#     print(data)
#     return sum(data)
#
#
# import itertools as it
#
#
# def equal_to_24(*cards) -> str:
#     for template in ["aZ(bX(cVd))", "(aZb)X(cVd)", "((aZb)Xc)Vd"]:
#         for card in it.permutations(cards):
#             for prod in it.product("*/+-", repeat=3):
#                 temp = template
#                 for char in (("Z", prod[0]), ("X", prod[1]), ("V", prod[2]),
#                              ("a", str(card[0])), ("b", str(card[1])),
#                              ("c", str(card[2])), ("d", str(card[3])),):
#                     temp = temp.replace(*char)
#                 try:
#                     if eval(temp) == 24:
#                         return temp
#                 except ZeroDivisionError:
#                     pass
#     return "It's not possible!"
#
#
# def credit_card_issuer_checking(number: int) -> str:
#     if len(str(number)) == 15:
#         amex_start = ["34", "37"]
#         if str(number)[:2:] in amex_start:
#             return "AMEX"
#     visa_lens = [13, 16]
#     if len(str(number)) in visa_lens:
#         if str(number)[:1:] == "4":
#             return "VISA"
#         if str(number)[:4:] == "6011":
#             return "Discover"
#         mastercard_start = ["51", "52", "53", "54", "55"]
#         if str(number)[:2:] in mastercard_start:
#             return "Mastercard"
#
#     return "Unknown"
#
#
# def perfect_number(number: int) -> bool:
#     if number <= 1:
#         return False
#
#     result = 1
#
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             result += i
#             complement = number // i
#             if i != complement:
#                 result += complement
#
#     return result == number
#
#
# def highest_and_lowest(string_of_nums: str) -> str:
#     try:
#         data_list = string_of_nums.split(sep=" ")
#         return f"{max(data_list)} {min(data_list)}"
#     except Exception:
#         return ""
#
#
# def test_highest_and_lowest(string_of_nums, max_min_string):
#     assert highest_and_lowest(string_of_nums) == max_min_string, (
#         f"Function 'highest_and_lowest' should return '{max_min_string}' "
#         f"when string is '{string_of_nums}'")
#
#
# def pascal_triangle_row(row_index: int) -> list:
#     def calculate_combination(n: int, k: int) -> int:
#         result = 1
#         for i in range(1, k + 1):
#             result *= n - i + 1
#             result //= i
#         return result
#
#     row = []
#     for k in range(row_index + 1):
#         row.append(calculate_combination(row_index, k))
#     return row
#
#
# def calculate_profit(**kwargs) -> int:
#     if 0 in kwargs:
#         return 0
#     old = amount
#     for year in range(period):
#         amount *= 1 + (percent / 100)
#         print(amount)
#     return amount - old
#
#
# def find_number(start: int, stop: int, string: str) -> list:
#     code = Counter(char for number in range(start, stop + 1) for char in
#                    str(number)) - Counter(string)
#     return [number for number in range(start, stop + 1) if
#             Counter(str(number)) == code]
#
#
# def get_plan(cur, month, perc):
#     result = []
#     for i in range(month):
#         result.append(math.floor(cur / 100 * (100 + perc)))
#         cur = result[-1]
#     return result
#
#
# def reverse_random_string(random_string: str, amount_of_symbols: int) -> str:
#     if len(random_string) < amount_of_symbols:
#         return random_string[::-1]
#     elif len(random_string) < 2 * amount_of_symbols:
#         fp = random_string[amount_of_symbols - 1:: -1]
#         sp = random_string[amount_of_symbols:]
#         return fp + sp
#     else:
#         result = ""
#         aos = amount_of_symbols
#         for i in range(0, len(random_string), 2 * amount_of_symbols):
#             result += random_string[i: i + aos][::-1]
#             result += random_string[i + aos: i + 2 * aos]
#         return result
#
#
# def snail(matrix: list) -> list:
#     result = []
#     while matrix:
#         result += matrix.pop(0)
#         if matrix and matrix[0]:
#             for row in matrix:
#                 result.append(row.pop())
#         if matrix:
#             result += matrix.pop()[::-1]
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 result.append(row.pop(0))
#     return result
#
#
# from itertools import combinations
#
#
# def unique_combinations(nums, k):
#     unique_combinations_set = set()
#     for combination in combinations(nums, k):
#         unique_combinations_set.add(tuple(sorted(combination)))
#     return sorted(unique_combinations_set)
#
#
# from collections import Counter
#
#
# def most_common_character(input_string):
#     char_count = Counter(input_string)
#     max_frequency = max(char_count.values())
#     most_common_chars = [char for char, freq in char_count.items() if
#                          freq == max_frequency]
#     return most_common_chars[0] if most_common_chars else None


#
# input_string = "hello world"
# result = most_common_character(input_string)
# print("Most common character:", result)

# JS TASK
# function canBuyBeer(age) {
#     if (age < 18) {
#         return 'You can not buy beer';
#     } else {
#         return 'You can buy beer';
#     }
# }
# function replaceA(input) {
#
#     return input.replace(/a|A/gi, '*');
# }

#
# from collections import OrderedDict
#
#
# def remove_duplicates(input_list):
#     return list(OrderedDict.fromkeys(input_list))


# js dail:
# for (let i = 3; i <= 11; i++) {
#     if (i % 2 !== 0) {
#         console.log(i);
#     }
# }

# for (let i = 5; i >= 1; i--) {
#     console.log(i);
# }

# let title = "Hello, world!";
#
# for (let i = 0; i < title.length; i++) {
#     console.log(title[i]);
# }
# function replaceSpaces(input) {
#   let modifiedString = '';
#   for (let i = 0; i < input.length; i++) {
#     if (input[i] === ' ') {
#       modifiedString += '-';
#     } else {
#       modifiedString += input[i];
#     }
#   }
#   return modifiedString;
# }
# function
# countMs(text)
# {
#     let
# uppercaseCount = 0;
# let
# lowercaseCount = 0;
#
# for (let i = 0; i < text.length; i++)
# {
# if (text[i] === 'M')
# {
#     uppercaseCount + +;
# } else if (text[i] === 'm') {
# lowercaseCount++;
# }
# }
#
# return uppercaseCount + lowercaseCount;
# }
# const title = 'Strings';
#
# for (let i = 0; i < title.length; i++) {
#     console.log(title[i]);
# }
# function
# calculateTaxes(income)
# {
#     let
# taxAmount;
#
# if (income <= 1000)
# {
#     taxAmount = income * 0.02; // 2 %
# } else if (income <= 10000) {
# taxAmount = 1000 * 0.02 + (income - 1000) * 0.03; // 2 % for the first 1000, 3 % for the rest up to 10000
# } else {
# taxAmount = 1000 * 0.02 + 9000 * 0.03 + (income - 10000) * 0.05; // 2 % for the first 1000, 3 % for the next 9000, 5 % for the rest
# }
#
# return taxAmount;
# }

# function printFromTo(input, start, end) {
#   if (start < 0 || end >= input.length || start > end) {
#     console.log("Invalid start or end index.");
#     return;
#   }
#
#   for (let i = start; i <= end; i++) {
#     console.log(input[i]);
#   }
# }

# function
# printBackwards(input, start, end)
# {
#
# if (start < 0 | | end >= input.length | | start > end)
# {
#     console.log("Invalid start or end index.");
# return;
# }
#
# let
# reversedSubstring = input.reverse()
#
# for (let i = 0; i < reversedSubstring.length; i++) {
#     console.log(reversedSubstring[(i + start) % reversedSubstring.length]);
# }
#
# }
# /**
#  * This comment gives you autocompletion
#  *
#  * @param {string} input
#  * @param {number} start
#  * @param {number} end
#  */
# function printBackwards(input, start, end) {
#   let substring = input.substring(start, end+1);
#   let reversedStr = substring.split("").reverse().join("");
#     for (let i = 0; i < reversedStr.length; i++) {
#     console.log(reversedStr[i]);
#   }
# }
# function isSubstring(phrase, part) {
#     return phrase.includes(part);
# }
#
# // Example usage:
# console.log(isSubstring("Hello, world!", "world")); // true
# console.log(isSubstring("Hello, world!", "universe")); // false
# const title = 'Strings';
#
# for (let i = 0; i < title.length; i++) {
#     console.log(title[i]);
# }
# /**
#  * This comment gives you autocompletion
#  *
#  * @param {string} input
#  */
# function convertToUpperCase(input) {
#   return input.toUpperCase()
# }
#


# def next_smaller(number: int) -> int:
#     digits = list(str(number))
#     i = len(digits) - 2
#     while i >= 0 and digits[i] <= digits[i + 1]:
#         i -= 1
#     if i == -1:
#         return -1
#     j = len(digits) - 1
#     while digits[j] >= digits[i]:
#         j -= 1
#     digits[i], digits[j] = digits[j], digits[i]
#     digits[i + 1:] = reversed(digits[i + 1:])
#     result = int("".join(digits))
#     return result
#
#
# def intersection_of_two(nums1: list, nums2: list) -> list:
#     data = list(set(nums1)) + list(set(nums2))
#     data_dict = {key: data.count(key) for key in data}
#     result = [num for num in data_dict if data_dict[num] == 2]
#     result.sort()
#     return result
#
#
# def performant_smallest(nums: list, n: int) -> list:
#     condition = nums.copy()
#     condition.sort()
#     condition = condition[:n:]
#     result = []
#     for num in nums:
#         if num in condition:
#             result.append(num)
#             condition.remove(num)
#     print(result)
#     return result
#
#
# def performant_smallest(nums: list, n: int) -> list:
#     if n == len(nums):
#         return nums
#     try:
#         target = (list(set(nums))[n:n + 1:])[0]
#     except Exception:
#         target = sorted(nums)[-1]
#
#     result = []
#     for i in nums:
#         if i < target:
#             result.append(i)
#             if len(result) == n:
#                 break
#     return result
#
#
# def climb_stairs(number: int) -> int:
#     if number <= 2:
#         return number
#     first, second = 1, 2
#     for _ in range(3, number + 1):
#         third = first + second
#         first, second = second, third
#     return second
#
#
# def choose_best_sum(limit: int, number_of_towns: int,
#                     list_of_distances: list) -> int:
#     from itertools import combinations
#     best_sum = None
#     for towns in combinations(list_of_distances, number_of_towns):
#         current_sum = sum(towns)
#         if current_sum <= limit:
#             if best_sum is None or current_sum > best_sum:
#                 best_sum = current_sum
#     return best_sum
#
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# def kth_smallest(root, k):
#     stack = []
#     while root or stack:
#         while root:
#             stack.append(root)
#             root = root.left
#         root = stack.pop()
#         k -= 1
#         if k == 0:
#             break
#         root = root.right
#     return root.val
#
#
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
#
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()
#
#
# class BstNode:
#
#     def __init__(self, key):
#         self.key = key
#         self.right = None
#         self.left = None
#
#     def insert(self, key):
#         if self.key == key:
#             return
#         elif self.key < key:
#             if self.right is None:
#                 self.right = BstNode(key)
#             else:
#                 self.right.insert(key)
#         else:  # self.key > key
#             if self.left is None:
#                 self.left = BstNode(key)
#             else:
#                 self.left.insert(key)
#
#     def display(self):
#         lines, *_ = self._display_aux()
#         for line in lines:
#             print(line)
#
#     def _display_aux(self):
#         """Returns list of strings, width, height, and horizontal coordinate of the root."""
#         # No child.
#         if self.right is None and self.left is None:
#             line = '%s' % self.key
#             width = len(line)
#             height = 1
#             middle = width // 2
#             return [line], width, height, middle
#
#         # Only left child.
#         if self.right is None:
#             lines, n, p, x = self.left._display_aux()
#             s = '%s' % self.key
#             u = len(s)
#             first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
#             second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
#             shifted_lines = [line + u * ' ' for line in lines]
#             return [first_line,
#                     second_line] + shifted_lines, n + u, p + 2, n + u // 2
#
#         # Only right child.
#         if self.left is None:
#             lines, n, p, x = self.right._display_aux()
#             s = '%s' % self.key
#             u = len(s)
#             first_line = s + x * '_' + (n - x) * ' '
#             second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
#             shifted_lines = [u * ' ' + line for line in lines]
#             return [first_line,
#                     second_line] + shifted_lines, n + u, p + 2, u // 2
#
#         # Two children.
#         left, n, p, x = self.left._display_aux()
#         right, m, q, y = self.right._display_aux()
#         s = '%s' % self.key
#         u = len(s)
#         first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (
#                 m - y) * ' '
#         second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (
#                 m - y - 1) * ' '
#         if p < q:
#             left += [n * ' '] * (q - p)
#         elif q < p:
#             right += [m * ' '] * (p - q)
#         zipped_lines = zip(left, right)
#         lines = [first_line, second_line] + [a + u * ' ' + b for a, b in
#                                              zipped_lines]
#         return lines, n + m + u, max(p, q) + 2, n + u // 2
#
#
# def date_generated(d1, d2):
#     import datetime
#     import random
#     start = datetime.datetime.strptime(d1, '%d-%m-%Y')
#     end = datetime.datetime.strptime(d2, '%d-%m-%Y')
#     intervalo = [start + datetime.timedelta(x) for x in
#                  range(int((end - start).days) + 1)]
#     datas = []
#     for data in intervalo:
#         datas.append(data.strftime('%d-%m-%Y'))
#     print(*random.sample(datas, 1))
#
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#
#         best_deal = 0
#         min_price = prices[0]
#         for i in range(1, len(prices)):
#             best_deal = max(best_deal, prices[i] - min_price)
#             min_price = min(min_price, prices[i])
#         return best_deal
#
#
# def is_prime(number: int) -> bool:
#     result = lambda number: number > 1 and all(
#         number % i != 0 for i in range(2, int(number ** 0.5) + 1))
#     return result(number)
#
#
# def longest_common_subsequence(s1, s2):
#     m = len(s1)
#     n = len(s2)
#
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#     lcs = ""
#     i, j = m, n
#     while i > 0 and j > 0:
#         if s1[i - 1] == s2[j - 1]:
#             lcs = s1[i - 1] + lcs
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1
#
#     return lcs


# function factorial(N) {
#     if (N === 0 || N === 1) {
#         return 1;
#     } else {
#         let result = 1;
#         for (let i = 2; i <= N; i++) {
#             result *= i;
#         }
#         return result;
#     }
# }


# def all_inclusive(string: str, lst: list) -> bool:
#     temp = []
#     string = list(string)
#     for __ in string:
#         first_part = string[-1::]
#         second_part = string[:-1:]
#         first_part.extend(second_part)
#         temp_result = ""
#         for _ in first_part:
#             temp_result += _
#         temp.append(temp_result)
#         string = list(temp_result)
#     for combination in temp:
#         if combination not in lst:
#             return False
#     return True
#
#
# string_test = "XjYABhR"
# list_test = [
#     "TzYxlgfnhf",
#     "yqVAuoLjMLy",
#     "BhRXjYA",
#     "YABhRXj",
#     "hRXjYAB",
#     "jYABhRX",
#     "XjYABhR",
#     "ABhRXjY",
# ]
# print(all_inclusive(string=string_test, lst=list_test))


# class Room:
#     def __init__(self, description):
#         self.description = description
#         self.doors = {}
#
#     def add_door(self, direction, room):
#         self.doors[direction] = room
#
#
# class Player:
#     def __init__(self, current_room):
#         self.current_room = current_room
#
#     def move(self, direction):
#         if direction in self.current_room.doors:
#             self.current_room = self.current_room.doors[direction]
#             print("You move to", self.current_room.description)
#         else:
#             print("There is no door in that direction!")
#
#
# def choose_word():
#     words = ['apple', 'banana', 'orange', 'grape', 'pineapple']
#     return random.choice(words)
#
#
# def longest_consecutive_subsequence(nums):
#     nums_set = set(nums)
#     longest_seq_length = 0
#     longest_seq_start = None
#
#     for num in nums_set:
#         if num - 1 not in nums_set:
#             current_num = num
#             current_seq_length = 1
#
#             while current_num + 1 in nums_set:
#                 current_num += 1
#                 current_seq_length += 1
#
#             if current_seq_length > longest_seq_length:
#                 longest_seq_length = current_seq_length
#                 longest_seq_start = num
#
#     longest_seq = [num for num in range(longest_seq_start,
#                                         longest_seq_start + longest_seq_length)]
#
#     return longest_seq, longest_seq_length
#
#
# def display_word(word, guessed_letters):
#     display = ''
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += '_'
#     return display
#
#
# def main():
#     word = choose_word()
#     guessed_letters = []
#     attempts = 6
#
#     print("Welcome to the Word Guessing Game!")
#     print("Try to guess the word one letter at a time.")
#
#     while True:
#         print("\nWord:", display_word(word, guessed_letters))
#         print("Attempts left:", attempts)
#         guess = input("Enter a letter: ").lower()
#
#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#         else:
#             guessed_letters.append(guess)
#             if guess not in word:
#                 attempts -= 1
#                 print("Incorrect guess!")
#                 if attempts == 0:
#                     print("You've run out of attempts. The word was:", word)
#                     break
#             else:
#                 print("Correct guess!")
#
#         if set(word) == set(guessed_letters):
#             print("Congratulations! You've guessed the word correctly:", word)
#             break
#
#
# def max_subarray_sum(nums: list[int]):
#     max_sum = float('-inf')
#     current_sum = 0
#
#     for num in nums:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#
#     return max_sum
#
#
# def get_reversed_color(hex_color: str) -> str:
#     if not isinstance(hex_color, str) or len(hex_color) > 6 or not all(
#             c in "0123456789ABCDEFabcdef" for c in hex_color):
#         raise ValueError("Invalid hex-color string")
#
#     hex_color = hex_color.upper().zfill(6)
#     reversed_color = "".join([hex(15 - int(c, 16))[2:] for c in hex_color])
#     return "#" + reversed_color.upper()
#
#

#
# print(CLASS_SPEC_VALID_COMBINATIONS["Druid"])
# function getPosition(text, word) {
#     return text.indexOf(word);
# }
# function
# countConsonants(input)
# {
# // const
# consonantsSet = new
# Set('bcdfghjklmnpqrstvwxyz');
# // let
# count = 0;
#
# // for (let i = 0; i < input.length; i++) {
#                                           // if (
#         consonantsSet.has(input[i].toLowerCase()) & & input[i].toLowerCase() !=
# = 'y') {
# // count++;
# //}
# //}
#
# //
# return count;
# //}
# function
# countLetters(input)
# {
#     const
# letterRegex = / [a - zA - Z] /;
# let
# count = 0;
#
# for (let i = 0; i < input.length; i++)
# {
# if (letterRegex.test(input[i]))
# {
#     count + +;
# }
# }
#
# return count;
# }
# function convertToLowerCase(input) {
#   return input.toLowerCase();
# }
# function calculateTaxes(income) {
#     if (income <= 1000) {
#         return income * 0.02;
#     } else if (income <= 10000) {
#         return income * 0.03;
#     } else {
#         return income * 0.05;
#     }
# }
#
# /**
#  * This comment gives you autocompletion
#  *
#  * @param {number[]} numbers
#  */
# function getSum(numbers) {
#   let sum = 0;
#
#   for (let i = 0; i < numbers.length; i++) {
#     sum += numbers[i];
#   }
#
#   return sum;
# }
#
# /**
#  * Returns the largest number from an array of numbers.
#  *
#  * @param {number[]} numbers - An array of numbers.
#  * @returns {number} The largest number.
#  */
# function getLargestNumber(numbers) {
#
#     return Math.max(...numbers);
# }

# function splitWords(text) {
#     // Using a regular expression to split the text into words
#     return text.match(/\w+/g) || [];
# }
# function joinWords(words, glue) {
#     return words.join(glue);
# }
# function checkWord(words, word) {
#     return words.includes(word);
# }
# function getFirstPosition(values, value) {
#   const index = values.indexOf(value);
#   return index !== -1 ? index : -1;
# }
# function sumArray(arr) {
#     let sum = 0;
#     for (let i = 0; i < arr.length; i++) {
#
#         if (typeof arr[i] === 'number' && !isNaN(arr[i])) {
#
#             if (arr[i] < 0) {
#                 sum -= arr[i];
#             } else {
#                 sum += arr[i];
#             }
#         }
#     }
#
#
#     return sum;
# }
#
# console.log(sumArray([1, 2, 3])); // Output: 6
# console.log(sumArray([-1, -2, -3])); // Output: 6
#

# def remove_duplicates(sorted_numbers: list) -> int:
#     print(sorted_numbers)
#     for num in sorted_numbers:
#         if sorted_numbers.count(num) > 1:
#             for _ in range(sorted_numbers.count(num) - 1):
#                 sorted_numbers.remove(num)
#     return len(sorted_numbers)


# function checkNumber(n) {
#     let results = [];
#     results.push(n > 0);
#     results.push(n % 2 === 0);
#     results.push(n % 10 === 0);
#     return results;
# }
#
# console.log(checkNumber(3));   // [true, false, false]
# console.log(checkNumber(10));  // [true, true, true]
# console.log(checkNumber(0));   // [false, true, true]
# console.log(checkNumber(-1));  // [false, false, false]


# function createArray(N) {
#   if (N === 0) {
#     return [];
#   } else {
#     return Array.from({ length: N }, (_, index) => index + 1);
#   }
# }


# function getArraysSum(arr1, arr2) {
#   let sum = 0;
#   for (let i = 0; i < arr1.length; i++) {
#     sum += arr1[i] + arr2[i];
#   }
#   return sum;
# }

# function
# combineArrays(first, second)
# {
#
# if (first.length !== second.length)
# {
#     throw
# new
# Error("Arrays must be of equal length");
# }
#
# const
# result = [];
#
# for (let i = 0; i < first.length; i++)
# {
#     result.push(first[i] + second[i]);
# }
#
# return result;
# }
#
# console.log(combineArrays([1, 2, 5], [3, 6, 1])); // [4, 8, 6]
# console.log(combineArrays([1], [6])); // [7]
# console.log(combineArrays([], [])); // []
# function doublePower(currentPowers) {
#   return currentPowers.map(power => power * 2);
# }


# function
# makeStickers(detailsCount, robotPart)
# {
#     const
# stickers = [];
#
# for (let i = 1; i <= detailsCount; i++)
# {
#     stickers.push(`${robotPart}
# detail  # ${i}`);
# }
#
# return stickers;www
# }

#
# function decryptMessage(message) {
#   const characters = message.split('');
#   const reversedCharacters = characters.reverse();
#   const decryptedMessage = reversedCharacters.join('');
#   return decryptedMessage;
# }

# function getDrinks(numberOfGuests) {
#   return numberOfGuests * (numberOfGuests + 1) / 2;
# }


# function isSorted(boxNumbers) {
#   for (let i = 0; i < boxNumbers.length - 1; i++) {
#     if (boxNumbers[i] > boxNumbers[i + 1]) {
#       return false;
#     }
#   }
#   return true;
# }
#
# function
# getLocation(coordinates, commands)
# {
#     let
# x = coordinates[0];
# let
# y = coordinates[1];
#
# for (let i = 0; i < commands.length; i++)
# {
#     switch(commands[i])
# {
#     case
# 'forward':
# y += 1;
# break;
# case
# 'back':
# y -= 1;
# break;
# case
# 'right':
# x += 1;
# break;
# case
# 'left':
# x -= 1;
# break;
# default:
# break;
# }
# }
#
# return [x, y];
# }


# /**
#  * This comment gives you autocompletion
#  *
#  * @param {string} doc
#  */
# function removeVowels(doc) {
#   return doc.replace(/[aeiouyAEIOUY]/g, '');
# }
# function compareRobots(firstRobotResults, secondRobotResults) {
#     const totalWeightFirstRobot = firstRobotResults.reduce((acc, curr) => acc + curr, 0);
#     const totalWeightSecondRobot = secondRobotResults.reduce((acc, curr) => acc + curr, 0);
#
#     if (totalWeightFirstRobot > totalWeightSecondRobot) {
#         return 'First robot for sale!';
#     } else if (totalWeightSecondRobot > totalWeightFirstRobot) {
#         return 'Second robot for sale!';
#     } else {
#         return 'Both robots for sale!';
#     }
# }


# function getDrinksWithStep(numberOfGuests, step) {
#   let sum = 0;
#
#   for (let i = 1; i <= numberOfGuests; i += step) {
#     sum += i;
#   }
#
#   return sum;
# }


# /**
#  * @param {Array} array
#  * @param {number} i
#  * @param {number} j
#  *
#  * @returns {void}
#  */
# function swapArray(array, i, j) {
#   if (i >= 0 && i < array.length && j >= 0 && j < array.length) {
#     [array[i], array[j]] = [array[j], array[i]];
#   }
#
#   return array;
# }

# python tests
# from datetime import time
#
# activity_time_start_filter = "15:00"
# activity_time_end_filter = "16:15"
# time_hour, time_minute = map(int, activity_time_start_filter.split(":"))
# rt_start = time(hour=time_hour, minute=time_minute)
#
# time_hour, time_minute = map(int, activity_time_end_filter.split(":"))
# rt_end = time(hour=time_hour, minute=time_minute)
# print(rt_start, "to", rt_end)
# # print(type(rt_start), type(rt_end))
# # print(type(Team.objects.first().activity_sessions.all().first().time_start))
# ###should be <class 'datetime.time'>
# print(rt_end - rt_start)


# /**
#  * @param {number[]} nums
#  * @param {number} n
#  *
#  * @returns {number[]}
#  */
# function shuffleArray(nums, n) {
#   const result = [];
#
#   for (let i = 0; i < n; i++) {
#     result.push(nums[i]);
#     result.push(nums[i + n]);
#   }
#
#   return result;
# }

def find_perimeter(grid: list) -> int:
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter


from datetime import time


def lft_time_module_testing(activity_time_start_filter: str,
                            activity_time_end_filter: str,
                            session_time_start: time,
                            session_time_end: time) -> bool:
    time_hour, time_minute = map(int, activity_time_start_filter.split(":"))
    user_activity_start = time(hour=time_hour, minute=time_minute)

    time_hour, time_minute = map(int, activity_time_end_filter.split(":"))
    user_activity_end = time(hour=time_hour, minute=time_minute)
    print("user: ", user_activity_start, "-", user_activity_end)
    print("session: ", session_time_start, "-", session_time_end)

    # common case
    if user_activity_start < user_activity_end:
        print("common case for user")
        query = (user_activity_start <= session_time_start and
                 session_time_end <= user_activity_end)

    # midnight case
    if user_activity_start > user_activity_end:
        print("user midnight case")
        query = (user_activity_start <= session_time_start and
                 session_time_end <= user_activity_end)

    print(query)


# lft_time_module_testing(
#     activity_time_start_filter="22:00",  # USER s
#     activity_time_end_filter="01:00",  # USER e
#     session_time_start=time(hour=22, minute=00),  # SESSION s
#     session_time_end=time(hour=00, minute=00)  # SESSION e
# )


from datetime import datetime, timedelta


def check_coverage(user_start, user_end, session_start, session_end):
    user_start = datetime.strptime(user_start, "%H:%M")
    user_end = datetime.strptime(user_end, "%H:%M")
    session_start = datetime.strptime(session_start, "%H:%M")
    session_end = datetime.strptime(session_end, "%H:%M")

    if user_end < user_start:
        user_end += timedelta(days=1)

    if session_end < session_start:
        session_end += timedelta(days=1)

    if user_start <= session_start and user_end >= session_end:
        return True
    else:
        return False


def activity_time_filter_queryset(queryset, activity_time_start_filter,
                                  activity_time_end_filter):
    user_start_time = datetime.strptime(activity_time_start_filter,
                                        '%H:%M').time()
    user_end_time = datetime.strptime(activity_time_end_filter, '%H:%M').time()

    user_delta = timedelta(
        hours=user_end_time.hour - user_start_time.hour,
        minutes=user_end_time.minute - user_start_time.minute
    )

    if user_end_time < user_start_time:
        user_delta += timedelta(days=1)

    queryset = queryset.filter(
        teams__activity_sessions__duration__gte=user_delta
    ).distinct()

    queryset = queryset.filter(
        teams__activity_sessions__time_start__lte=user_start_time,
        teams__activity_sessions__time_end__gte=user_end_time
    ).distinct()

    return queryset


def activity_time_filter_queryset(queryset,
                                  selected_days_filter,
                                  activity_time_start_filter,
                                  activity_time_end_filter):
    user_start_time = datetime.strptime(activity_time_start_filter,
                                        '%H:%M').time()
    user_end_time = datetime.strptime(activity_time_end_filter, '%H:%M').time()

    user_delta = timedelta(
        hours=user_end_time.hour - user_start_time.hour,
        minutes=user_end_time.minute - user_start_time.minute
    )

    if user_end_time < user_start_time:
        user_delta += timedelta(days=1)

    teams_queryset = Team.objects.filter(guild__in=queryset)

    if len(selected_days_filter) != 7:
        teams_queryset = teams_queryset.filter(
            activity_sessions__day__day_of_week__in=selected_days_filter
        ).distinct()

    teams_queryset = teams_queryset.filter(
        activity_sessions__duration__lte=user_delta
    ).distinct()

    approved_teams = []
    print("***********RESULT***************************")
    print("User input: ", user_start_time, user_end_time, user_delta)
    for team in teams_queryset:
        print("Team name: ", team)
        for session in team.activity_sessions.all():
            # print(
            #     session.day, session.time_start, "to", session.time_end,
            #     session.duration
            # )

            if user_start_time <= session.time_start:
                print(f"{user_start_time} <= {session.time_start}")
            if user_end_time >= session.time_end:
                print(f"{user_end_time} >= {session.time_end}")
    print("**************************************\n")

    queryset = Guild.objects.filter(teams__in=teams_queryset).distinct()

    return queryset


from datetime import datetime, timedelta

#
# from datetime import datetime

# user_start = datetime(1900, 1, 1, 23, 55, 0)
# user_end = datetime(1900, 1, 2, 00, 59, 0)
# team_start = datetime(1900, 1, 2, 00, 56, 0)
# team_end = datetime(1900, 1, 2, 00, 57, 0)

from datetime import datetime, timedelta


def func_final(user_start, user_end, team_start, team_end):
    user_start = datetime.strptime(user_start, '%H:%M')  # 1900-01-01 19:00:00
    user_end = datetime.strptime(user_end, '%H:%M')
    team_start = datetime.strptime(team_start, '%H:%M')
    team_end = datetime.strptime(team_end, '%H:%M')
    #######DELTA CHECK HERE)
    print("START: ", user_start, "-", user_end, "|",
          team_start, "-",
          team_end)

    ###### DELTA CHANGES #################
    if user_end < user_start:  # prep user
        user_end += timedelta(days=1)
        print("delta change user: ", user_start, "-", user_end)
    if team_end < team_start:  # prep team
        team_end += timedelta(days=1)

        print("delta change team: ", team_start, "-", team_end)

    if team_start < team_end:
        if team_start < user_start:
            if team_end < user_start:
                team_start += timedelta(days=1)
                team_end += timedelta(days=1)
    print(type(user_start), type(team_start))
    ######PERFECT CASE#################
    if user_start <= team_start <= team_end <= user_end:
        print("BEFORE TRUE RETURN: ", user_start, "-", user_end, "|",
              team_start, "-",
              team_end)
        return True
    print("BEFORE FALSE RETURN")
    print(user_start, user_end)
    print(team_start, team_end)

    return False


data = [

    ("21:00", "03:00", "19:00", "04:00"),  # IMP TESTING DATA
    ("21:00", "03:00", "21:00", "03:00"),
    ("21:00", "03:00", "22:00", "02:00"),
    ("21:00", "03:00", "22:00", "23:00"),
    ("21:00", "03:00", "23:00", "02:00"),
    ("21:00", "03:00", "01:00", "02:00"),
    ("21:00", "03:00", "19:00", "22:00"),
    ("21:00", "03:00", "02:00", "06:00"),
    ("21:00", "03:00", "18:00", "00:00"),
    ("21:00", "03:00", "00:00", "04:00")

]
counter = 1
for item in data:
    print("***************************************************")
    user_start, user_end, team_start, team_end = item
    print(
        f"{counter} case: {func_final(user_start, user_end, team_start, team_end)}")
    print("***************************************************")
    counter += 1


###########I OLD VER TO COMPARE ##########
def activity_time_filter_queryset(queryset,
                                  selected_days_filter,
                                  activity_time_start_filter,
                                  activity_time_end_filter):
    # 1900-01-01 19:00:00
    user_start = datetime.strptime(activity_time_start_filter,
                                   '%H:%M').replace(tzinfo=None)
    user_end = datetime.strptime(activity_time_end_filter, '%H:%M').replace(
        tzinfo=None)

    if user_end < user_start:  # prep user
        user_end += timedelta(days=1)
        print("delta change user: ", user_start, "-", user_end)

    user_delta = timedelta(
        hours=user_end.hour - user_start.hour,
        minutes=user_end.minute - user_start.minute
    )

    print(user_delta)
    queryset = queryset.filter(
        teams__activity_sessions__day__day_of_week__in=selected_days_filter
    ).distinct()

    queryset = queryset.filter(
        teams__activity_sessions__duration__lte=user_delta
    )

    team_queryset = Team.objects.filter(guild__in=queryset)
    filtered_team_queryset = Team.objects.none()

    record = len(team_queryset)
    for team in team_queryset:
        for session in team.activity_sessions.all():

            if session.time_end < session.time_start:  # prep team
                session.time_end += timedelta(days=1)

            if session.time_start < session.time_end:
                print(type(session.time_start), type(user_start))
                if session.time_start < user_start:
                    if session.time_end < user_start:
                        session.time_start += timedelta(days=1)
                        session.time_end += timedelta(days=1)

            if user_start <= session.time_start <= session.time_end <= user_end:
                filtered_team_queryset |= Team.objects.filter(id=team.id)

    print(filtered_team_queryset)
    # for team in filtered_team_queryset:
    #     for session in team.activity_sessions.all():
    #         print(session.time_start, session.time_end, session.day)
    # print(record, "to", len(filtered_team_queryset))
    return queryset


# copy DB type(session)
# check if tz aware
# check with tests (coverage later)!


# Example: Sending an email using smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email_username'
SMTP_PASSWORD = 'your_email_password'

# Compose email
message = MIMEMultipart()
message['From'] = 'sender@example.com'
message['To'] = 'recipient@example.com'
message['Subject'] = 'Automated Email'
message.attach(MIMEText('Hello, this is an automated email.', 'plain'))

# Send email
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.send_message(message)
    print("Email sent successfully!")


def palindromic_substring(string: str) -> str:
    def expand_center_odd(s: int, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def expand_center_even(s: int, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    for i in range(len(string)):
        odd_palindrome = expand_center_odd(string, i, i)
        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome

        even_palindrome = expand_center_even(string, i, i + 1)
        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome

    return longest_palindrome





####

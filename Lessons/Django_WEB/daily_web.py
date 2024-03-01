import math


def flatten_and_sort(lst: list) -> list:
    if len(lst):
        result = []
        for nested in lst:
            result += nested
        return sorted(result)
    return []


def is_isogram(string: str) -> bool:
    print(set(string))
    print(string)
    if len(set(string.lower())) == len(string.lower()):
        return True
    return False


def longest_substring(string: str) -> int:
    if len(string) == len(set(string)):
        return len(string)
    max_len = [0]
    temp_str = ""
    for i in string:
        if i not in temp_str:
            temp_str += i
        else:
            max_len.append(len(temp_str))
            temp_str = temp_str[temp_str.index(i) + 1:] + i
    return max(max_len)


def pluck(dicts: list, name: str) -> list:
    result = []
    for cur_dict in dicts:
        if name in cur_dict.keys():
            result.append(cur_dict[name])
        else:
            result.append(None)
    return result


def xo(string: str) -> bool:
    return True if string.lower().count("x") == string.lower().count(
        "o") else False


class PaginationHelper:
    content = []
    iter_index = 0

    def __init__(self, collection: list, items_per_page: int) -> None:
        self.collection = collection
        self.items_per_page = items_per_page

        for i in range(0, (len(self.collection) // items_per_page) + 1):
            self.content.append(
                self.collection[
                self.iter_index: self.iter_index + self.items_per_page:
                ]
            )
            self.iter_index += items_per_page

    def item_count(self) -> int:
        return len(self.collection)

    def page_count(self) -> int:
        if len(self.collection) == 0:
            return 0
        if self.items_per_page == 0:
            return 0
        result = len(self.collection) % self.items_per_page
        if result > 0:
            return (len(self.collection) // self.items_per_page) + 1
        return len(self.collection) // self.items_per_page

    def page_item_count(self, page_index: int) -> int:
        try:
            return len(self.content[page_index])
        except IndexError:
            return -1

    def page_index(self, item_index: int) -> int:
        if item_index < 0:
            return -1

        if len(self.collection) == 0:
            return -1
        try:
            for element in self.content:
                if self.collection[item_index] in element:
                    return self.content.index(element)
        except IndexError:
            return -1


helper = PaginationHelper(["a", "b", "c", "d", "e", "f"], 4)
helper.page_index(5)
helper.page_index(2)
helper.page_index(20)
helper.page_index(-10)


def find_children(santas_list: list, children: list) -> list:
    return sorted([kid for kid in children if kid in santas_list])


def triangle(row: str) -> str:
    if len(row) == 1:
        return row[0]

    colours = "RGB"
    all_rows = [row]
    next_row = ""

    while len(all_rows) < len(row):
        for iteration in range(1, len(all_rows[-1])):
            prev = row[iteration - 1]
            current = row[iteration]

            if prev == current:
                next_row += prev
            else:
                for colour in colours:
                    if colour not in prev + current:
                        next_row += colour

        all_rows.append(next_row)
        next_row = ""

    return all_rows[-1]


def compression(chars: list) -> str:
    if len(chars) == 1:
        return 1
    unique_and_order = []
    for i in chars:
        if i not in unique_and_order:
            unique_and_order.append(i)
    print(unique_and_order)
    result = ""
    for i in unique_and_order:
        if chars.count(i) == 1:
            result += i
        result += f"{i}{chars.count(i)}"
    print(result)
    return result


def sum_of_a_beach(beach: str) -> int:
    return sum(
        [beach.lower().count(i) for i in ("sand", "water", "fish", "sun")])


def valpa():
    result = ""
    for i in range(30):
        result += random.choice(
            [
                str(random.randint(1, 2)),
                str(random.randint(1, 2)),
                chr(random.randint(97, 122)).upper(),
                chr(random.randint(97, 122)).lower(),
            ]
        )
    return result


def longest_vowel_chain(string: str) -> int:
    if not len(string):
        return 0
    vowels = "aeiou"
    result = 0
    counter = 0
    for i in string:
        if i in vowels:
            counter += 1
        else:
            if result < counter:
                result = counter
            counter = 0

    return result


def shoot(results: list) -> str:
    p1_score = 0
    p2_score = 0
    multiplier = 0
    for every_try in results:
        # [{P1:'XX'', P2:'XO'}, True]
        multiplier = 2 if every_try[1] is True else 1
        p1_score += every_try[0]["P1"].count("X") * multiplier
        p2_score += every_try[0]["P2"].count("X") * multiplier
    if not p1_score == p2_score:
        if p1_score > p2_score:
            return "Pete Wins!"
        else:
            return "Phil Wins!"
    return "Draw!"


class MinStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return min(self.stack)


def find_unknown_number(first: int, second: int, third: int) -> int:
    for i in range(1, 200):
        if i % 3 == first:
            if i % 5 == second:
                if i % 7 == third:
                    return i


def discover_original_price(discounted_price: float,
                            sale_percentage: float) -> float:
    return round((discounted_price / (100 - sale_percentage)) * 100, 2)


def buy_tofu(cost: int, box: str) -> list or str:
    print(cost)
    print(box)
    box = box.split()
    result = [
        box.count("mon"),
        box.count("monme"),
        box.count("mon") + box.count("monme") * 60,
    ]
    min_amount = 0
    if result[1] > 0:
        for i in range(result[1]):
            if cost // 60:
                min_amount += 1
                cost -= 60
    if result[0] >= cost:
        min_amount += cost

    result.append(min_amount)
    if result[3] == 0:
        return "leaving the market"
    if cost % 60 > result[0]:
        return "leaving the market"
    return result


def is_valid_ip(ip_address: str) -> bool:
    ip_address = ip_address.split(".")
    if len(ip_address) != 4:
        return False
    for i in ip_address:
        try:
            int(i)
        except Exception:
            return False
        if " " in i:
            return False
        if int(i) < 0:
            return False
        if len(i) > 1:
            if int(i[0]) == 0:
                return False
        if not int(i) in range(255 + 1):
            return False
    return True


def trotter(number: int) -> int | str:
    if number == 0:
        return "INSOMNIA"

    digits_seen = set()
    i = 1

    while len(digits_seen) < 10:
        current_number = i * number
        digits_seen.update(set(str(current_number)))
        i += 1

    return current_number


def longest_common_prefix(strings_list: list) -> str:
    if not strings_list:
        return ""

    min_len = min(len(s) for s in strings_list)

    for i in range(min_len):
        char = strings_list[0][i]
        if not all(s[i] == char for s in strings_list):
            return strings_list[0][:i]

    return strings_list[0][:min_len]


def scramble(first_string: str, second_string: str) -> bool:
    print(first_string)
    print(second_string)
    for i in second_string:
        if i in first_string:
            if not first_string.count(i) >= second_string.count(i):
                return False
        else:
            return False
    return True


def credit_card_mask(card_number: str) -> str:
    return f"{'#' * len(card_number[:-4:])}{card_number[-4::]}"


def is_solved(board: list) -> int:
    param = 3
    for i in range(3):
        param -= 1
        if board[0][i] == board[1][1] == board[2][param]:
            if board[0][i] != 0:
                if board[0][i] == 1:
                    return 1
                return 2

        if len(set(board[i])) == 1:
            if board[i][0] != 0:
                if board[i][0] == 1:
                    return 1
                return 2

    for row in board:
        if 0 in row:
            return -1
    return 0


def is_happy(number):
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    slow = number
    fast = get_next(number)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1


# flake8: noqa E501


# "{'1-800-HOLY-COT', '1-800-INK-WANT', '1-800-HOLY-ANT'}"


def make_readable(seconds: int) -> str:
    if seconds > 359999:
        return ""
    result = ""
    hours, minutes = 0, 0
    while seconds >= 3600:
        hours += 1
        seconds -= 3600
    while seconds >= 60:
        minutes += 1
        seconds -= 60

    result = f"0{hours}:" if len(str(hours)) == 1 else f"{hours}:"
    if minutes < 10:
        result += f"0{minutes}:"
    else:
        result += str(minutes)
        result += ":"

    if seconds < 10:
        result += f"0{seconds}"
    else:
        result += str(seconds)
    print(result)
    return result


def pendulum(lst: list) -> list:
    left = []
    mid = []
    right = []
    counter = 0
    print(sorted(lst, reverse=True))
    for i in sorted(lst, reverse=True):
        print(i)
        if counter % 2 == 0:
            left.append(i)
        else:
            right.append(i)
        counter += 1
    print(left + mid + right[::-1])
    return left + mid + right[::-1]


def tv_remote(word: str) -> int:
    all_rows = [
        ["a", "b", "c", "d", "e", "1", "2", "3"],
        ["f", "g", "h", "i", "j", "4", "5", "6"],
        ["k", "l", "m", "n", "o", "7", "8", "9"],
        ["p", "q", "r", "s", "t", ".", "@", "0"],
        ["u", "v", "w", "x", "y", "z", "_", "/"],
    ]
    steps = 0
    current_position = [0, 0]  # Починаємо з літери "a"

    for letter in word:
        for i, row in enumerate(all_rows):
            if letter in row:
                letter_index = row.index(letter)
                steps += (
                        abs(current_position[0] - i)
                        + abs(current_position[1] - letter_index)
                        + 1
                )  # +1 за крок OK
                current_position = [i, letter_index]
                break

    return steps


# flake8: noqa E501

WORDS = [
    "ACT",
    "ADD",
    "ALL",
    "APE",
    "AND",
    "ANN",
    "ANY",
    "ANT",
    "ARE",
    "ART",
    "ASS",
    "BAD",
    "BAR",
    "BAT",
    "BAY",
    "BEE",
    "BIG",
    "BIT",
    "BOB",
    "BOY",
    "BUN",
    "BUT",
    "CAN",
    "CAR",
    "CAT",
    "COT",
    "COW",
    "CUT",
    "DAD",
    "DAY",
    "DEW",
    "DID",
    "DIN",
    "DOG",
    "DON",
    "DOT",
    "DUD",
    "EAR",
    "EAT",
    "EEL",
    "EGG",
    "ERR",
    "EYE",
    "FAG",
    "FAR",
    "FLY",
    "FOR",
    "FUN",
    "FUR",
    "GAY",
    "GET",
    "GOT",
    "GUM",
    "GUN",
    "GUY",
    "GUT",
    "GYM",
    "HAS",
    "HAT",
    "HER",
    "HEY",
    "HIM",
    "HIS",
    "HIT",
    "HOW",
    "HUG",
    "HUN",
    "ICE",
    "INK",
    "ITS",
    "IVE",
    "JAN",
    "JET",
    "JOB",
    "JOT",
    "JOY",
    "KEY",
    "LAP",
    "LAY",
    "LIE",
    "LET",
    "LOG",
    "MAN",
    "MAP",
    "MAY",
    "MEN",
    "MOM",
    "MUD",
    "MUM",
    "NAP",
    "NEW",
    "NOD",
    "NOT",
    "NOW",
    "OAR",
    "ODD",
    "OFF",
    "OLD",
    "ONE",
    "OUR",
    "OUT",
    "PAN",
    "PAL",
    "PAT",
    "PAW",
    "PEN",
    "PET",
    "PIG",
    "PIT",
    "POT",
    "PRO",
    "PUT",
    "QUO",
    "RAG",
    "RAM",
    "RAN",
    "RAP",
    "RAT",
    "RED",
    "RIP",
    "ROD",
    "ROT",
    "RUN",
    "RUT",
    "SAT",
    "SAW",
    "SAY",
    "SEA",
    "SEE",
    "SEX",
    "SHE",
    "SOY",
    "SUN",
    "SUX",
    "TAN",
    "TAT",
    "TEA",
    "THE",
    "TIN",
    "TIP",
    "TIT",
    "TON",
    "TOP",
    "TOO",
    "TWO",
    "URN",
    "USE",
    "VAN",
    "VET",
    "VIP",
    "WAR",
    "WAS",
    "WAY",
    "WED",
    "WHO",
    "WHY",
    "WIN",
    "WON",
    "XXX",
    "YAK",
    "YAM",
    "YAP",
    "YOU",
    "YUM",
    "ZAP",
    "ZIP",
    "ZIT",
    "ZOO",
    "ABLE",
    "ACED",
    "AGOG",
    "AHEM",
    "AHOY",
    "ALLY",
    "AMEN",
    "ANTI",
    "ANTS",
    "ANUS",
    "APES",
    "ARMY",
    "ARSE",
    "ARTY",
    "AVID",
    "AWED",
    "BABY",
    "BARS",
    "BATS",
    "BAYS",
    "BEAR",
    "BEES",
    "BILL",
    "BITE",
    "BITS",
    "BLOW",
    "BLUE",
    "BOLD",
    "BONE",
    "BOOB",
    "BOOM",
    "BOSS",
    "BOYS",
    "BUFF",
    "BUNG",
    "BUNS",
    "BUMS",
    "BURP",
    "BUST",
    "BUSY",
    "BUZZ",
    "CANS",
    "CANT",
    "CARS",
    "CART",
    "CATS",
    "CHAP",
    "CHIC",
    "CHUM",
    "CIAO",
    "CLAP",
    "COCK",
    "CODE",
    "COOL",
    "COWS",
    "COZY",
    "CRAB",
    "CREW",
    "CURE",
    "CULT",
    "DADS",
    "DAFT",
    "DAWN",
    "DAYS",
    "DECK",
    "DEED",
    "DICK",
    "DING",
    "DOGS",
    "DOTS",
    "DOLL",
    "DOLT",
    "DONG",
    "DOPE",
    "DOWN",
    "DRAW",
    "DUCK",
    "DUDE",
    "DUMB",
    "DUTY",
    "EARL",
    "EARN",
    "EARS",
    "EASY",
    "EATS",
    "EDGE",
    "EELS",
    "EGGS",
    "ENVY",
    "EPIC",
    "EYES",
    "FACE",
    "FAGS",
    "FANG",
    "FARM",
    "FART",
    "FANS",
    "FAST",
    "FEAT",
    "FEET",
    "FISH",
    "FIVE",
    "FIZZ",
    "FLAG",
    "FLEW",
    "FLIP",
    "FLOW",
    "FOOD",
    "FORT",
    "FUCK",
    "FUND",
    "GAIN",
    "GEEK",
    "GEMS",
    "GIFT",
    "GIRL",
    "GIST",
    "GIVE",
    "GLEE",
    "GLOW",
    "GOLD",
    "GOOD",
    "GOSH",
    "GRAB",
    "GRIN",
    "GRIT",
    "GROT",
    "GROW",
    "GRUB",
    "GUNS",
    "GUSH",
    "GYMS",
    "HAIL",
    "HAIR",
    "HALO",
    "HANG",
    "HATS",
    "HEAD",
    "HEAL",
    "HEIR",
    "HELL",
    "HELP",
    "HERE",
    "HERO",
    "HERS",
    "HIGH",
    "HIRE",
    "HITS",
    "HOLY",
    "HOPE",
    "HOST",
    "HUNK",
    "HUGE",
    "HUNG",
    "HUNS",
    "HURT",
    "ICON",
    "IDEA",
    "IDLE",
    "IDOL",
    "IOTA",
    "JAZZ",
    "JERK",
    "JESS",
    "JETS",
    "JINX",
    "JOBS",
    "JOHN",
    "JOKE",
    "JUMP",
    "JUNE",
    "JULY",
    "JUNK",
    "JUST",
    "KATA",
    "KEYS",
    "KICK",
    "KIND",
    "KING",
    "KISS",
    "KONG",
    "KNOB",
    "KNOW",
    "LARK",
    "LATE",
    "LEAN",
    "LICE",
    "LICK",
    "LIKE",
    "LION",
    "LIVE",
    "LOGS",
    "LOCK",
    "LONG",
    "LOOK",
    "LORD",
    "LOVE",
    "LUCK",
    "LUSH",
    "MAKE",
    "MANY",
    "MART",
    "MATE",
    "MAXI",
    "MEEK",
    "MIKE",
    "MILD",
    "MINT",
    "MMMM",
    "MOMS",
    "MOOD",
    "MOON",
    "MOOT",
    "MUCH",
    "MUFF",
    "MUMS",
    "MUTT",
    "NAPS",
    "NAZI",
    "NEAT",
    "NECK",
    "NEED",
    "NEWS",
    "NEXT",
    "NICE",
    "NICK",
    "NOON",
    "NOSE",
    "NOTE",
    "OARS",
    "OATS",
    "ONCE",
    "ONLY",
    "OPEN",
    "ORGY",
    "OVAL",
    "OVER",
    "PANS",
    "PALS",
    "PART",
    "PAST",
    "PATS",
    "PAWS",
    "PEAR",
    "PERT",
    "PENS",
    "PETS",
    "PHEW",
    "PIPE",
    "PIPS",
    "PLAN",
    "PLUM",
    "PLUS",
    "POET",
    "POOF",
    "POOP",
    "POSH",
    "POTS",
    "PROS",
    "PSST",
    "PUKE",
    "PUNK",
    "PURE",
    "PUSH",
    "PUSS",
    "QUAD",
    "QUAK",
    "QUID",
    "QUIT",
    "RANT",
    "RAPE",
    "RAPS",
    "RAPT",
    "RATE",
    "RAMS",
    "RATS",
    "REAP",
    "RICK",
    "RING",
    "RIPE",
    "ROOT",
    "ROSE",
    "ROSY",
    "ROTS",
    "RUNT",
    "RUTS",
    "SAFE",
    "SAGE",
    "SANE",
    "SAVE",
    "SAWS",
    "SEEK",
    "SEXY",
    "SHAG",
    "SHIT",
    "SICK",
    "SIGH",
    "SIRE",
    "SLAG",
    "SLIT",
    "SLUT",
    "SNAP",
    "SNOG",
    "SNUG",
    "SOFT",
    "SOON",
    "SOUL",
    "SOUP",
    "SPRY",
    "STIR",
    "STUN",
    "SUCK",
    "SWAG",
    "SWAY",
    "TACT",
    "TANK",
    "TANS",
    "THAT",
    "THIS",
    "TIME",
    "TINS",
    "TINY",
    "TITS",
    "TOES",
    "TONS",
    "TONY",
    "TOPS",
    "TOYS",
    "UBER",
    "URNS",
    "USED",
    "USER",
    "USES",
    "VAIN",
    "VAMP",
    "VARY",
    "VEIN",
    "VENT",
    "VERY",
    "VEST",
    "VIEW",
    "VIVA",
    "VOLT",
    "VOTE",
    "WAFT",
    "WAGE",
    "WAKE",
    "WALK",
    "WALL",
    "WANG",
    "WANK",
    "WANT",
    "WARD",
    "WARM",
    "WARP",
    "WARS",
    "WART",
    "WASH",
    "WAVE",
    "WEAR",
    "WEDS",
    "WEED",
    "WEEN",
    "WELD",
    "WHAT",
    "WHEE",
    "WHEW",
    "WHIP",
    "WHIZ",
    "WHOA",
    "WIFE",
    "WILL",
    "WIND",
    "WING",
    "WINK",
    "WINS",
    "WIRE",
    "WISH",
    "WITH",
    "WORD",
    "WORK",
    "WRAP",
    "XMAN",
    "XMEN",
    "XRAY",
    "XTRA",
    "XXXX",
    "YANK",
    "YAKS",
    "YAMS",
    "YAPS",
    "YARD",
    "YARN",
    "YELP",
    "YERN",
    "YOKE",
    "YOLK",
    "YULE",
    "ZANY",
    "ZAPS",
    "ZIPS",
    "ZITS",
    "ZERO",
    "ZOOM",
    "ZOOS",
]


def check_1800(string: str) -> set:
    panel = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
    }
    codes = {str(i): [] for i in range(10_000)}
    for word in WORDS:
        code = ""
        for letter in word:
            for number in panel:
                if letter in panel[number]:
                    code += number
        codes[code].append(word)
    cleared = {k: codes[k] for k in codes.keys() if len(codes[k])}
    del codes
    code_from_string = ""
    for word in string.split("-")[2::]:
        for letter in word:
            for button in panel:
                if letter in panel[button]:
                    code_from_string += button
    codes_to_process = [
        [code_from_string[:4:], code_from_string[4::]],
        [code_from_string[:3:], code_from_string[3::]],
    ]
    result = []

    for code_pair in codes_to_process:
        code1, code2 = code_pair
        words1 = cleared.get(code1, [])
        words2 = cleared.get(code2, [])
        combinations = [(word1, word2) for word1 in words1 for word2 in words2]
        for combination in combinations:
            result.append(f"1-800-{combination[0]}-{combination[1]}")

    return set(result)


check_1800("1-800-CODE-WAR")


# "{'1-800-INK-WANT', '1-800-HOLY-ANT', '1-800-HOLY-COT'}"


def duplicate_arguments(*args) -> bool:
    if len(args) == len(set(args)):
        return False
    else:
        return True


def str_in_str(haystack: str, needle: str) -> int:
    if not len(needle):
        return 0
    try:
        return haystack.index(needle)
    except Exception:
        return -1


def count_ones(left: int, right: int) -> int:
    return sum(bin(i).count("1") for i in range(left, right + 1))


def coupon_code(
        entered_code: str,
        correct_code: str,
        current_date: str,
        expiration_date: str,
) -> bool:
    from datetime import datetime

    if entered_code == correct_code:
        return datetime.strptime(expiration_date,
                                 "%B %d, %Y") >= datetime.strptime(
            current_date, "%B %d, %Y"
        )
    return False


coupon_code(
    entered_code="123",
    correct_code="123",
    current_date="July 9, 2015",
    expiration_date="July 9, 2015",
)


def count_and_say(number: int) -> str:
    if number == 1:
        return "1"

    result = "1"

    for _ in range(number - 1):
        current_char = result[0]
        count = 1
        new_result = ""

        for i in range(1, len(result)):
            if result[i] == current_char:
                count += 1
            else:
                new_result += str(count) + current_char
                current_char = result[i]
                count = 1

        new_result += str(count) + current_char
        result = new_result

    return result


def one_down(txt: str) -> str:
    if not isinstance(txt, str):
        return "Input is not a string"
    result = ""
    for letter in txt:
        if ord(letter) == 32:
            result += " "
        else:
            if letter == "A":
                result += "Z"
                continue
            if letter == "a":
                result += "z"
                continue
            else:
                result += chr(ord(letter) - 1)
    return result


one_down("Ifmmp")


def timer(func):
    def wrapper(*args, **kwargs):
        import datetime

        start = datetime.datetime.now()
        func(*args)

        print(
            f"Function {func.__name__} execution takes {datetime.datetime.now() - start} s."
        )

    return wrapper


@timer
def some_func(x: int, y: int) -> int:
    result = 0
    for i in range(10):
        result += x - y ** 2
    print(result)
    return result


def middle_character(word: str) -> str:
    if not (len(word)):
        return ""
    lenw = len(word)
    if lenw == 2:
        return word
    if lenw == 1:
        return word
    if lenw % 2 == 0:
        return word[int(lenw / 2) - 1] + word[int(lenw / 2)]
    return word[int(lenw / 2 - 0.5)]


def roman_to_int(roman: str) -> int:
    result = 0
    data = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    prev_value = 0

    for numeral in reversed(roman):
        current_value = data[numeral]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value

    return result


def find_number(start: int, stop: int, string: str) -> list:
    result = []
    data_list = [data for data in range(start, stop + 1)]
    print(string)
    for number in data_list:
        if str(number) in string:
            print(string)
            string = string.replace(str(number), ".")
            print(string)
        else:
            result.append(number)
    if not len(result):
        return []
    return result


def multiples_3_5(number: int) -> int:
    if number < 3:
        return 0
    data = []
    for i in range(3, number):
        flag_3 = i % 3 == 0
        flag_5 = i % 5 == 0
        if flag_3 or flag_5:
            data.append(i)
    print(data)
    return sum(data)


import itertools as it


def equal_to_24(*cards) -> str:
    for template in ["aZ(bX(cVd))", "(aZb)X(cVd)", "((aZb)Xc)Vd"]:
        for card in it.permutations(cards):
            for prod in it.product("*/+-", repeat=3):
                temp = template
                for char in (
                        ("Z", prod[0]),
                        ("X", prod[1]),
                        ("V", prod[2]),
                        ("a", str(card[0])),
                        ("b", str(card[1])),
                        ("c", str(card[2])),
                        ("d", str(card[3])),
                ):
                    temp = temp.replace(*char)
                try:
                    if eval(temp) == 24:
                        return temp
                except ZeroDivisionError:
                    pass
    return "It's not possible!"


def credit_card_issuer_checking(number: int) -> str:
    if len(str(number)) == 15:
        amex_start = ["34", "37"]
        if str(number)[:2:] in amex_start:
            return "AMEX"
    visa_lens = [13, 16]
    if len(str(number)) in visa_lens:
        if str(number)[:1:] == "4":
            return "VISA"
        if str(number)[:4:] == "6011":
            return "Discover"
        mastercard_start = ["51", "52", "53", "54", "55"]
        if str(number)[:2:] in mastercard_start:
            return "Mastercard"

    return "Unknown"


def perfect_number(number: int) -> bool:
    if number <= 1:
        return False

    result = 1

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            result += i
            complement = number // i
            if i != complement:
                result += complement

    return result == number


def highest_and_lowest(string_of_nums: str) -> str:
    try:
        data_list = string_of_nums.split(sep=" ")
        return f"{max(data_list)} {min(data_list)}"
    except Exception:
        return ""


# @pytest.mark.parametrize(
#     "string_of_nums, max_min_string",
#     [
#         ("-100", "-100 -100"),
#         ("-1", "-1 -1"),
#         ("0", "0 0"),
#         ("1", "1 1"),
#         ("-1 0 1", "1 -1"),
#         ("1 2 3 4", "4 1"),
#         ("4 3 2 1", "4 1"),
#         ("1 2 3 4 5", "5 1"),
#         ("1 2 -3 4 5", "5 -3"),
#         ("1 9 3 4 -5", "9 -5"),
#         ("0 0 0 0 0", "0 0"),
#         ("-1 0 1 0", "1 -1"),
#         ("10 8 90 -7", "90 -7"),
#         ("-100 100", "100 -100"),
#         ("-10000000 0", "0 -10000000"),
#         ("-123456789 -1234567810", "-123456789 -1234567810"),
#     ],
# )
def test_highest_and_lowest(string_of_nums, max_min_string):
    assert highest_and_lowest(string_of_nums) == max_min_string, (
        f"Function 'highest_and_lowest' should return '{max_min_string}' "
        f"when string is '{string_of_nums}'"
    )


def pascal_triangle_row(row_index: int) -> list:
    def calculate_combination(n: int, k: int) -> int:
        result = 1
        for i in range(1, k + 1):
            result *= n - i + 1
            result //= i
        return result

    row = []
    for k in range(row_index + 1):
        row.append(calculate_combination(row_index, k))
    return row


def calculate_profit(**kwargs) -> int:
    if 0 in kwargs:
        return 0
    old = amount
    for year in range(period):
        amount *= 1 + (percent / 100)
        print(amount)
    return amount - old


from collections import Counter


def find_number(start: int, stop: int, string: str) -> list:
    code = Counter(
        char for number in range(start, stop + 1) for char in str(number)
    ) - Counter(string)
    return [number for number in range(start, stop + 1) if
            Counter(str(number)) == code]


def get_plan(cur, month, perc):
    result = []
    for i in range(month):
        result.append(math.floor(cur / 100 * (100 + perc)))
        cur = result[-1]
    return result


def reverse_random_string(random_string: str, amount_of_symbols: int) -> str:
    if len(random_string) < amount_of_symbols:
        return random_string[::-1]
    elif len(random_string) < 2 * amount_of_symbols:
        fp = random_string[amount_of_symbols - 1:: -1]
        sp = random_string[amount_of_symbols:]
        return fp + sp
    else:
        result = ""
        aos = amount_of_symbols
        for i in range(0, len(random_string), 2 * amount_of_symbols):
            result += random_string[i: i + aos][::-1]
            result += random_string[i + aos: i + 2 * aos]
        return result


def snail(matrix: list) -> list:
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


def next_smaller(number: int) -> int:
    digits = list(str(number))
    i = len(digits) - 2
    while i >= 0 and digits[i] <= digits[i + 1]:
        i -= 1
    if i == -1:
        return -1
    j = len(digits) - 1
    while digits[j] >= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    result = int("".join(digits))
    return result


def intersection_of_two(nums1: list, nums2: list) -> list:
    data = list(set(nums1)) + list(set(nums2))
    data_dict = {key: data.count(key) for key in data}
    result = [num for num in data_dict if data_dict[num] == 2]
    result.sort()
    return result


def performant_smallest(nums: list, n: int) -> list:
    condition = nums.copy()
    condition.sort()
    condition = condition[:n:]
    result = []
    for num in nums:
        if num in condition:
            result.append(num)
            condition.remove(num)
    print(result)
    return result


def performant_smallest(nums: list, n: int) -> list:
    if n == len(nums):
        return nums
    try:
        target = (list(set(nums))[n:n + 1:])[0]
    except Exception:
        target = sorted(nums)[-1]

    result = []
    for i in nums:
        if i < target:
            result.append(i)
            if len(result) == n:
                break
    return result


def climb_stairs(number: int) -> int:
    if number <= 2:
        return number
    first, second = 1, 2
    for _ in range(3, number + 1):
        third = first + second
        first, second = second, third
    return second


def choose_best_sum(limit: int, number_of_towns: int,
                    list_of_distances: list) -> int:
    from itertools import combinations
    best_sum = None
    for towns in combinations(list_of_distances, number_of_towns):
        current_sum = sum(towns)
        if current_sum <= limit:
            if best_sum is None or current_sum > best_sum:
                best_sum = current_sum
    return best_sum


# Write a Python program to find the kth smallest element in a given binary search tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kth_smallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.val


root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):

      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data


   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()



class BstNode:
    import random

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2




b = BstNode(50)
for _ in range(50):
    b.insert(random.randint(0, 100))
b.display()




def date_generated(d1, d2):
    import datetime
    import random
    start = datetime.datetime.strptime(d1, '%d-%m-%Y')
    end = datetime.datetime.strptime(d2, '%d-%m-%Y')
    intervalo = [start + datetime.timedelta(x) for x in range(int ((end-start).days)+1)]
    datas = []
    for data in intervalo:
        datas.append(data.strftime('%d-%m-%Y'))
    print(*random.sample(datas, 1))

date_generated('03-12-2021','03-01-2022')


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        best_deal = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            best_deal = max(best_deal, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return best_deal

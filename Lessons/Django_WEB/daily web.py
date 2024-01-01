import random


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
    return True if string.lower().count("x") == string.lower().count("o") \
        else False


class PaginationHelper:
    content = []
    iter_index = 0

    def __init__(self, collection: list, items_per_page: int) -> None:
        self.collection = collection
        self.items_per_page = items_per_page

        for i in range(0, (len(self.collection) // items_per_page) + 1):
            self.content.append(
                self.collection[self.iter_index:
                                self.iter_index + self.items_per_page:]
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


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
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
    return sum([beach.lower().count(i) for i in ("sand", "water", "fish", "sun")])


def valpa():
    result = ""
    for i in range(30):
        result += random.choice(
            [
                str(random.randint(1, 2)),
                str(random.randint(1, 2)),
                chr(random.randint(97, 122)).upper(),
                chr(random.randint(97, 122)).lower()]
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


def discover_original_price(
        discounted_price: float, sale_percentage: float
) -> float:
    return round((discounted_price / (100 - sale_percentage)) * 100, 2)


def buy_tofu(cost: int, box: str) -> list or str:
    print(cost)
    print(box)
    box = box.split()
    result = [box.count("mon"),
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


# flake8: noqa E501
WORDS = ["ACT", "ADD", "ALL", "APE", "AND", "ANN", "ANY", "ANT", "ARE", "ART", "ASS", "BAD", "BAR", "BAT", "BAY", "BEE", "BIG", "BIT", "BOB", "BOY", "BUN",
         "BUT", "CAN", "CAR", "CAT", "COT", "COW", "CUT", "DAD", "DAY", "DEW", "DID", "DIN", "DOG", "DON", "DOT", "DUD", "EAR", "EAT", "EEL", "EGG", "ERR",
         "EYE", "FAG", "FAR", "FLY", "FOR", "FUN", "FUR", "GAY", "GET", "GOT", "GUM", "GUN", "GUY", "GUT", "GYM", "HAS", "HAT", "HER", "HEY", "HIM", "HIS",
         "HIT", "HOW", "HUG", "HUN", "ICE", "INK", "ITS", "IVE", "JAN", "JET", "JOB", "JOT", "JOY", "KEY", "LAP", "LAY", "LIE", "LET", "LOG", "MAN", "MAP",
         "MAY", "MEN", "MOM", "MUD", "MUM", "NAP", "NEW", "NOD", "NOT", "NOW", "OAR", "ODD", "OFF", "OLD", "ONE", "OUR", "OUT", "PAN", "PAL", "PAT", "PAW",
         "PEN", "PET", "PIG", "PIT", "POT", "PRO", "PUT", "QUO", "RAG", "RAM", "RAN", "RAP", "RAT", "RED", "RIP", "ROD", "ROT", "RUN", "RUT", "SAT", "SAW",
         "SAY", "SEA", "SEE", "SEX", "SHE", "SOY", "SUN", "SUX", "TAN", "TAT", "TEA", "THE", "TIN", "TIP", "TIT", "TON", "TOP", "TOO", "TWO", "URN", "USE",
         "VAN", "VET", "VIP", "WAR", "WAS", "WAY", "WED", "WHO", "WHY", "WIN", "WON", "XXX", "YAK", "YAM", "YAP", "YOU", "YUM", "ZAP", "ZIP", "ZIT", "ZOO",
         "ABLE", "ACED", "AGOG", "AHEM", "AHOY", "ALLY", "AMEN", "ANTI", "ANTS", "ANUS", "APES", "ARMY", "ARSE", "ARTY", "AVID", "AWED", "BABY", "BARS",
         "BATS", "BAYS", "BEAR", "BEES", "BILL", "BITE", "BITS", "BLOW", "BLUE", "BOLD", "BONE", "BOOB", "BOOM", "BOSS", "BOYS", "BUFF", "BUNG", "BUNS",
         "BUMS", "BURP", "BUST", "BUSY", "BUZZ", "CANS", "CANT", "CARS", "CART", "CATS", "CHAP", "CHIC", "CHUM", "CIAO", "CLAP", "COCK", "CODE", "COOL",
         "COWS", "COZY", "CRAB", "CREW", "CURE", "CULT", "DADS", "DAFT", "DAWN", "DAYS", "DECK", "DEED", "DICK", "DING", "DOGS", "DOTS", "DOLL", "DOLT",
         "DONG", "DOPE", "DOWN", "DRAW", "DUCK", "DUDE", "DUMB", "DUTY", "EARL", "EARN", "EARS", "EASY", "EATS", "EDGE", "EELS", "EGGS", "ENVY", "EPIC",
         "EYES", "FACE", "FAGS", "FANG", "FARM", "FART", "FANS", "FAST", "FEAT", "FEET", "FISH", "FIVE", "FIZZ", "FLAG", "FLEW", "FLIP", "FLOW", "FOOD",
         "FORT", "FUCK", "FUND", "GAIN", "GEEK", "GEMS", "GIFT", "GIRL", "GIST", "GIVE", "GLEE", "GLOW", "GOLD", "GOOD", "GOSH", "GRAB", "GRIN", "GRIT",
         "GROT", "GROW", "GRUB", "GUNS", "GUSH", "GYMS", "HAIL", "HAIR", "HALO", "HANG", "HATS", "HEAD", "HEAL", "HEIR", "HELL", "HELP", "HERE", "HERO",
         "HERS", "HIGH", "HIRE", "HITS", "HOLY", "HOPE", "HOST", "HUNK", "HUGE", "HUNG", "HUNS", "HURT", "ICON", "IDEA", "IDLE", "IDOL", "IOTA", "JAZZ",
         "JERK", "JESS", "JETS", "JINX", "JOBS", "JOHN", "JOKE", "JUMP", "JUNE", "JULY", "JUNK", "JUST", "KATA", "KEYS", "KICK", "KIND", "KING", "KISS",
         "KONG", "KNOB", "KNOW", "LARK", "LATE", "LEAN", "LICE", "LICK", "LIKE", "LION", "LIVE", "LOGS", "LOCK", "LONG", "LOOK", "LORD", "LOVE", "LUCK",
         "LUSH", "MAKE", "MANY", "MART", "MATE", "MAXI", "MEEK", "MIKE", "MILD", "MINT", "MMMM", "MOMS", "MOOD", "MOON", "MOOT", "MUCH", "MUFF", "MUMS",
         "MUTT", "NAPS", "NAZI", "NEAT", "NECK", "NEED", "NEWS", "NEXT", "NICE", "NICK", "NOON", "NOSE", "NOTE", "OARS", "OATS", "ONCE", "ONLY", "OPEN",
         "ORGY", "OVAL", "OVER", "PANS", "PALS", "PART", "PAST", "PATS", "PAWS", "PEAR", "PERT", "PENS", "PETS", "PHEW", "PIPE", "PIPS", "PLAN", "PLUM",
         "PLUS", "POET", "POOF", "POOP", "POSH", "POTS", "PROS", "PSST", "PUKE", "PUNK", "PURE", "PUSH", "PUSS", "QUAD", "QUAK", "QUID", "QUIT", "RANT",
         "RAPE", "RAPS", "RAPT", "RATE", "RAMS", "RATS", "REAP", "RICK", "RING", "RIPE", "ROOT", "ROSE", "ROSY", "ROTS", "RUNT", "RUTS", "SAFE", "SAGE",
         "SANE", "SAVE", "SAWS", "SEEK", "SEXY", "SHAG", "SHIT", "SICK", "SIGH", "SIRE", "SLAG", "SLIT", "SLUT", "SNAP", "SNOG", "SNUG", "SOFT", "SOON",
         "SOUL", "SOUP", "SPRY", "STIR", "STUN", "SUCK", "SWAG", "SWAY", "TACT", "TANK", "TANS", "THAT", "THIS", "TIME", "TINS", "TINY", "TITS", "TOES",
         "TONS", "TONY", "TOPS", "TOYS", "UBER", "URNS", "USED", "USER", "USES", "VAIN", "VAMP", "VARY", "VEIN", "VENT", "VERY", "VEST", "VIEW", "VIVA",
         "VOLT", "VOTE", "WAFT", "WAGE", "WAKE", "WALK", "WALL", "WANG", "WANK", "WANT", "WARD", "WARM", "WARP", "WARS", "WART", "WASH", "WAVE", "WEAR",
         "WEDS", "WEED", "WEEN", "WELD", "WHAT", "WHEE", "WHEW", "WHIP", "WHIZ", "WHOA", "WIFE", "WILL", "WIND", "WING", "WINK", "WINS", "WIRE", "WISH",
         "WITH", "WORD", "WORK", "WRAP", "XMAN", "XMEN", "XRAY", "XTRA", "XXXX", "YANK", "YAKS", "YAMS", "YAPS", "YARD", "YARN", "YELP", "YERN", "YOKE",
         "YOLK", "YULE", "ZANY", "ZAPS", "ZIPS", "ZITS", "ZERO", "ZOOM", "ZOOS"]


def check_1800(string: str) -> set:
    numbers = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
    }
    all_words = {word: None for word in WORDS}
    for word in WORDS:
        code = ""
        for letter in word:
            for key in numbers.keys():
                if letter in numbers[key]:
                    code += key
        all_words[word] = code
    code_to_process = ""
    new_string = string.split("-")
    for word in new_string[2::]:
        code_to_process += all_words[word]

    lil_code_part = ""
    second_code_part = ""
    for i in code_to_process:
        while lil_code_part not in all_words.values():
            lil_code_part += i
    print(lil_code_part)


check_1800("1-800-INK-WANT")


# "{'1-800-HOLY-COT', '1-800-INK-WANT', '1-800-HOLY-ANT'}"


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


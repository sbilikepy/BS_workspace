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

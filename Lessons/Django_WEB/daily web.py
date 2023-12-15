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



print(sum_of_a_beach("sand"))#1
print(sum_of_a_beach("fishsandwatersun"))#4
print(sum_of_a_beach("PROPeRSaNofWATer"))#1
print(sum_of_a_beach("Given string SuN with spaces"))#1


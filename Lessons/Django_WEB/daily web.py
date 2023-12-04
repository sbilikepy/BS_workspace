def flatten_and_sort(lst: list) -> list:
    if len(lst):
        result = []
        for nested in lst:
            result += nested
        return sorted(result)
    return []




print(flatten_and_sort([[3], [1]]))
flatten_and_sort([[3, 2], [5, 1]])  #  [1, 2, 3, 5]
flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])  #  [1, 2, 3, 4, 5, 6, 7, 8, 9]
flatten_and_sort([[], []])  #  []
def testt():
    for i in range(10):
        print(i)
if __name__ == '__main__':
    testt()


def is_isogram(string: str) -> bool:
    print(set(string))
    print(string)
    if len(set(string.lower())) == len(string.lower()):
        return True
    return False

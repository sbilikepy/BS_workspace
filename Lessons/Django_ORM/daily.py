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
        if (sum_value - num) in nums[nums.index(num) + 1::]:
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

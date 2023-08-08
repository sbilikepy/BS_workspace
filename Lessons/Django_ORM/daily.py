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

capitals_first("academy Mate")


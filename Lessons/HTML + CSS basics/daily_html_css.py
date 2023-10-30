def calculate(string: str) -> str:
    result = []
    string = string.replace("plus", "p").replace("minus", "m")
    num = ""
    last_num = ""
    for i in range(len(string)):
        try:
            num += str(int(string[i]))
        except Exception:
            result.append(num)
            result.append(string[i])
            num = ""
    del num
    for i in string[::-1]:
        try:
            last_num += str(int(i))
        except Exception:
            result.append(last_num[::-1])
            break
    del last_num
    final_num = int(result[0])
    result = result[1::]
    for i in range(len(result)):
        if result[i] == "p":
            final_num += int(result[i + 1])
        if result[i] == "m":
            final_num -= int(result[i + 1])
    return str(final_num)


if __name__ == "__main__":
    calculate("123plus2plus3plus4")  # 10


def histogram(results: list) -> str:
    return (f"6|{'' if results[-1] == 0 else '#' * results[-1] + ' ' + str(results[-1])}\n"
            f"5|{'' if results[-2] == 0 else '#' * results[-2] + ' ' + str(results[-2])}\n"
            f"4|{'' if results[-3] == 0 else '#' * results[-3] + ' ' + str(results[-3])}\n"
            f"3|{'' if results[-4] == 0 else '#' * results[-4] + ' ' + str(results[-4])}\n"
            f"2|{'' if results[-5] == 0 else '#' * results[-5] + ' ' + str(results[-5])}\n"
            f"1|{'' if results[-6] == 0 else '#' * results[-6] + ' ' + str(results[-6])}\n")


print(histogram([7, 3, 10, 1, 0, 5]))

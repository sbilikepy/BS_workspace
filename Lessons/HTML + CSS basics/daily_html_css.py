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

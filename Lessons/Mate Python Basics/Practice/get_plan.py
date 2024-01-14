def is_special_number(number: int) -> str:
    temp = str(number)
    if number < 10 and number < 6:
        return "Special!!"
    elif number < 10 and number > 5:
        return "NOT!!"
    if "6" in temp or "7" in temp or "8" in temp or "9" in temp:
        return "NOT!!"

    return "Special!!"


print(is_special_number(121231231231723))

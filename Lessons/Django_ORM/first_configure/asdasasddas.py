def partlist(lst: list) -> list:
    result = []
    for i in range(1, len(lst)):
        p_1 = " ".join(lst[:i:])
        p_2 = " ".join(lst[i::])
        result.append(
            (p_1, p_2)
        )

    return result


partlist(["1", "2", "3", "4", "5", "6"])

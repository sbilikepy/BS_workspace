def get_unique_items(ls: list) -> list:
    unique_result = []
    ls.sort
    for i in ls:
        if i not in unique_result:
            unique_result.append(i)
    return unique_result

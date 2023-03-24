def double_power(current_powers: list) -> list:
    result = []
    temp_list = []
    for i in current_powers:
        x = i*2
        temp_list.append(x)
        return temp_list

print(double_power([100,200,300]))



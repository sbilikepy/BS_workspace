list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
start_point = 0
cycle_counter = 0
result = 0

while start_point <= 8:
    start_point += 1
    for i in list_num:
        result = start_point * i
        print(f"{start_point} * {i} = {result}")
        cycle_counter += 1

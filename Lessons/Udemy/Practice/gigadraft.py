# def is_tidy(number: int) -> bool:
#     temp = str(number)
#     for i in range(len(temp) - 1):
#         if temp[i] > temp[i + 1]:
#             return False
#     return True
# print(is_tidy(12))  # t
# print(is_tidy(32))  # f
# print(is_tidy(1024))  # f
# print(is_tidy(3445))  # t
# print(is_tidy(13579))  # t


def spiral(resolution: int):
    result = [0] * resolution**2
    result[-1] = resolution**2
    result = result[::-1]

    for i in range(1, len(result)):
        print(f"(i) = {(i)} // [i] = {[i]}")
        if result[i] < result[i - 1]:
            result[i] = result[i - 1] - 1

    result = result[::-1]

    # result.insert(resolution, "change direction")
    # for i in result[resolution-1::resolution+1]:
    #     result.insert(i,'change direction')
    # result.append('change direction')
    # print(f"result list at this stage: {result}")

    print(f"result list at final stage: {result}")
    return result


spiral(3)

def get_largest_expression_result(a, b):
    result = []
    v1 = a + b
    v2 = a - b
    v3 = a * b
    v4 = a / b
    result.append(v1)
    result.append(v2)
    result.append(v3)
    result.append(v4)
    return(max(result))
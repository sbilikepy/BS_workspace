romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


# XIV
def parse_roman(roman):
    result = 0

    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[roman[i]] < romans[roman[i + 1]]:  #
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]

    return result


print(parse_roman("I") == 1)
print(parse_roman("II") == 2)
print(parse_roman("IV") == 4)
print(parse_roman("X") == 10)
print(parse_roman("XIV") == 14)
print(parse_roman("L") == 50)
print(parse_roman("M") == 1000)

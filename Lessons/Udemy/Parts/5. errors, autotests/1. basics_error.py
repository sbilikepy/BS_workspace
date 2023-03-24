def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print (f'an error occurred: {ex}')
    except:
        print(f'unknown error occurred')
divider = int(input('input divider: ')) # str test
print(divide(100, divider))

for number in range(1, 101):
    if number % 15 == 0:
        print(number, "FizzBuzz")
    elif number % 5 == 0:
        print(number, "Buzz")
    elif number % 3 == 0:
        print(number, "Fizz")

    else:
        print(number)

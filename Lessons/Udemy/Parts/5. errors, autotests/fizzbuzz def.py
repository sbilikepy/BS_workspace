def get_reply(number):  # fizzbuzz
    if number % 5 == 0 and number % 3 == 0:
        print('Fizzbuzz')
        return 'Fizzbuzz'
    elif number % 5 == 0:
        print('Buzz')
        return 'Buzz'
    elif number % 3 == 0:
        print('Fizz')
        return 'Fizz'
    else:
        print('')


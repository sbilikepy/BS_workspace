def parity_checker() -> None:
    number_customer = int(input("What number do you want to check?"))
    result_checker = 0
    if number_customer == 0:
        print("Even")
    if number_customer % 2 == 0 and number_customer > 0:
        print("Even")
    if number_customer % 2 > 0 and number_customer > 0:
        print("Odd")

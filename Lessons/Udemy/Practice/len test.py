def get_drinks_with_step(number_of_guests: int, step: int) -> int:
    counter = 0
    for i in range(1, number_of_guests + 1, step):
        counter += i
    return len(counter)

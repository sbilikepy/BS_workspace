from typing import Union


def calculate_profit(amount: int, percent: Union[float, int], period: int) -> int:
    balance = amount
    for i in range(0, period):
        balance += balance * (percent / 100)

    return int(balance - amount)

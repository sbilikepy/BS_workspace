from bank_api import bank_api


class BankAccount(object):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def pay(self, to_number, amount):
        if amount < 0:
            raise ValueError("can't be negative")

        if amount > self.balance:
            raise ValueError("not enough money")

        bank_api.transfer(self.account_number, to_number, amount)

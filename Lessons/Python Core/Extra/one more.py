import random
import math

global_avg = []
amount = 100
coin_flip_conditions = ["H", "T"]
amount_log = [amount]


def just_one_more():
    global amount
    flip = random.choice(coin_flip_conditions)
    if flip == "H":
        amount *= 1.8
    else:
        amount *= 0.5
    amount_log.append(amount)


if __name__ == '__main__':
    for k in range(100):
        for i in range(100):
            just_one_more()
        print(amount_log)
        print(amount_log[-1])
        global_avg.append(amount_log[-1])
    print(global_avg)
    print(sum(global_avg)/len(global_avg))

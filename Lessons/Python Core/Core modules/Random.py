import random

# random.seed(1)
# for _ in range(10):
#     print(random.randint(1,10))

print(random.randint(1, 100))
list_ = [1, 2, 3]
print(random.choice(list_))
random.shuffle(list_)
print(list_)

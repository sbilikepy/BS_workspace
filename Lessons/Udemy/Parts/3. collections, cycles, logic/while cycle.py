x = 0
while x < 3:
    print (f'x equals {x}')# ДО ТЕХ ПОР ПОКА что то остается TRUE
    x+=1
else:
    print('condition is not met')
print('_________________________________')

vals = [1,2,3,4,5,6,7,8,9]
sum = 0
for v in vals:
    if v % 2 == 0:
        continue    # переход в v
    else:
        sum += v
    if sum > 10:
        break       # прекращает цикл
print(sum)

for v in vals:
    pass      # ничего не происходит, не знаю зачем нужно




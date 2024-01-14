# калькулятор цельсий в форенгейт и обратно
a = input("Исходное измерение Ц = c ; Ф = f :  ")
b = int(input("Какая температура:  "))
c = float(0)
for i in a:
    if i == "c":
        c = (b) * (9 / 5) + 32
        print(c)
        break
    elif i == "f":
        c = (b - 32) * (5 / 9)
        print(c)
        break

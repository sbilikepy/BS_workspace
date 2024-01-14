import os  # взаимодействие с файловой системой

# "r" - только чтение
# "r+" -и чтение и запись, при открытии в таком режиме файл должен существовать
# "w" - Write - создаёт, данные перезаписываются
# "w+" - Write - открывается на чтение и запись, данные перезаписываются
#           если он существовал, если не существовал - то создаем
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist, добавляет в конец, файл не создается

import getpass  # показывает текущую директорию

print(getpass.getuser())
with open("test.txt", "w") as f:  # write
    f.write("\n name | phone" "\n John;1234" "\n Bob;5678" "\n Alice;9432")

    f.close()

file = open("test.txt")
data = file.read()
print(data)
print(type(data))

print(file.read())  # курсор в конце файла
file.seek(0)  # курсор на 0 байт
print(file.read())
file.seek(0)
lines = file.readlines()  # возвращает список list
print(type(lines))
print(lines)
print(lines)
print(type(lines))
print(len(lines))

print(file.closed)

with open("test.txt") as sample_file:
    sample_data = sample_file.read()
    print(sample_data)

# f = open("test.txt", "r")  # read
# print(f.read())
# data = f.read()
# print (data)
print("__________________________________________________________")
with open("test.txt", mode="a") as sample_file:  # ОТДЕЛЬНО ЧТЕНИЕ  И ЗАПИСЬ
    sample_file.write("Eric;7639")
with open("test.txt", mode="r") as sample_file:
    print(sample_file.read())

print("__________________________________________________________")
print("__________________________________________________________")

with open("test.txt", mode="r+") as sample_file:
    sample_file.seek(0, 2)  # (0, 1, 2) начало, след после курсора, конец)
    sample_file.write("\nToub:3453")
    sample_file.seek(0)
    print(sample_file.read())

with open("abracadabra.txt", mode="w+") as spell_file:
    spell_file.write("abra-abra")
    spell_file.seek(0)
    print("__________________________________________________________")
    print(spell_file.read())

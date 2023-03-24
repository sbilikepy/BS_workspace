file = None
try:
    file = open(r'C:\notexist\something.txt')
    data = file.read()
except FileNotFoundError as ex:
    print(f'error has occurred. description: {ex.strerror}')
else:
    print('maybe else')
finally:
    print('finally1')
    if file:
        file.close()
        print('finally2') #

print( 'doing some work here ')   # test



def get_int():
    while True:
        try:
            reply = int(input('enter int here: '))
            return reply
        except:
            print(f'we need INT you dumbass')
            continue

number = get_int()

print('_________________________________')
print(number)

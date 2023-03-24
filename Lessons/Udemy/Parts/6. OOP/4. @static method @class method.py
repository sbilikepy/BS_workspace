class StaticTest():
    x = 1  # class
    # def __init__(self,):


t1 = StaticTest()
print(f'via instance: {t1.x}')
print(f'via class: {StaticTest.x}')
print('________________read and write_________________')
t1.x = 2  # instance
print(f'via instance: {t1.x}')
print(f'via class: {StaticTest.x}')

StaticTest.x = 3

print(f'via instance: {t1.x}')
print(f'via class: {StaticTest.x}')  # its dif atributes

print('___static methods creation example___')  # when no atributes, just method collection


class Date():
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):  # instance
        return f'{self.month} - {self.day} - {self.year}'

    @classmethod
    def millenium_classmethod(cls, month, day):  # self is instantion and cls is info about class
        return cls(month, day, 2000)

    @staticmethod
    def millenium_staticmethod(month, day):  # self is instantion and cls is info about class
        return Date(month, day, 2000)


date1 = Date.millenium_classmethod(6, 9)
date2 = Date.millenium_staticmethod(6, 9)

print(date1.display())
print(date2.display())


class DateTime(Date):
    def display(self):
        return f'{self.month} - {self.day} - {self.year} - 00:00:00 PM'


dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_staticmethod(10, 10)

print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))

print('________________display_________________')
print(dt1.display())
print(dt2.display())


# классметод содержит информацию о классе, поэтому конструируется именно он
# статикметод абстрагирован от класса


class StrConverter():

    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')

        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')

        else:
            value = bytes_or_str
        return value


print(StrConverter.to_str('\x41'))
print(StrConverter.to_str('A'))

print(StrConverter.to_bytes('\x41'))
print(StrConverter.to_bytes('A'))

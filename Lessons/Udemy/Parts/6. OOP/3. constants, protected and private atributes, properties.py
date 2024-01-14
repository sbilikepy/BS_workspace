class Character:
    MAX_SPEED = 100  # costant atribute CAPS

    def __init__(self, race, damage=10):
        self.damage = damage
        self.__race = (
            race  # private __n                  # то что не меняется, приватный
        )
        self._health = (
            100  # inheritance visible _n       # то что меняется редко, защищенный
        )
        self.current_speed = 20

    def hit(self, damage):
        self._healt -= damage

    @property  # декоратор свойства для чтения
    def health(self):
        return self._health

    @property  # декоратор свойства для чтения
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


print(Character.MAX_SPEED)
Character.MAX_SPEED = 10  # this constant can change
print(Character.MAX_SPEED)

c = Character("Elf", 20)
print(c._Character__race)
c._Character__race = "Orc"
print(c._Character__race)

c._health = 0
print(c._health)
print("___")
print(c.health)
print(c.race)

print(c.current_speed)
c.current_speed = 120
print(c.current_speed)

c.current_speed = -123
print(c.current_speed)

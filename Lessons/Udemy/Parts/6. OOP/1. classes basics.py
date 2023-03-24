from PIL import Image

with Image.open(
        r"C:\Users\BS_HOME\PycharmProjects\pythonProject_test_curse\__main__\lessons\6. OOP\python-classes.jpg") as im:
    im.rotate(0).show()


# oop

class Character():  # pascal casing rule

    def __init__(self, race, damage=10,
                 armor=20):  # определение конструктора, все атрибуты записываются через ссылку селф
        self.race = race
        self.damage = damage
        self.armor = armor


unit = Character('Elf', damage=20, armor=40)  #
print(type(unit))

print(unit.race, unit.damage, unit.armor)

class Character:
    max_speed = 1000  # можно обращаться без создания экземпляра
    max_health = 100
    death_health = 0

    def __init__(self, race, dmg=10, armor=20):  # методы
        self.race = race  # атрибуты
        self.dmg = dmg
        self.armor = armor
        self.health = 100
        # нельзя обращаться без создания экземпляра (инстанция)

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= Character.death_health


unit = Character("Orc")

print(unit.race, unit.dmg, unit.armor)
print(unit.max_speed)


unit.hit(20)
print(unit.health)
print(unit.is_dead())
unit.hit(80)
print(unit.is_dead())

unit.health = -200
print(unit.is_dead())

print(unit.health)

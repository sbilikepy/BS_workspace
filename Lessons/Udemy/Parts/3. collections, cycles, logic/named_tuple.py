#NamedTuple даёт возможность проименовать элементы, которые он сожержит
#NamedTupleCLASS = namedtuple('a', 'b')
#Subtup = [NamedTupleCLASS('a','name age etc')
# players = [('Carlsen',1990,2842), ('Caruana, 1992, 2822'), ('Mamedyarov', 1985, 2801)]
# print(type(players))
# print(type(players[0]))


from collections import namedtuple
player = namedtuple('player', 'name age elo')
players = [player('Carlsen',1990,2842), player('Caruana', 1992, 2822), player('Mamedyarov', 1985, 2801)]
print(players[0])
print(players[1])
print(players[2])
for a,b,c in players:
    print (a,b,c)
print('_____')

print(players[0])
print(players[0].name)
print(players[0].age)
print(players[0].elo)
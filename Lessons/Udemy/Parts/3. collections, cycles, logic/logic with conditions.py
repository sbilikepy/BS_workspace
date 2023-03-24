if True:
    print ('Indeed, true.')
if 3 > 2:
    print('3 is greater than 2')
if 3 < 2:
    print ('2 is less than 2')


is_admin = True
if is_admin:
    print ('Its admin')

selected_character = input('select your race:  ')
if selected_character == 'Protos':
    print('Protos is the most powerful race')
elif selected_character == 'Zerg':
    print ('Zerg is the most weak race but it spreads like a plague')
elif selected_character == 'Terrain':
    print ('Terrain is a race balanced between Zerg and Protos')
else:
    print('idk what race is it')
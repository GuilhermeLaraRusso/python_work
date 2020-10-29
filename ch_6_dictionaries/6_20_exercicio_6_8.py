# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

luna = {'kind': 'dog', 'owner': 'Lorenzo'}
rex = {'kind': 'dog', 'owner': 'Sandra'}
tuchinha = {'kind': 'dog', 'owner': 'Regina'}
xana = {'kind': 'cat', 'owner': 'Eduardo'}

pets = [luna, rex, tuchinha, xana]

for pet in pets:
    print(pet)

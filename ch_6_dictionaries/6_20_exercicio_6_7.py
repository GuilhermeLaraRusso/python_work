# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.


person_1 = {'first_name': 'Lorenzo', 'last_name': 'Russo', 'age': 6, 'city': 'Belo Horizonte'}
person_2 = {'first_name': 'Guilherme', 'last_name': 'Russo', 'age': 32, 'city': 'Belo Horizonte'}
person_3 = {'first_name': 'Thais', 'last_name': 'Silva', 'age': 32, 'city': 'Belo Horizonte'}

people = [person_1, person_2, person_3]

for person in people:
    print(person)
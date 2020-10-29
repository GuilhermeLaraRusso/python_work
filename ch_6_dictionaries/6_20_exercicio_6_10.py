# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {'Guilherme': [17, 13, 37],
                    'Thais': [8, 18, 44],
                    'Lorenzo': [6, 9, 14],
                    'Gloria': [17, 13, 23],
                    'Rogerio': [49, 55, 88]
                    }

for person, numbers in favorite_numbers.items():
    print(person.title() + "'s favorite numbers are: ")
    for number in numbers:
        print('\t' + str(number))
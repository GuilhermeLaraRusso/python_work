# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.



def show_magicians(magicians, great_magicians):
    """Print the name of the magicians and change the list"""
    """Of magicians to empty while adding Great to each magician"""
    while magicians:
        current_magician = 'Great ' + magicians.pop().title()
        great_magicians.append(current_magician)
    print(great_magicians)
    print(magicians)



def make_great(magicians):
    for magician in magicians:
        print('Great ' + magician.title())


magicians = ['barney', 'houdini', 'penn', 'teller']
great_magicians = []
# make_great(magicians)
show_magicians(magicians, great_magicians)
print(magicians)




# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.



def show_magicians(magicians, great_magicians):
    """Print the name of the magicians and change the list
    Of magicians to empty while adding Great to each magician"""
    while magicians:
        current_magician = 'Great ' + magicians.pop().title()
        great_magicians.append(current_magician)
    print(great_magicians)
    print(magicians)



magicians = ['barney', 'houdini', 'penn', 'teller']
great_magicians = []

show_magicians(magicians[:], great_magicians)
print(magicians)

def show_magicians(magicians, great_magicians):
    """Print the name of the magicians and change the list"""
    """Of magicians to empty while adding Great to each magician"""
    while magicians:
        current_magician = 'Great ' + magicians.pop().title()
        great_magicians.append(current_magician)
    print(great_magicians)
    print(magicians)

# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.

magicians = ['barney', 'houdini', 'penn', 'teller']

def show_magicians(magicians):
    """Print the name of the magicians"""
    for magician in magicians:
        print(magician.title())

show_magicians(magicians)
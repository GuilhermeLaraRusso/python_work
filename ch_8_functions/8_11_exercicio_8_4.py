# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(text='I love Python', size='large'):
    """Describing the size and the text printed on a T-Shirt"""
    print("\nYou have chosen the size '" + size.title() + "' with the message:")
    print(text)

make_shirt(size='m')

make_shirt(text='Be Happy', size='g')

make_shirt()
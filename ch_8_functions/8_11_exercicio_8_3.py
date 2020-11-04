# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, text):
    """Describing the size and the text printed on a T-Shirt"""
    print("\nYou have chosen the size '" + size.title() + "' with the message:")
    print(text)

make_shirt('m', 'Shit Happens')

make_shirt(text='Be Happy', size='g')
# When you use with, the file object returned by open() is only available inside
# the with block that contains it. If you want to retain access to a file’s contents
# outside the with block, you can store the file’s lines in a list inside the block
# and then work with that list. You can process parts of the file immediately
# and postpone some processing for later in the program.
# The following example stores the lines of pi_digits.txt in a list inside the
# with block and then prints the lines outside the with block:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
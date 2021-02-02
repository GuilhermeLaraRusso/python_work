# When you’re reading a file, you’ll often want to examine each line of the file.
# You might be looking for certain information in the file, or you might want to
# modify the text in the file in some way. For example, you might want to read
# through a file of weather data and work with any line that includes the word
# sunny in the description of that day’s weather. In a news report, you might
# look for any line with the tag <headline> and rewrite that line with a specific
# kind of formatting.
# You can use a for loop on the file object to examine each line from a
# file one at a time:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)


# These blank lines appear because an invisible newline character is
# at the end of each line in the text file. The print statement adds its own
# newline each time we call it, so we end up with two newline characters at
# the end of each line: one from the file and one from the print statement.
# Using rstrip() on each line in the print statement eliminates these extra
# blank lines:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
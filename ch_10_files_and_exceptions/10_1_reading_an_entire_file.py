# To try the following examples yourself, you can enter these lines in an
# editor and save the file as pi_digits.txt, or you can download the file from the
# book’s resources through https://www.nostarch.com/pythoncrashcourse/. Save
# the file in the same directory where you’ll store this chapter’s programs.
# Here’s a program that opens this file, reads it, and prints the contents
# of the file to the screen:


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# The first line of this program has a lot going on. Let’s start by looking
# at the open() function. To do any work with a file, even just printing its contents,
# you first need to open the file to access it. The open() function needs
# one argument: the name of the file you want to open. Python looks for this
# file in the directory where the program that’s currently being executed is
# stored. In this example, file_reader.py is currently running, so Python looks
# for pi_digits.txt in the directory where file_reader.py is stored. The open()
# function returns an object representing the file. Here, open('pi_digits.txt')
# returns an object representing pi_digits.txt. Python stores this object in
# file_object, which we’ll work with later in the program.
# The keyword with closes the file once access to it is no longer needed.
# Notice how we call open() in this program but not close(). You could open
# Files and Exceptions 191
# and close the file by calling open() and close(), but if a bug in your program
# prevents the close() statement from being executed, the file may never
# close. This may seem trivial, but improperly closed files can cause data
# to be lost or corrupted. And if you call close() too early in your program,
# you’ll find yourself trying to work with a closed file (a file you can’t access),
# which leads to more errors. It’s not always easy to know exactly when you
# should close a file, but with the structure shown here, Python will figure that
# out for you. All you have to do is open the file and work with it as desired,
# trusting that Python will close it automatically when the time is right.
# Once we have a file object representing pi_digits.txt, we use the read()
# method in the second line of our program to read the entire contents of
# the file and store it as one long string in contents. When we print the value
# of contents, we get the entire text file back:
#
# The only difference between this output and the original file is the
# extra blank line at the end of the output. The blank line appears because
# read() returns an empty string when it reaches the end of the file; this empty
# string shows up as a blank line. If you want to remove the extra blank line,
# you can use rstrip() in the print statement:
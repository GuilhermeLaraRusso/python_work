file_path = 'E:\Projetos\Python\python_work\ch_10_files_and_exceptions\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)


# Using absolute paths, you can read files from any location on your system.
# For now it’s easiest to store files in the same directory as your program
# files or in a folder such as text_files within the directory that stores your program
# files.
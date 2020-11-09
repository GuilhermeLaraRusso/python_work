# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *



# from magicos import show_magicians
#
# magicians = ['houdini', 'barney']
# great_magicians = []
#
# show_magicians(magicians, great_magicians)



# import magicos
#
# magicians = ['houdini', 'barney']
# great_magicians = []
#
# magicos.show_magicians(magicians, great_magicians)



# from magicos import show_magicians as sm
#
# magicians = ['houdini', 'barney']
# great_magicians = []
#
# sm(magicians, great_magicians)



# import magicos as mag
#
# magicians = ['houdini', 'barney']
# great_magicians = []
#
# mag.show_magicians(magicians, great_magicians)



from magicos import *

magicians = ['houdini', 'barney']
great_magicians = []

show_magicians(magicians, great_magicians)
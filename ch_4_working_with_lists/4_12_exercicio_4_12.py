# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake', 'strogonoff', 'fries', 'chocolate']

print('The first three items on the list are: ')
for food in my_foods[:3]:
    print(food.title())

print('\nThree items from the middle of the list are: ')
for food in my_foods[2:5]:
    print(food.title())

print('\nThe last three items in the list are:')
for food in my_foods[-3:]:
    print(food.title())
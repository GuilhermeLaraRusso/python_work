# To copy a list, you can make a slice that includes the entire original list
# by omitting the first index and the second index ([:]). This tells Python to
# make a slice that starts at the first item and ends with the last item, producing
# a copy of the entire list.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)



# This doesn't work:
# friend_foods = my_foods

# Instead of storing a copy of my_foods in friend_foods at u, we set
# friend_foods equal to my_foods. This syntax actually tells Python to connect
# the new variable friend_foods to the list that is already contained in
# my_foods, so now both variables point to the same list. As a result, when we
# add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice
# cream' will appear in both lists, even though it appears to be added only to
# friend_foods.


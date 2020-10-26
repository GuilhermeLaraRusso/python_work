# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

# • Tests for equality and inequality with strings

# • Tests using the lower() function

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

# • Tests using the and keyword and the or keyword

# • Test whether an item is in a list

# • Test whether an item is not in a list

car = 'BMW'
print(car == 'bmw')
print(car.lower() == 'bmw')
print(car != 'audi')

age_1 = 18
age_2 = 21
age_3 = 70

print(age_1 > 21)
print(age_1 <= 18)
print(age_2 >= 21)
print(age_1 >= 21 and age_2 >= 21)
print(age_2 >= 21 and age_3 >= 21)
print(age_1 >=50 or age_3 >= 50)

pizzas = ['pepperoni', 'calabresa', 'a moda', 'frago', 'portuguesa']
print('pepperoni' in pizzas)
print('calabresa' in pizzas)
print('marguerita' in pizzas)
print('marguerita' not in pizzas)
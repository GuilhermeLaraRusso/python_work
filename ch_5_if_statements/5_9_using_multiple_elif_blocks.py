# You can use as many elif blocks in your code as you like. For example, if the
# amusement park were to implement a discount for seniors, you could add
# one more conditional test to the code to determine whether someone qualified
# for the senior discount. Let’s say that anyone 65 or older pays half the
# regular admission, or $5:


age = 12

if age < 4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

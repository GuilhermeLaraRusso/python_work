# We’ve made a simple assumption about every list we’ve worked with so far;
# we’ve assumed that each list has at least one item in it. Soon we’ll let users
# provide the information that’s stored in a list, so we won’t be able to assume
# that a list has any items in it each time a loop is run. In this situation, it’s
# useful to check whether a list is empty before running a for loop.

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print('\nFinished making your pizza!')
else:
    print("Are you sure you want playn pizza?")

# This time we start out with an empty list of requested toppings at u.
# Instead of jumping right into a for loop, we do a quick check at v.
#
# When the name of a list is used in an if statement, Python returns True if the list contains
# at least one item; an empty list evaluates to False.
#
# If requested_toppings
# passes the conditional test, we run the same for loop we used in the previous
# example. If the conditional test fails, we print a message asking the customer
# if they really want a plain pizza with no toppings w.
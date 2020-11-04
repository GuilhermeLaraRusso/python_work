def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()


# At u the traceback tells us the location of the problem, allowing us to
# look back and see that something went wrong in our function call. At v
# the offending function call is written out for us to see. At w the traceback
# Functions 141
# tells us the call is missing two arguments and reports the names of the missing
# arguments.
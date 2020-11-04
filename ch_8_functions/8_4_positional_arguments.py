# When you call a function, Python must match each argument in the function
# call with a parameter in the function definition. The simplest way to
# do this is based on the order of the arguments provided. Values matched
# up this way are called positional arguments.
# To see how this works, consider a function that displays information
# about pets. The function tells us what kind of animal each pet is and the
# pet’s name, as shown here:

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'luna')


# The definition shows that this function needs a type of animal and the
# animal’s name u. When we call describe_pet(), we need to provide an animal
# type and a name, in that order. For example, in the function call, the
# argument 'hamster' is stored in the parameter animal_type and the argument
# 'harry' is stored in the parameter pet_name v. In the function body,
# these two parameters are used to display information about the pet being
# described.

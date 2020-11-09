# Sometimes you’ll want to prevent a function from modifying a list. For
# example, say that you start with a list of unprinted designs and write a
# 150 Chapter 8
# function to move them to a list of completed models, as in the previous
# example. You may decide that even though you’ve printed all the designs,
# you want to keep the original list of unprinted designs for your records. But
# because you moved all the design names out of unprinted_designs, the list is
# now empty, and the empty list is the only version you have; the original is
# gone. In this case, you can address this issue by passing the function a copy
# of the list, not the original. Any changes the function makes to the list will
# affect only the copy, leaving the original list intact.
# You can send a copy of a list to a function like this:

# function_name(list_name[:])

# The slice notation [:] makes a copy of the list to send to the function.
# If we didn’t want to empty the list of unprinted designs in print_models.py,
# we could call print_models() like this:



def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


# The function print_models() can do its work because it still receives the
# names of all unprinted designs. But this time it uses a copy of the original
# unprinted designs list, not the actual unprinted_designs list. The list
# completed_models will fill up with the names of printed models like it did
# before, but the original list of unprinted designs will be unaffected by the
# function.
# Even though you can preserve the contents of a list by passing a copy
# of it to your functions, you should pass the original list to functions unless
# you have a specific reason to pass a copy. It’s more efficient for a function
# to work with an existing list to avoid using the time and memory needed to
# make a separate copy, especially when you’re working with large lists.
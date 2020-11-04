# Sometimes it makes sense to make an argument optional so that people
# using the function can choose to provide extra information only if they
# want to. You can use default values to make an argument optional.
# For example, say we want to expand get_formatted_name() to handle
# middle names as well. A first attempt to include middle names might look
# like this:

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Avoiding Index Errors When Working with Lists


# This example results in an index error:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

# Python attempts to give you the item at index 3. But when it searches
# the list, no item in motorcycles has an index of 3. Because of the off-by-one
# nature of indexing in lists, this error is typical. People think the third item
# is item number 3, because they start counting at 1. But in Python the third
# item is number 2, because it starts indexing at 0.
# An index error means Python can’t figure out the index you requested. If
# an index error occurs in your program, try adjusting the index you’re asking
# for by one. Then run the program again to see if the results are correct.
# Keep in mind that whenever you want to access the last item in a list
# you use the index -1. This will always work, even if your list has changed
# size since the last time you accessed it:



# Outro exemplo
motorcycles = []
print(motorcycles[-1])
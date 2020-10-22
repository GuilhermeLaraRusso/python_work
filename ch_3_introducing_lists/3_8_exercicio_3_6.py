# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.

# • Use insert() to add one new guest to the beginning of your list.

# • Use insert() to add one new guest to the middle of your list.

# • Use append() to add one new guest to the end of your list.

# • Print a new set of invitation messages, one for each person in your list.

guests = ['Thais', 'Lorenzo', 'Ayrton Senna', 'John Travolta']
guests.insert(0, 'Gill Bates')
guests.insert(2, 'Bruce Willis')
guests.append('Batman')
print(guests)

print(guests[0] + ', você está convidado para a mair festa do ano!')
print(guests[1] + ', você está convidado para a mair festa do ano!')
print(guests[2] + ', você está convidado para a mair festa do ano!')
print(guests[3] + ', você está convidado para a mair festa do ano!')
print(guests[4] + ', você está convidado para a mair festa do ano!')
print(guests[5] + ', você está convidado para a mair festa do ano!')
print(guests[6] + ', você está convidado para a mair festa do ano!')



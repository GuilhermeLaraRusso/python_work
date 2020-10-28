# To modify a value in a dictionary, give the name of the dictionary with the
# key in square brackets and then the new value you want associated with
# that key.

#
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + '.')
#
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + '.')



# For a more interesting example, let’s track the position of an alien that
# can move at different speeds. We’ll store a value representing the alien’s
# current speed and then use it to determine how far to the right the alien
# should move:



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('"Original x-position: ' + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New' x-position: " + str(alien_0['x_position']))

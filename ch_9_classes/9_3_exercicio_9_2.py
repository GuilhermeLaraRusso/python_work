# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() +
              " possui cozinha do tipo " + self.cuisine_type.title() + "!")

    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " está aberto!")


pepe = Restaurant('pepê', 'brasileira')
jsan = Restaurant('J-san', 'japonesa')
rocco = Restaurant('Rocco', 'hamburguer')

pepe.describe_restaurant()
jsan.describe_restaurant()
rocco.describe_restaurant()
pepe.open_restaurant()
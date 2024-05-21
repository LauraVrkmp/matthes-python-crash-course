class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}, "
              f"and the cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is open!")

restaurant = Restaurant("Chez moi", "French")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
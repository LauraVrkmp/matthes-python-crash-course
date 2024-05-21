class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}, "
              f"and the cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is open!")
    
restaurant_1 = Restaurant("Bon appetit", "French")
restaurant_2 = Restaurant("Chez moi", "French")
restaurant_3 = Restaurant("All-you-can-eat", "American")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
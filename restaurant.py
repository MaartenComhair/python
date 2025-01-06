class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Name restaurant: {self.restaurant_name}")
        print(f"Cuisine type restaurant: {self.cuisine_type}")

    def open_restaurant(self):
        print(F"{self.restaurant_name} is currently open")

    def set_numbers_served(self):
        print(f"numbers served: {self.number_served}")

    def increment_numbers_served(self, increment):
        self.number_served += increment

    

    

restaurant = Restaurant("Tante Julia", "Belgisch eten")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()
restaurant.set_numbers_served()
restaurant.number_served = 20
restaurant.set_numbers_served()
restaurant.increment_numbers_served(10)
restaurant.set_numbers_served()


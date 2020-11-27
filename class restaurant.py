class Restaurant:
    """A simple attempt to model restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'My restaurant is called {self.restaurant_name.title()}!\nWe serve wonderfull {self.cuisine_type.title()}!')

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open!')

    def set_number_served ( self , number_served ) :
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, new_costumers_served):
        """Add the given amount to the number of costumers served"""
        self.number_served += new_costumers_served


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))
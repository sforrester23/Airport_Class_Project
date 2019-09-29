from People_Class import *

# Define new subclass of people
class Passenger(People):
    # Define all the attributes for customers, including the ones inherited from People
    # Inherit the same attributes as People class
    def __init__(self, first_name, last_name, age, phone_number, passport_number):
        # Select the new attributes to add as well
        super().__init__(first_name, last_name, age, phone_number)
        self.passport_number = passport_number


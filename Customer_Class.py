from People_Class import *

# Define new subclass of people
class Customer(People):
    # Define all the attributes for customers, including the ones inherited from People
    # Inherit the same attributes as People class
    def __init__(self, first_name, last_name, age, email, phone_number, passport_number, flight_number, destination_airport, origin_airport):
        # Select the new attributes to add as well
        super().__init__(first_name, last_name, age, email, phone_number)
        self.passport_number = passport_number
        self.flight_number = flight_number
        self.destination_airport = destination_airport
        self.origin_airport = origin_airport



from People_Class import *

# Define new subclass of people
class Passenger(People):
    # Define all the attributes for customers, including the ones inherited from People
    # Inherit the same attributes as People class
    def __init__(self, first_name, last_name, age, phone_number, passport_number, flight_number):
        # Select the new attributes to add as well
        super().__init__(first_name, last_name, age, phone_number)
        self.passport_number = passport_number
        self.flight_number = flight_number
        self.info_passenger = []
        self.info_flights = []

    def passenger_add(self, passenger):
        # passenger_f_name = input('What is the passengers first name? ')
        # passenger_l_name = input('What is the passengers last name? ')
        # passenger_age = int(input('How old is the passenger? '))
        # passenger_phone = input('What is the passenger\'s phone number? ')
        # passenger_passport = input('What is the passenger\'s passport number? ')
        # passenger_flight_num = input('What is the passenger\'s flight number? ')
        # passenger = Passenger(passenger_f_name, passenger_l_name, passenger_age, passenger_phone, passenger_passport, passenger_flight_num)
        # 'This is the passenger:' ['Passenger ID: {}'.format(passenger_id, passenger.first_name, passenger.last_name, passenger.passenger_flight_num, passenger.passport_number]
        # passenger = [passenger_id, passenger, passenger_flight_num]
        # passengers.append(passenger)

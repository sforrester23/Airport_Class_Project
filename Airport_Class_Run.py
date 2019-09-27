from People_Class import *
from Passenger_Class import *
from Plane_Class import *
from Flight_Class import *
from Employee_Class import *

# print('PASSENGER INFORMATION')
# print('_____________________')
# # CUSTOMER: first_name, last_name, age, email, phone_number, passport_number, flight_number, destination_airport, origin_airport
# customer_1 = Customer('Sam', 'Forrester', 24, 'sforrester@spartaglobal.com', '07902105573', 505450007, 'BA0418', 'Antananrivo', 'Talinn')
# print(customer_1.first_name)
# print(customer_1.last_name)
# print(customer_1.age)
# print(customer_1.email)
# print(customer_1.phone_number)
# print(customer_1.passport_number)
# print(customer_1.flight_number)
# print(customer_1.destination_airport)
# print(customer_1.origin_airport)
# print(' ')
# print('//////////////////////////////////////////')
# print(' ')
# print('FLIGHT INFORMATION')
# print('_____________________')
# # FLIGHT: model_number, capacity, flight_ID, destination, origin, departure_time, duration
flight_1 = Flight('BA0418', 'Antanarivo', 'Talinn', '9:30', 10)
flight_2 = Flight('BA0416', 'Luxembourg', 'Mumbai', '17:35', 12)
flight_3 = Flight('EJ5879', 'Ibiza', 'Kavos', '12:15', 3.5)
flight_4 = Flight('TC5031', 'Tripoli', 'Montevideo', '15:55', 5.25)
flight_5 = Flight('RY0469', 'Addis Ababa', 'Paracas', '19:00', 8)

print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_1.flight_ID, flight_1.origin, flight_1.destination, flight_1.departure_time, flight_1.duration))
print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_2.flight_ID, flight_2.origin, flight_2.destination, flight_2.departure_time, flight_2.duration))
print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_3.flight_ID, flight_3.origin, flight_3.destination, flight_3.departure_time, flight_3.duration))
print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_4.flight_ID, flight_4.origin, flight_4.destination, flight_4.departure_time, flight_4.duration))
print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_5.flight_ID, flight_5.origin, flight_5.destination, flight_5.departure_time, flight_5.duration))

# print(flight_1.flight_ID)
# print(flight_1.destination)
# print(flight_1.origin)
# print(flight_1.departure_time)
# print(flight_1.duration)

# EMPLOYEE: first_name, last_name, age, email, phone_number, employee_ID, job
employee_257 = Employee('Ronald', 'Tastytoes', 87, '07801216489', 257, 'Pilot')


# print('Please enter your Employee ID')
# input_employee_ID = input('')
# if input_employee_ID in
passengers = [] # make an empty list of passengers for adding to.

print('What would you like to do?')
print('- Select 1 for list all flights.')
print('- Select 2 for creating a passenger.')
print('- Select 3 for adding a passenger to a flight.')
print('- Select 4 for listing names and passport numbers of a flight')
print('Type EXIT to leave')

choice = input('Option: ').upper()
passenger_ID = 1

while choice != 'EXIT':
    # Pseudo code
    # If 1 then this
    # which flights would you like to list?#
    if choice == '1':
        print('Which flight would you like to see?')
        print('Please select from the following:')
        print('1 - Flight BA0418')
        print('2 - Flight: BA0416')
        print('3 - Flight: EJ5879')
        print('4 - Flight: TC5031')
        print('5 - Flight: RY0469')
        print('6 - ALL FLIGHTS')
        which_flight = input('Select one: ')
        if which_flight == '1':
            print(flight_1.list_flights())
        elif which_flight == '2':
            print(flight_2.list_flights())
        elif which_flight == '3':
            print(flight_3.list_flights())
        elif which_flight == '4':
            print(flight_4.list_flights())
        elif which_flight == '5':
            print(flight_5.list_flights())
        elif which_flight == '6':
            print(flight_1.list_flights())
            print(flight_2.list_flights())
            print(flight_3.list_flights())
            print(flight_4.list_flights())
            print(flight_5.list_flights())
        else:
            print('Sorry, I didn\'t quite catch what you wanted to do.')

    elif choice == '2':
        passenger_f_name = input('What is the passengers first name? ')
        passenger_l_name = input('What is the passengers last name? ')
        passenger_age = int(input('How old is the passenger? '))
        passenger_phone = input('What is the passenger\'s phone number? ')
        passenger_passport = input('What is the passenger\'s passport number? ')
        passenger_flight_num = input('What is the passenger\'s flight number? ' )
        passenger = Passenger(passenger_f_name, passenger_l_name, passenger_age, passenger_phone, passenger_passport, passenger_passport)
        print(passenger.passenger_add(passenger))
        # print('This is the passenger: ')
        # print(['Passenger ID is: {}'.format(passenger_ID), passenger.first_name, passenger.last_name, passenger.flight_number, passenger.passport_number])
        # passenger = [passenger_ID, passenger]
        # passengers.append(passenger)
        passenger_ID += 1

    # elif choice == '3':



    print('What would you like to do now?')
    print('- Select 1 for list all flights.')
    print('- Select 2 for creating a passenger.')
    print('- Select 3 for adding a passenger to a flight.')
    print('- Select 4 for listing names and passport numbers of a flight')
    print('Type EXIT to leave')

    choice = input('Option: ').upper()






# If 2 then this
    # input passenger information and assign it to a new passenger entry
# If 3 then this
    # add said passenger to a list of flights
# If 4 then this
    # list all names and passport numbers nicely with


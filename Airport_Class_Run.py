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
flight_3 = Flight('EJ5879', 'Ibiza', 'Miami', '12:15', 3.5)
flight_4 = Flight('TC5031', 'Tripoli', 'Montevideo', '15:55', 5.25)
flight_5 = Flight('RY0469', 'Addis Ababa', 'Caracas', '19:00', 8)
# make the flights into a list, for iteration purposes later.
flight_list = [flight_1, flight_2, flight_3, flight_4, flight_5]

# print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_1.flight_ID, flight_1.origin, flight_1.destination, flight_1.departure_time, flight_1.duration))
# print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_2.flight_ID, flight_2.origin, flight_2.destination, flight_2.departure_time, flight_2.duration))
# print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_3.flight_ID, flight_3.origin, flight_3.destination, flight_3.departure_time, flight_3.duration))
# print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_4.flight_ID, flight_4.origin, flight_4.destination, flight_4.departure_time, flight_4.duration))
# print('Flight {} from {} to {} is departing at {} and takes {} hours'. format(flight_5.flight_ID, flight_5.origin, flight_5.destination, flight_5.departure_time, flight_5.duration))

# print(flight_1.flight_ID)
# print(flight_1.destination)
# print(flight_1.origin)
# print(flight_1.departure_time)
# print(flight_1.duration)

# EMPLOYEE: first_name, last_name, age, email, phone_number, employee_ID, job
employee_257 = Employee('Ronald', 'Tastytoes', 87, '07801216489', 257, 'Pilot')

# build a employee login section to begin with and authenticate
# print('Please enter your Employee ID')
# input_employee_ID = input('')
# if input_employee_ID in

print('What would you like to do?')
print('- Select 1 for list all flights.')
print('- Select 2 for creating a passenger.')
print('- Select 3 for adding a passenger to a flight.')
print('- Select 4 for listing names and passport numbers of a flight')
print('Type EXIT to leave.')

choice = input('Option: ').upper()

passenger_list = [] # make an empty list for passengers and their information. This will store class instances of passengers.
name_list = [] # make an empty list of names of passengers for adding to later - part of testing.

# Run the program the whole time the user doesn't enter exit when prompted
while choice != 'EXIT':
    # What should we do when the user chooses option 1?
    if choice == '1':
        print(' ')
        print('Which flight would you like to see?')
        print('Please select from the following:')
        print('1 - Flight BA0418')
        print('2 - Flight: BA0416')
        print('3 - Flight: EJ5879')
        print('4 - Flight: TC5031')
        print('5 - Flight: RY0469')
        print('6 - ALL FLIGHTS')
        # Ask them which flight they'd like to see, as well as an option to view all flights
        which_flight = input('Select one: ')
        # Display the following based on their choice of flight
        if which_flight == '1': # flight 1
            print(flight_1.list_flights())
        elif which_flight == '2': # flight 2
            print(flight_2.list_flights())
        elif which_flight == '3': # flight 3
            print(flight_3.list_flights())
        elif which_flight == '4': # flight 4
            print(flight_4.list_flights())
        elif which_flight == '5': # flight 5
            print(flight_5.list_flights())
        elif which_flight == '6': # all flights
            print(flight_1.list_flights())
            print(flight_2.list_flights())
            print(flight_3.list_flights())
            print(flight_4.list_flights())
            print(flight_5.list_flights())
        else: # else show them that they didn't enter right info and it'll take them back to the prompt menu
            print('Sorry, I didn\'t quite catch what you wanted to do.')

    # If they selected option two, to input a passengers information
    elif choice == '2':
        print(' ')
        # Ask them for passengers information
        passenger_f_name = input('What is the passengers first name? ').capitalize()
        passenger_l_name = input('What is the passengers last name? ').capitalize()
        passenger_age = int(input('How old is the passenger? '))
        passenger_phone = input('What is the passenger\'s phone number? ')
        passenger_passport = input('What is the passenger\'s passport number? ')
        # Set up an empty list for passengers to be assigned to with a unique passenger ID
        # Run the method of adding a passenger for this employee, based on the input information provided
        employee_257.passenger_add(passenger_f_name, passenger_l_name, passenger_age, passenger_phone, passenger_passport)
        # Add this information to the passenger information list, so it gets assigned a unique ID
        # Add this list to the larger list for ALL passenger
        passenger_list = employee_257.passenger_info
        # Testing
        # Below prints a running list of names for the passengers added, just so you can stay on track of them - testing
        for key in range(len(passenger_list)):
            name_list.append(passenger_list[key].first_name)
        print(name_list)



        #TESTING PASSENGER INPUT:
        # print(employee_257.passenger_info)
        # print(employee_257.passenger_info[0].first_name)
        # print(employee_257.passenger_info[0].last_name)
        # print(employee_257.passenger_info[0].age)
        # print(employee_257.passenger_info[0].phone_number)
        # print(employee_257.passenger_info[0].passport_number)
        # print(employee_257.passenger_info[0].flight_number)

    # If they selected option 3, to add a passenger to a flight:
    elif choice == '3':
        print(' ')
        # Ask them for the information on the passenger they'd like to add to a given flight
        passenger_f_name_add = input('What is the FIRST NAME of the person you\'d like to add? ').strip()
        passenger_l_name_add = input('What is the LAST NAME of the person you\'d like to add? ').strip()
        passenger_passport_add = input('What is the PASSPORT NUMBER of the person you\'d like to add? ').strip()
        # Begin the checks on whether or not the passenger information they've entered matches up with the data entered in the 'input passenger' section.
        # by default, we'll assume that the passport is not in the list
        passport_in_list = False
        # iterate through the values in the list of passenger information, if any created in step 3
        for count in range(len(employee_257.passenger_info)):
            # check each class instance in the list and see if it contains the passport number that the user wishes to add to a flight
            if passenger_passport_add in employee_257.passenger_info[count].passport_number:
                # only change the logical statement 'passport_in_list' to True if it exists in the list
                passport_in_list = True
        # if the passport is in the list of pre-entered passengers (i.e. if passport_in_list = True), then ask the user which flight they would like to add the passenger to. They are allowed because the passenger is in the system.
        if passport_in_list:
            print(' ')
            # give the user options on which flight to add the passenger to
            print('Which flight would you like to add them to? Enter flight number from list below: ')
            print('Option 1: {} - {} to {}'.format(flight_1.flight_ID, flight_1.origin, flight_1.destination))
            print('Option 2: {} - {} to {}'.format(flight_2.flight_ID, flight_2.origin, flight_2.destination))
            print('Option 3: {} - {} to {}'.format(flight_3.flight_ID, flight_3.origin, flight_3.destination))
            print('Option 4: {} - {} to {}'.format(flight_4.flight_ID, flight_4.origin, flight_4.destination))
            print('Option 5: {} - {} to {}'.format(flight_5.flight_ID, flight_5.origin, flight_5.destination))
            # take input for their answer
            flight_to_add_to = int(input('Please choose an option from the above: ').strip())
            # carry out the method defined in the Passenger_Class file called passenger_add_flight to add the passengers to the user's selected flight, based on the user's choice
            if flight_to_add_to == 1:
                flight_1.passenger_add_flight(passenger_f_name_add, passenger_l_name_add, passenger_passport_add)
                print(flight_1.passengers_on_flight)
            elif flight_to_add_to == 2:
                flight_2.passenger_add_flight(passenger_f_name_add, passenger_l_name_add, passenger_passport_add)
                print(flight_2.passengers_on_flight)
            elif flight_to_add_to == 3:
                flight_3.passenger_add_flight(passenger_f_name_add, passenger_l_name_add, passenger_passport_add)
                print(flight_3.passengers_on_flight)
            elif flight_to_add_to == 4:
                flight_4.passenger_add_flight(passenger_f_name_add, passenger_l_name_add, passenger_passport_add)
                print(flight_4.passengers_on_flight)
            elif flight_to_add_to == 5:
                flight_5.passenger_add_flight(passenger_f_name_add, passenger_l_name_add, passenger_passport_add)
                print(flight_5.passengers_on_flight)
            # If they did not enter one of the options above, then it will take them back to a prompt screen
            else:
                print('Sorry, I did not recognise the flight option you entered. Please try again.')
        # else statement for the instance when the passenger number is not included in the system.
        # If so, prompt the user to add them to the passenger section and it will take them to the menu screen with prompt.
        else:
            print('Sorry that is not a passenger with a passport number in the system. Please enter the passenger before adding them to a flight.')

    # If the user selects option 4, to list all flights and their passenger numbers
    elif choice == '4':
        print(' ')
        # ask the user which flight they'd like to print the information of
        print('Which flight would you like to list the names and passport numbers of?')
        # for loop for displaying the flight options available to the user. This can therefore be applied to any length list of flights.
        for index in range(len(flight_list)):
            # print a different flight information based on the index number of the for loop.
            # This iterates through all flights in the list flight_list
            print('Option {}: {} - {} to {}'.format(index+1, flight_list[index].flight_ID, flight_list[index].origin, flight_list[index].destination))
        # set up a while loop for error checking
        while True:
            # Try the following section of code to see if it throws out any errors
            try:
                # ask the user for their choice, assign it to an integer (this is where the error is likely to come up, for instance if the user inputs a string - or rather something that can not be converted into an integer data type).
                flight_choice = int(input('Please choose an option from the above: ').strip())
                if flight_choice > len(flight_list)-1 and flight_choice < 0:
                    raise ValueError('That value is not in the range of options listed. Please try again.')
            # if there is a value error, like you get if you try to assign a string to an integer, print this error message
            except ValueError:
                print('Oh no, that\'s not a valid input for the options given! please enter a valid number.')
                # continue from the top of the while loop, giving the user the opportunity to re-enter a value in the range.
                continue
            else:
                for number in range(len(flight_list)):
                    if int(flight_choice) == number+1:
                        print(flight_list[number].passengers_on_flight)
                        break
                break
    else:
        print('Sorry, that is not an option available. Please try again.')






    print(' ')
    print('What would you like to do now?')
    print('- Select 1 for list all flights.')
    print('- Select 2 for creating a passenger.')
    print('- Select 3 for adding a passenger to a flight.')
    print('- Select 4 for listing names and passport numbers of a flight')
    print('Type EXIT to leave.')

    choice = input('Option: ').upper()






# If 2 then this
    # input passenger information and assign it to a new passenger entry
# If 3 then this
    # add said passenger to a list of flights
# If 4 then this
    # list all names and passport numbers nicely with


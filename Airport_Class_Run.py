# Possible customisations:
# Employee ID login section - encapsulation
# error checking in multiple places for strings entered when they should be integers
# add more users to be able to access the program?

import sys
from People_Class import *
from Passenger_Class import *
from Plane_Class import *
from Flight_Class import *
from Employee_Class import *

# Define the flights currently available
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

# EMPLOYEE: first_name, last_name, age, email, phone_number, employee_ID, job
employee_257 = Employee('Ronald', 'Tastytoes', 87, '07801216489', 257, 'Pilot')

# employee login section to begin with to authenticate.
# should use encapsulation to execute this, so no one can look at the code and find a users password.
# Define a maximum number of attempts
num_of_attempts = 3
# The whole time the number of attempts is positive, keep letting the user attempt to login
while num_of_attempts >0:
    # Ask for the users login
    employee_id_attempt = int(input('What is your employee login?: '))
    # Check if their inputted login is what the system thinks it is
    if employee_id_attempt == employee_257.employee_ID:
        # If they're correct, grant access and welcome them
        print('Access Granted.')
        print('Welcome {} {}!'.format(employee_257.first_name, employee_257.last_name))
        # break the while loop so they don't have to keep guessing
        break
    else:
        # Otherwise, tell them they failed and reduce the number of attempts by 1.
        print('Access Denied. Retry...')
        num_of_attempts -= 1
        # Tell them how many attempts they have left.
        print('Number of attempts remaining: {}'.format(num_of_attempts))
        if num_of_attempts <= 0:
            # If the number of attempts becomes 0 or less (somehow), end the program.
            sys.exit('Sorry, you have exceeded your number of login attempts! Bye.')
        continue

# List the users options on what they'd like to do
print('What would you like to do?')
print('- Select 1 for list all flights.')
print('- Select 2 for creating a passenger.')
print('- Select 3 for adding a passenger to a flight.')
print('- Select 4 for listing names and passport numbers of a flight.')
print('Type EXIT to leave.')
# take their choice and store it
choice = input('Option: ').upper()

passenger_list = [] # make an empty list for passengers and their information. This will store class instances of passengers.
name_list = [] # make an empty list of names of passengers for adding to later - part of testing.

# Run the program the whole time the user doesn't enter type exit when prompted
while choice != 'EXIT':
    # What should we do when the user chooses option 1?
    if choice == '1':
        print(' ') # line break in terminal
        print('Which flight would you like to see?')
        print('Please select from the following:')
        # Set up for loop for printing the flights in the list of flights.
        # We must define the range of the iteration by using range(len()) as otherwise it wont recognise the range as integers and won't iterate properly.
        for index in range(len(flight_list)):
            print('{} - Flight: {}'.format(index+1, flight_list[index].flight_ID))
        print('0 - ALL FLIGHTS')
        # Ask them which flight they'd like to see, as well as an option to view all flights
        which_flight = int(input('Select one: '))
        # Display the following based on their choice of flight
        # THIS CAN BE REFACTORED AS A FOR LOOP AS WE'LL SEE LATER ON
        # refactoring like this would enable us to display all flights stored in a list, not just the original 5 we started with
        # this creates a possibility to add any number of flights, and even have an option to do so in the main menu
        # if the option given is in the range of the options, i.e. if it is above or equal to 1 and below or equal to the end of the range option (give by len(flight_list)
        if which_flight <= len(flight_list) and which_flight >= 1:
            # for loop to iterate the printing of only the option that the user has inputted
            for num in range(len(flight_list)):
                # this if statement means it only prints the flight information that is equal to the choice specified by the user
                if num == which_flight-1:
                    print(flight_list[num].list_flights())
        # elif statements for printing all the flights, if user chose option 0
        elif which_flight == 0:
            for num in range(len(flight_list)):
                print(flight_list[num].list_flights())
        # else show them that they didn't enter right info and it'll take them back to the main menu and prompt
        else:
            print('Sorry, that is not one of the options. Please try again.')

    # If they selected option two, to input a passengers information
    elif choice == '2':
        print(' ') # space line in terminal
        # Ask them for passengers information
        passenger_f_name = input('What is the passengers first name? ').capitalize()
        passenger_l_name = input('What is the passengers last name? ').capitalize()
        passenger_age = int(input('How old is the passenger? '))
        passenger_phone = input('What is the passenger\'s phone number? ')
        passenger_passport = input('What is the passenger\'s passport number? ')

        # Run the method of adding a passenger for this employee, based on the input information provided
        employee_257.passenger_add(passenger_f_name, passenger_l_name, passenger_age, passenger_phone, passenger_passport)

        # Add this list to the larger list for ALL passengers, so we don't have to access the same employees information all the time
        # In a nice PERSISTENT world, we'd have a general list for every employee to access and wouldn't matter if another employee logged in and started inputting passengers' information, it would have the same passengers that had been added.
        # Unfortunately, we're only going to have one employee logging in and adding things, so the next line wouldn't really matter that much. But it's nice to rename complicated variables into smoother ones. We'll use this nicer notation from this point on, even if we don't need to for this example.
        passenger_list = employee_257.passenger_info
        # Let the user know you've added the passenger they wanted to.
        # Do this by accessing the last entry in passenger_list with [len(passenger_list) -1] as the list index
        print('Passenger {} {} added.'.format(passenger_list[len(passenger_list)-1].first_name, passenger_list[len(passenger_list)-1].last_name))

        # Testing
        # Below prints a running list of names for the passengers added, just so you can stay on track of them - testing
        # for key in range(len(passenger_list)):
        #     name_list.append(passenger_list[key].first_name)
        # print(name_list)

    # If they selected option 3, to add a passenger to a flight:
    elif choice == '3':
        print(' ') # line break in terminal

        # Ask them for the information on the passenger they'd like to add to a given flight
        passenger_f_name_add = input('What is the FIRST NAME of the person you\'d like to add? ').strip()
        passenger_l_name_add = input('What is the LAST NAME of the person you\'d like to add? ').strip()
        passenger_passport_add = input('What is the PASSPORT NUMBER of the person you\'d like to add? ').strip()

        # Begin the checks on whether or not the passenger information they've entered matches up with the data entered in the 'input passenger' section.
        # by default, we'll assume that the passport is not in the list
        passport_in_list = False
        # iterate through the values in the list of passenger information, if any created in step 3
        for count in range(len(passenger_list)):
            # check each class instance in the list and see if it contains the passport number that the user wishes to add to a flight
            if passenger_passport_add in passenger_list[count].passport_number:
                # only change the logical statement 'passport_in_list' to True if it exists in the list
                passport_in_list = True
        # if the passport is in the list of pre-entered passengers (i.e. if passport_in_list = True), then ask the user which flight they would like to add the passenger to. They are allowed because the passenger is in the system.
        if passport_in_list:
            print(' ')
            # give the user options on which flight to add the passenger to (can be refactored into for loop)
            print('Which flight would you like to add them to? Enter flight number from list below: ')
            for index in range(len(flight_list)):
                print('Option {}: {} - {} to {}'.format(index+1, flight_list[index].flight_ID, flight_list[index].origin, flight_list[index].destination))
            # print('Option 1: {} - {} to {}'.format(flight_1.flight_ID, flight_1.origin, flight_1.destination))
            # print('Option 2: {} - {} to {}'.format(flight_2.flight_ID, flight_2.origin, flight_2.destination))
            # print('Option 3: {} - {} to {}'.format(flight_3.flight_ID, flight_3.origin, flight_3.destination))
            # print('Option 4: {} - {} to {}'.format(flight_4.flight_ID, flight_4.origin, flight_4.destination))
            # print('Option 5: {} - {} to {}'.format(flight_5.flight_ID, flight_5.origin, flight_5.destination))
            # take input for their answer
            flight_to_add_to = int(input('Please choose an option from the above: ').strip())
            # carry out the method defined in the Passenger_Class file called passenger_add_flight to add the passengers to the user's selected flight, based on the user's choice (refactored into a for loop from if statement)
            if flight_to_add_to <= len(flight_list):
                for index in range(len(flight_list)):
                    if index == flight_to_add_to-1:
                        flight_list[index].passenger_add_flight(passenger_f_name_add, passenger_l_name_add, passenger_passport_add)
                        print('Passenger with passport number {} added to flight option {} successfully'.format(passenger_passport_add, flight_to_add_to))
            # Else if the number inputted is not in the flight list's range, tell the user the number they inputted is incorrect.
            else:
                print('Sorry, I did not recognise the flight option you entered. Please try again.')

        # else statement for the instance when the passengers passport number is not included in the system.
        # If so, prompt the user to add them to the passenger section and it will take them to the menu screen with prompt.
        else:
            print('Sorry that is not a passenger with a passport number in the system. Please enter the passenger before adding them to a flight.')

    # If the user selects option 4, to list all flights and their passenger numbers
    elif choice == '4':
        print(' ') # line break in terminal
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
                        # print(flight_list[number].passengers_on_flight[0])
                        for index in range(len(flight_list[number].passengers_on_flight)):
                            print(' ')
                            print('Passenger number {}'.format(index+1))
                            print('Name: {} {}'.format(flight_list[number].passengers_on_flight[index][0], flight_list[number].passengers_on_flight[index][1]))
                            print('Passport Number: {}'.format(flight_list[number].passengers_on_flight[index][2]))
                        break
                break
    else:
        print('Sorry, that is not an option available. Please try again.')

    # This appears at the end of the while loop. It acts as the prompt to the user whenever another action is carried out.
    # The terminal will always drop back down to this list of options and input prompt unless 'exit' is entered,
    # terminating the while loop, and hence the script.
    print(' ')
    print('What would you like to do now?')
    print('- Select 1 for list all flights.')
    print('- Select 2 for creating a passenger.')
    print('- Select 3 for adding a passenger to a flight.')
    print('- Select 4 for listing names and passport numbers of a flight.')
    print('Type EXIT to leave.')
    # What does the user select?
    choice = input('Option: ').upper()

    # While loop runs again! Unless 'exit' is entered.

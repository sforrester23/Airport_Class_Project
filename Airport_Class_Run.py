from People_Class import *
from Customer_Class import *
from Plane_Class import *
from Flight_Class import *
from Employee_Class import *

print('PASSENGER INFORMATION')
print('_____________________')
# CUSTOMER: first_name, last_name, age, email, phone_number, passport_number, flight_number, destination_airport, origin_airport
customer_1 = Customer('Sam', 'Forrester', 24, 'sforrester@spartaglobal.com', '07902105573', 505450007, 'BA0418', 'Antananrivo', 'Talinn')
print(customer_1.first_name)
print(customer_1.last_name)
print(customer_1.age)
print(customer_1.email)
print(customer_1.phone_number)
print(customer_1.passport_number)
print(customer_1.flight_number)
print(customer_1.destination_airport)
print(customer_1.origin_airport)
print(' ')
print('//////////////////////////////////////////')
print(' ')
print('FLIGHT INFORMATION')
print('_____________________')
# FLIGHT: model_number, capacity, flight_ID, destination, origin, departure_time, duration
flight_1 = Flight('BA0418', 'Antanarivo', 'Talinn', '9:30', 10)
print(flight_1.flight_ID)
print(flight_1.destination)
print(flight_1.origin)
print(flight_1.departure_time)
print(flight_1.duration)

# print('Please enter your Employee ID')
# input_employee_ID = input('')
# if input_employee_ID in


print('What would you like to do?')
print('Select 1 for list all flights.')
print('Select 2 for adding a passenger.')


# action = input('')

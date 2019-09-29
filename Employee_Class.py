from People_Class import *
from Passenger_Class import *

class Employee(People):
    def __init__(self, first_name, last_name, age, phone_number, employee_ID, job):
        super().__init__(first_name, last_name, age, phone_number)
        self.employee_ID = employee_ID
        self.job = job

        self.passenger_info = [] # Set up an empty list for passengers information
        self.employee_id_list = [] # Set up and empty list for employee ids to be stored

    # def add_passenger(self, customer_ID, flight_number):
    #     pass

    def passenger_add(self, passenger_f_name, passenger_l_name, passenger_age, passenger_phone, passenger_passport):

        passenger = Passenger(passenger_f_name, passenger_l_name, passenger_age, passenger_phone, passenger_passport)
        self.passenger_info.append(passenger)

    def employee_id_listing(self, employee_list):
        for index in range(len(employee_list)):
            self.employee_id_list.append(employee_list[index].employee_ID)
        return self.employee_id_list


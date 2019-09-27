from People_Class import *

class Employee(People):
    def __init__(self, first_name, last_name, age, email, phone_number, employee_ID, job):
        super().__init__(first_name, last_name, age, email, phone_number)
        self.employee_ID = employee_ID
        self.job = job

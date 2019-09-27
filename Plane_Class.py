from Flight_Class import *

class Plane(Flight):
# Define a class for all planes
    def __init__(self, flight_ID, destination, origin, departure_time, duration, model_number, capacity):
        # Define the attributes of planes
        super().__init__(flight_ID, destination, origin, departure_time, duration)
        self.model_number = model_number
        self.capacity = capacity


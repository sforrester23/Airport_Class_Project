from Plane_Class import *

class Flight(Plane):

    def __init__(self, model_number, capacity, flight_ID, destination, origin, departure_time, duration):
        super().__init__(model_number, capacity)
        self.flight_ID = flight_ID
        self.destination = destination
        self.origin = origin
        self.departure_time = departure_time
        self.duration = duration

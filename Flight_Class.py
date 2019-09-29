class Flight():

    def __init__(self, flight_ID, destination, origin, departure_time, duration):
        self.flight_ID = flight_ID
        self.destination = destination
        self.origin = origin
        self.departure_time = departure_time
        self.duration = duration
        # Set up an empty list for the the flight information and which passengers are on it
        self.passengers_on_flight = []

    def list_flights(self):
        return 'Flight {} from {} to {} is departing at {} and takes {} hours.'. format(self.flight_ID, self.origin, self.destination, self.departure_time, self.duration)

    def passenger_add_flight(self, passenger_f_name_add, passenger_l_name_add, passenger_passport_input):
        passenger_to_add = [passenger_f_name_add, passenger_l_name_add, passenger_passport_input]
        self.passengers_on_flight.append(passenger_to_add)



class Flight():

    def __init__(self, flight_ID, destination, origin, departure_time, duration):
        self.flight_ID = flight_ID
        self.destination = destination
        self.origin = origin
        self.departure_time = departure_time
        self.duration = duration

    def list_flights(self):
        return 'Flight {} from {} to {} is departing at {} and takes {} hours.'. format(self.flight_ID, self.origin, self.destination, self.departure_time, self.duration)



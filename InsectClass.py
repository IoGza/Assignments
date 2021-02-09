import random 

class Insect:
    
    def __init__(self):
        self.__legs = 4
        self.__wings = 2
    
    def flightLength(self):
        flight_mileage = random.randint(1,10)
        return flight_mileage

    # def getFlightMiles(self):
    #     return self.flight_mielage

    
import random 

class Insect:
    
    def __init__(self):
        self.__legs = 4
        self.__wings = 2
        self.__flight = 0
    
    def flightLength(self):
        self.flight = random.randint(1,10)
        return self.flight

    
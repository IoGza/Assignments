

class Car:
    def __init__(self,year_model,make,speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed = 0
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
    
    def __str__(self):
        return str(self.__year_model) +" " + self.__make +" " + "going " +str(self.__speed) +" MPH"
            



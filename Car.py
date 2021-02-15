from CarClass import Car

c = Car(2009,"Sedan",5)

print("This is a", c.__str__())

c.accelerate()
print("The car is going",c.get_speed(), "MPH")
c.accelerate()
print("The car is going",c.get_speed(), "MPH")
c.accelerate()
print("The car is going",c.get_speed(), "MPH")
c.accelerate()
print("The car is going",c.get_speed(), "MPH")
c.accelerate()
print("The car is going",c.get_speed(), "MPH")

print()

c.brake()
print("The car is currently brarking and is going", c.get_speed(), "MPH")
c.brake()
print("The car is currently brarking and is going", c.get_speed(), "MPH")
c.brake()
print("The car is currently brarking and is going", c.get_speed(), "MPH")
c.brake()
print("The car is currently brarking and is going", c.get_speed(), "MPH")
c.brake()
print("The car is currently brarking and is going", c.get_speed(), "MPH")
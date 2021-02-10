from StudentClass import Student
from datetime import datetime

d = datetime.today()

student = Student(892448163, "Evan McKinney", "07-01-1999", "Freshman")
# print(student.getStudent())

print(student.registerDate())
print(student.current_age(1999))

from datetime import datetime 
class Student:
    def __init__(self, StudentID, Name, dob, classification):
        self.StudentID = StudentID
        self.Name = Name
        self.dob = dob
        self.classification = classification

    def getStudent(self):
        fullStudent = "StudentID: " + str(self.StudentID) + "\n" + "Student Name: " + self.Name + "\n" + "Student DOB: " + self.dob +"\n" +"Student Class: " + self.classification
        return fullStudent

    def current_age(self):
        today = datetime.today()
        age = today.year - self.dob
        return today.year - dob.

    def registerDate(self):
        if self.classification == "Senior":
            print("Seniors register starting from 11/1 thru 11/3")
        elif self.classification == "Junior":
            print("Juniors register starting from 11/4 thru 11/6")
        elif self.classification == "Sophomore":
            print("Sophomores register starting from 11/7 thru 11/9")
        else:
            print("Freshman register starting from 11/10 thru 11/12")



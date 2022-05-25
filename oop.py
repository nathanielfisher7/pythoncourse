class Instructors:
    companyName = "BSU"

    def __init__(self, course,duration):  # All classes should have this
        self.course = course
        self.duration = duration

    def printInfo(self):
        print("My Company name is ", Instructors.companyName)


elearning = Instructors("Python for beginners", 1)

MLPR = Instructors("Machine Learning and Pattern Recognition", 4)
MLPR.course = "Machine Knowledge" #Modify course attribute value

elearning.printInfo()
MLPR.printInfo()

print(elearning.course)
print(elearning.duration)
print(MLPR.course)
#del MLPR.duration              #Delete the attribute
print(MLPR.duration)




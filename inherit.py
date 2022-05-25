class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


fisher = Person("Bob", "Jones")
fisher.printname()


class Lawyers(Person):
    def __init__(self, fname, lname,casetype):
        Person.__init__(self,fname,lname) # __init__ from the parent can still be used
        self.case_type = casetype
#        self.firstname = fname
#        self.lastname = lname

    def printinfo(self): # Can add new methods to the Child class
        print("Hello my name is", self.firstname, self.lastname,
              "I work in", self.case_type, "Justice")




happy_lawyers = Lawyers("Jack", "Smiley", "Criminal")
happy_lawyers.printname()
happy_lawyers.printinfo()
print(happy_lawyers.case_type)

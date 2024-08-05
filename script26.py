class Person:
    # properties and methods
    # properties
    first_name = None
    last_name = None
    age = None
    rollNo = None

    # methods
    def walk(self):
        print("I am walking")
    
    def talk(self):
        print("I am talking")

# object create 
chinmay = Person()
amol = Person()

# retriving the properties
print(chinmay.first_name)
print(chinmay.last_name)
print(chinmay.age)
print(chinmay.rollNo)
# calling on methods
chinmay.walk()
chinmay.talk()

# setting the properties values outside the class
chinmay.first_name = "chinmay"
chinmay.last_name = "deshpande"
chinmay.age = 34
chinmay.rollNo = 123

print(chinmay.first_name)
print(chinmay.last_name)
print(chinmay.age)
print(chinmay.rollNo)

# amol 

print(amol.first_name)
print(amol.last_name)
print(amol.age)
print(amol.rollNo)

amol.walk()
amol.talk()

amol.first_name = "amol"
amol.last_name = "rao"
amol.age = 23
amol.rollNo = 34

# setting the properties values at the time of object creation


class Person:
    # contructor
    def __init__(self,fn,ln,age,rollNo) :
        self.firstName = fn 
        self.lastName = ln 
        self.age = age
        self.rollNo = rollNo

    def display_name(self):
        print(self.firstName + self.lastName)

amol = Person("amol","rao",23,34)
print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)

# calling the method
amol.display_name()

chinmay = Person("chinmay","deshpande",34,55)
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.age)
print(chinmay.rollNo)

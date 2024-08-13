
# instance method
class Person:
    def __init__(self,fn,ln,ag):
        # instance variables
        self.firstName = fn 
        self.lastName = ln 
        self.age = ag
    # instance method to print fullName
    def displayName(self):
        print(self.firstName + self.lastName)
    # instance method to update age
    def updateAge(self,ag):
        self.age = ag


amol = Person("amol","rao",34)
print(amol.firstName)
print(amol.lastName)
print(amol.age)
amol.displayName()
amol.updateAge(23)
print(amol.age)

chinmay = Person("chinmay","deshpande",35)
chinmay.displayName()
chinmay.updateAge(34)
print(chinmay.age)

# class method 

class PersonB :
    # class level variable
    country = "india"
    def __init__(self,fn,ln,ag):
        # instance varibales
        self.firstName = fn 
        self.lastName = ln 
        self.age = ag 

    # instance method
    def displayName(self):
        print(self.firstName + self.lastName)

    # class method
    @classmethod
    def changeCountry(cls,cn):
        cls.country = "bharat"

amol  = PersonB("amol","rao",34)
chinmay = PersonB("chinmay","deshpande",56)
print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.country)
amol.country = "bharat"
print(chinmay.country)
print(amol.country)

PersonB.changeCountry('bharat')

sarika = PersonB("sarika","pansare",34)
print(sarika.country)

# static method
# static methods are called directly on className

class Counter:
    # class variable
    count = 0
    # constructor
    def __init__(self):
        Counter.count =   Counter.count  + 1

    @staticmethod
    def countObj():
        return Counter.count
    
amol = Counter()
chinmay = Counter()

e = Counter.countObj()
print(e)

        












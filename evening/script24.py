# method order resolution 


# single 
# multi-level 
# multiple  - ------ method order resolution
# herarchical

# Method order resolution 
class A(object):
    def methodOne(self):
        print("A class is called") #3 
        super().methodOne()

class B(object):
    def methodOne(self):
        print("B class is called")  # 5
        super().methodOne()

class C(object):
    def methodOne(self):
        print("Class C method called") # 6
        
class X(A,B):
    def methodOne(self):
       print("Class X is called") # 2
       super().methodOne()

class Y(B,C):
    def methodOne(self):
        print("Class Y is called")  # 4
        super().methodOne()

class P(X,Y,C):
    def methodOne(self):
       print("P is called")  # 1
       super().methodOne()

p = P()
p.methodOne()


# File handling

class Person:
    # class Level
    country = "India"
    count = 0

    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        Person.count =  Person.count


    # instance method
    def displayName(self):
        print(self.firstName+ self.lastName)

    @classmethod
    def changeCountry(cls):
        cls.country = "Bharat"

    @staticmethod
    def countObj():
        return Person.count
    
chinmay = Person("chinmay","deshpande")
print(chinmay.country)
Person.changeCountry()
print(chinmay.country)
Person.countObj()










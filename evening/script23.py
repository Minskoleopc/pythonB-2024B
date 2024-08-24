# duck typing 


class Human:
   def talk(self):
      print("hello hi ")

class Duck:
   def talk(self):
      print("quack quack")

class Dog:
   def bark(self):
      print("bow bow !")

def call_talk_other(obj):
    if hasattr(obj,"talk"):
       obj.talk()
    elif hasattr(obj,"bark"):
       obj.bark()

a = Human()
b = Duck()
c = Dog()

call_talk_other(a)
call_talk_other(b)
call_talk_other(c)

# overloading 
# same class , same method but different signature - overriding

class Calculator:
    # def addition(self,x,y):
    #   print(x+y)

    # def addition(self,x,y,z):
    #   print(x+y+z)

    # def addition(self,x,y,z,a):
    #   print(x+y+z+a)
    def addition(self,x= None, y = None , z = None , a = None):
        if x != None and y != None and z != None and a != None:
           print(x+y+z+a)
        elif x != None and y != None and z != None:
           print(x+y+z)
        elif x != None and y != None:
           print(x+y)
        
    
e = Calculator()
e.addition(12,3)
e.addition(12,3,3)
e.addition(12,3,3,4)
# overriding 
# same methodname , same signature but different class 
# has a relationship

class WorldBank:
    def save(self):
      print("I am from worlbank")

    def loan(self):
      print("i am loan from worldbank")
    

class SBI(WorldBank):
    def save(self):
      print("I am from SBI")

    def loan(self):
      print("i am loan from SBI")
    

e = SBI()
e.loan()
e.save()


# operator overloading
# print(1 + 1)
# print("hello "+ "world!")
# print(2 + "hello")
# # print(obj + obj)

print(1 + 1)
print("hello "+ "world")
# operator overloading

# class BookX:
#     def __init__(self,pages):
#        self.pages = pages
    
#     # addition operator overloaded to get result of adding object
#     def __add__(self,others):
#         return self.pages + others.pages

# class BookY:
#     def __init__(self,pages):
#       self.pages = pages
#     def __add__(self,others):
#         return self.pages + others.pages
    

# mahabharat = BookX(120)
# ramayan = BookY(240)

# print(mahabharat.pages + ramayan.pages)
# print(mahabharat+ramayan)
# print(ramayan+mahabharat)


class BookY:
    def __init__(self,pages):
      self.pages = pages

class BookX:
    def __init__(self,pages):
       self.pages = pages

    def __gt__(self,other):
       return self.pages > other.pages 


x = BookX(30)
y = BookY(25)
print(x.pages > y.pages)
print(x > y)

# __lt__ , ___sub__


# inheritance 

# single 
# multi-level
# herarchical 
# multiple

# polymorphism
# duck typing 
# overloading 
# overriding 
# operator overload


# abstraction

from abc import ABC , abstractmethod

class Demo(ABC):
   @abstractmethod
   def loan(self):
      pass
   
   def save(self):
      pass

class SBI(Demo):
   def loan(self):
      print("loan method")

class PNB(Demo):
   pass

a = SBI()












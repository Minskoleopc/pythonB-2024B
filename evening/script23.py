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
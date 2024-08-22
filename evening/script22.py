# polymorphism 

# poly - many 
# # morphism - of one thing

# class Human:
#     # method
#     def talk(self):
#         print("hello hi")

# class Duck:
#     # method
#     def talk(self):
#         print("Quack Quack")

# #function
# def call_talk(obj):
#     obj.talk()

# amol = Human()
# animalOne = Duck()

# call_talk(amol)
# call_talk(animalOne)


# program 2
class Human:
    def talk(self):
        print("hello hi")

class Duck:
    def talk(self):
        print("quack quack")

class Dog:
    def bark(self):
        print("bow bow")

# not correct way
# def call_talk(obj):
#     obj.talk()

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()

a = Human()
b = Duck()
c = Dog()

call_talk(c)
call_talk(b)
call_talk(a)







# program -1
# default argument
def add(x = 2, y = 4):
    print(x+y)
add(10)  # 14
add() # 6
add(11,4) # 15

# program - 2
# positional arguments 
def add(x,y):
    print(x-y)
add(y = 33,x = 5)

# program - 3
# *args
def addition(*args):
    print(args)
    total = 0 
    for x in args:
        total = total + x
    return total
q2 = addition(1,2,3,4,5,6)
print(q2)

# program - 4
# **kwargs 
def addCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs
q3  = addCity(firstName ="chinmay",lastName="Deshpande",rollNo = 23)
print(q3)

# program 5
birthYear = [1989,1990,1991,1992]
ages = [] # [35]
#[35,34,33,32]
for x in birthYear:
    age = 2024 - x
    ages.append(age)
print(ages)

# program 6
marks = [44,55,66,77,22,33,45,66]
above50 = []
for x in marks:
    if x > 50:
        above50.append(x)
print(above50)

# program 7
numbers = [11,22,33]
total = 0 
for x in numbers:
    total = total + x # 66
print(total)

#program 8
cities = ["pune","wardha","kolkata"]
for x in cities:
    print("welcome "+x)




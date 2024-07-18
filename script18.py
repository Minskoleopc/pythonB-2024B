
# functions

# program 1

# int as parameter and int as a return type 
def add(x,y):
    return x + y
e = add(12,3)
print(e)
print(type(e))

#float as a paramter and float as a return type 
def addE(x,y):
    return x + y
f = addE(12.5,11.5)
print(f)
print(type(f))

# boolean as a parameter and boolean as a return type 
def canDrive(age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True
    else:
        return False

e = canDrive(17,True)
print(e)

# string as a parameter and string as a return type 
def greet(name):
    return "welcome "+name+" !"
f = greet("chinmay")
print(f)

# list as parameter and list as a return type 
cities = ["pune","mumbai","banglore","kolkata","chennai"]
def addCity(lst):
    lst.append("nagpur")
    return lst
f = addCity(cities)
print(f)

# dict as a parameter and dictionary as a return type 
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
}

def addLangauge(d):
    d.update({"language":"marathi"})
    return d
g = addLangauge(info)
print(g)

# tuple as parameter and tuple as return type 
tupC = (11,22,33)
def addElementToTuple(tupA):
    tupA = list(tupA)
    tupA.append(44)
    tupA = tuple(tupA)
    return tupA
t = addElementToTuple(tupC)
print(t)

# set as paramter and set as a return 
setA = {11,22,33}
def addValToSet(setP):
    setP.add(44)
    return setP
e = addValToSet(setA)
print(e)

# next 3 days ----- 7:30 pm 
# list , tuple , dictionary , set , string











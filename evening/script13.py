# # int 
# # int as a parameter and int as a return type 
# def add(x,y):
#     return x + y

# e = add(12,3)
# print(e)
# print(type(e))

# # float 
# # float value as a parameter and float value as return type 
# def addB(x,y):
#     return x + y
# f = addB(12.4,13.4)
# print(f)
# print(type(f))

# boolean value as a parameter and boolean value as a return type
# boolean 
print("hello")
def CanDrive(age, hvV):
    if age >= 18 and hvV:
        return True
    else:
        return False
f = CanDrive(13,True)
print(f)

# string 
# string as a parameter and string as a return type 
def greet(word):
    return "hello "+ word
g  = greet("chinmay")
print(g)

# list 
# list a parameter and list a return type 

names = ["chinmay","shirish","rahul","sachin"]
def addE(lst):
    lst.append("samay")
    return lst
j = addE(names)
print(j)

# dict 
# dict as a parameter and dict as a return type 
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":344
}

def addEtoD(information):
    information['language'] = "marathi"
    information.update({"city":"pune"})
    return information
h = addEtoD(info)
print(h)

# tuple
# tuple as a parameter and tuple as a return type
tupleA = (12,34)
print(type(tupleA))
def addE(tupB):
    tupB = list(tupB)
    tupB.append(56)
    tupB = tuple(tupB)
    return tupB
l = addE(tupleA)
print(l)

# set 
# set as a parameter and set as a return type 
g = {11,22,33,44,55,66}
def addV(setB):
    setB.add(35)
    return setB
w = addV(g)
print(w)



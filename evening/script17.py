
# function 
# program 1
# def - keyword
# add - function name 
# x,y - parameters
# return - keyword
#add(12,3) - call , 12,3 ===> arguments
# def add(x,y):
#     return x + y

# e = add(12,3)
# print(e)


# program 1
# def add(x,y):
#     return x + y

# add()
def add(x = 1,y = 3):
    return x + y

print(add())
print(add(1,22))
print(add(2))

# positional arguments 
def sub(x,y):
    return x - y
f = sub(y =3,x = 4)

# *args
from functools import reduce
def addition(*args):
    return reduce(lambda acc,el:acc+el,args)
f = addition(12,7,4,5,6,7,8)
print(f)


def additionE(*args):
    print(args)
    e = list(args)
    total = 0 
    for x in e:
        total = total + x
    return total
e = additionE(12,33,4,5,6)
print(e)


# program 5
# *kwargs
def addCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs

g = addCity(firstName = "chinmay" , lastName = "deshpande", age = 45)
print(g)











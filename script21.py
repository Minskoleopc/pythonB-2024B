#add = lambda x,y:x+y
#lambda - keyword
#x,y - parameter
#x+y - return type 
#add

# program 1
# function as a parameter to another function 
add = lambda x,y:x+y
def addition(fn,x,y):
    #fn = lambda x,y:x+y
    # x = 12
    # y = 3

    e = fn(x,y)
    return e

q1 = addition(add,12,3)
print(q1)

# program 2
# function as a return type
def subtraction():
    return lambda x,y:x-y
sub = subtraction()
print(sub)

#sub = lambda x,y:x-y
e = sub(12,4)
print(e)

# program 3
# default parameter
def multiplication(x=4,y=2):
    print(x*y)
multiplication(12,3)
multiplication()
multiplication(10)

#program 4
#positional argument 
def division(x,y):
    print(x/y)
division(y=8,x=16)

# program5
def addAll(*args):
    print(args) # (12,4,3,4)
    total = 0
    for x in args:
        total = total + x
    return total
q = addAll(12,4,3,4)
print(q)

# 12,4,3,4,5,6,7,8,9,4,6,7,8,5,6,7,8,4 ------> (12,4,3,4,5,6,7,8,9,4,6,7,8,5,6,7,8,4)

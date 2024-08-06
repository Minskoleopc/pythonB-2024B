# functions 


# function as a parmeter to another function 




# function as return type 


# lamdba function 


# expression
def add(x,y):
    return x + y
e = add(12,4)
print(e)

# lambda --- keyword
# x , y  --- parameter 
# x + y  --- return type 


add = lambda x,y:x+y
e = add(34,5)
print(e)

# program 2

x = 10
print(x)

f = lambda x : x * x
#print(f)
f(3)


# program 3
# function as parameter to another 

sub = lambda x,y:x-y
def subtraction(fn,x,y):
    # fn = lambda x,y:x-y
    # x  = 40
    # y = 20
    e = fn(x,y)
    return e
e2 = subtraction(sub,40,20)
print(e2)



# program 4
mul = lambda x,y:x*y
def multiplication(fn,x,y):
    # fn = lambda x,y:x*y
    # x = 23
    # y = 2

    m = fn(x,y)
    return m
m2 = multiplication(mul,23,2)
print(m2)


# function as a return type 
def division():
    return lambda x,y:x/y

e = division()
#e  = lambda x,y:x/y
print(e)
print(e(12,4))














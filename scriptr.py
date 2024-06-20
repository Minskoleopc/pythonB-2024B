# day1
x = 10
print(x)
x = 400
print(x)


# Arithmetic operation

a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

q = 9
r = 3

print(q+r)
print(q-r)
print(q*r)
print(q/r)
print(q%r)

# function 

def Cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)

Cal(12,3)
Cal(23,4)

# day 2

# function without paremeter and without return type 
def add():
    print(9+9)
add()
add()
add()
add()

# function with parameter and without return type 
def addA(x,y):
    print(x+y)

addA(12,4)
addA(12,1)
addA(12,7)

# function with parameter and with return
def addC(x,y):
    return x + y
e = addC(12,4)
print(e)
print(e+e)
print(e/4)
print(e * 0.10)

# day 3

# introvert    extrovert
# calm          loud
# less social   more social
# less outing   more outing


# human 
# properties - color gender height weight
# methods    - walk() , talk()

#vehicle 
#properties - color ,regno , companyName , type , model
#methods - start(), stop()

#Bank acc
#properties - bal ,  accName , accNumber , IFSC code
#method - withdrawl() , deposit()


a = 10
print(a)
print(type(a))
# 10,-10,0

b = 100.7
print(b)
print(type(b))
# 19.9 , -18.8, 0.00

c = True
print(c)
print(type(c))
# True or False

d = 'chinmay'
print(d)
print(type(d))
#'chinmay',"!",'1',"a","A"," ","#!@dsads"


# comparison 
# entity < entity --- boolean ---- True or False 

# < , > , <= , >= , != ,== 

print(6 > 3)
print(6 < 3)
print(6 == 3)
print(6 != 3)
print(6 >= 3)
print(6 <= 3)
print(7 >= 7)
print(7 <= 7)

# logical operator 
# and or not


# and
# True  and True  ----- True 
# False and True  ----- False
# True  and False ----- False
# False and False ----- False

print(5 == 5 and 6 == 6)
print(5 != 5 and 6 == 6)
print(5 == 5 and 6 != 6)
print(5 != 5 and 6 != 6)



#or
# True   or  True  ------ True 
# False  or  True  ------ True
# True   or  False  ----- True
# False  or  False  ----- False


print(5 == 5 or 6 == 6)
print(5 != 5 or 6 == 6)
print(5 == 5 or 6 != 6)
print(5 != 5 or 6 != 6)


# not True  --- False
# not False --- True

print(not (7 == 7))
print(not (7 != 7))





























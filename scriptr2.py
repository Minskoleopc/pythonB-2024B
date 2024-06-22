# day 1
x = 10
print(x)
print(type(x))

x = 100
print(x)
x = 800
print(x)

# program 2
# Arithmetic operation 
# + ,- ,* , / , %
# % remainder 

print(23 % 7)

j = 8
k = 4

print(j+k)
print(j-k)
print(j*k)
print(j/k)
print(j%k)

s = 6
t = 3

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)


# function 

def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
Calculator(12,3)
Calculator(4,2)

# day 2

# function with parameter and without return 

def add():
    print(9+9)
add()
add()
add()
add()

# function with parameter and without return type
def addB(x,y):
    print(x+y)
addB(3,4)

# function with parameter and with return type 
def addC(x,y):
    return x + y
e = addC(12,4)
print(e)
print(e+e)
print(e/4)
print(e * 0.10)

# type 

# introvert    extrovert
# calm            loud
# less outing     more outing
# less social     more social



# Human - amol 
# propeties ---> color ,gender , weight , height
# Method - sleep() walk() talk()

# Vehicle
# Properties ---> color , model , type , regNo
# Method - start() , stop()

# Bank acc
# Properties - accNO , accName , accType 
# Methods - deposit() , withdrawl()


a = 10
print(a)
print(type(a))
#10,-10,0

b = 10.5
print(b)
print(type(b))
# 12.4 , -12.5 , 0.4

c = True
print(c)
print(type(c))
# True False

d = "chinmay"
print(d)
print(type(d))
# "A", "1","!", " ", "12ad#!@#"


# comparion operator 
# < , > ,<= , >= ,!= ,==
# entity < entity  ---- boolean

print(4 > 2)
print(4 < 2)
print(4 == 2)
print(4 != 2)
print(4 == 4)
print(4 >= 4)
print(4 <= 4)
print(4 != 4)
print(4 >= 3)
print(4 <= 3)


# Logical operator
# and 

#True   and   True  ----- True
#True   and   False ----- False
#False  and   True  ----- Fasle
#False  and   False ----- False  

print(6 == 6 and 7 == 7)
print(6 != 6 and 7 == 7)
print(6 == 6 and 7 != 7)
print(6 != 6 and 7 != 7)

# or 

#True   or   True  ----- True
#True   or   False ----- True
#False  or   True  ----- True
#False  or   False ----- False  

print(6 == 6 or 7 == 7)
print(6 != 6 or 7 == 7)
print(6 == 6 or 7 != 7)
print(6 != 6 or 7 != 7)

# not
# not True -- False
# not False - True

print(not(7 == 7))
print(not(7 != 7))























# list comprehension 
# return type will always be []

birthYear = [1989,1990,1991,1992] 
ages = [] # [35,34,33,32]

for x in birthYear:
    age = 2024 - x
    ages.append(age)
print(ages)

e1 = list(map(lambda x : 2024-x,birthYear))
print(e1)

#[expression:loop:condition]
e2 = [2024 - x for x in birthYear]
print(e2)

# program 2
numbers = [11,22,33,44,55]
e2 = [x + 10 for x in numbers]
print(e2)

#program 3 
marks = [44,55,66,77,88,55,44,88]
above60 = []

for x in marks:
    if x > 60:
        above60.append(x)
print(above60)
e3 = list(filter(lambda x :x >60,marks))
print(e3)

#[expression:loop:condition]
e3 = [x for x in marks if x > 60]
print(e3)

# program 3

numberB = [22,33,44,55]
# ["even","odd","even","odd"]

status = []
for  x in numberB:
    if x % 2 == 0:
        status.append("even")
    else:
         status.append("odd")
print(status)


#[tenary:loop]

# e2 = ["even" for x in numberB if x%2 == 0 ]
# print(e2)

# user ternary if more than one reference 
e4 = ["even" if x % 2 == 0 else "old" for x in numberB]
print(e4)









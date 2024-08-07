# program 1
birthYear = [2002,2001,2000,1999]
ages = []
for  x in birthYear:
    print(2024 - x)
    age = 2024 - x
    ages.append(age)
print(ages)
print(list(map(lambda x:2024-x,birthYear)))

# program 2
numbers = [12,33,44,55,66]
e = list(map(lambda x : x + 10,numbers))
print(e)


# program 3
# filter 
marks = [77,33,44,55,22,44,11,22]
above50 = []
for x in marks:
    if x > 50:
        above50.append(x)
print(above50)
f = list(filter(lambda x : x  > 50,marks))
print(f)

#program 4
transactions = [11,22,33,44,55,-44,55,-66,77,44,55,66]
deposit = list(filter(lambda x:x > 0 , transactions))
print(deposit)
withdrawl = list(filter(lambda x:x < 0 , transactions))
print(withdrawl)

# program 5
listA = [11,22,33]
total = 0
for x in listA:
    total = total + x
print(total)

from functools import reduce
f = reduce(lambda acc,el:acc + el,listA)
print(f)

# list comprehension 



# optional parameter , default parameter , positional arguments , args , kwargs





















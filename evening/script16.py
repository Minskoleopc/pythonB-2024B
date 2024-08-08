birthYear = [2019,2020,2021,2023]
ages  = []

for x in birthYear:
    ag = 2024 - x
    ages.append(ag)
print(ages)

e = list(map(lambda x:2024-x,birthYear))
print(e)

# list comprehension
#[expression:loop:condition(only one condition)]
e2 = [2024 - x for x in birthYear]
print(e2)

# program 2
transactions = [9900,-1923,8000,4455,6666,-777,888,-444]

deposit = []
withdrawl =[]
for x in transactions:
    if x > 0:
        deposit.append(x)

print(deposit)

for x in transactions:
    if x < 0:
        withdrawl.append(x)

print(withdrawl)

deposit = list(filter(lambda x : x > 0 ,transactions))
withdrawl = list(filter(lambda x : x < 0 ,transactions))

deposit = [x for x in transactions if x > 0]
print(deposit)

withdrawl = [x for x in transactions if x < 0]
print(withdrawl)


# program 4 
numbers = [11,22,33]
total = 0 

for x in numbers:
    total = total + x 
print(total)

from functools import reduce
print(reduce(lambda acc, el:acc+el,numbers))

numbersB = [11,22,33,44]
#["odd","even","odd","even"]

evenOdd = []

for x in numbersB:
    if x % 2 == 0:
        evenOdd.append('even')
    else:
        evenOdd.append('odd')
print(evenOdd)

e2 = ["even" if x % 2 == 0 else "odd" for x in numbersB]
print(e2)


print([x * 2 for x in range(1,11)])




















# map , filter , reduuce 
# for 
# list comprehension -list


birthYear = [1989,1990,1992,1992]
ages = []

for x in birthYear:
   age =  2024 - x
   ages.append(age)
print(ages)

e = list(map(lambda x: 2024 - x,birthYear))
print(e)

#[expression : loop : condition(one condition)]
#[ternary[multiple contion]:loop]
print([2024 - x for x in birthYear])

# program 2
marks = [33,44,55,66,22,33,56]
above50 = []
for x in marks:
   if x >  50:
      above50.append(x)
print(above50)
      
above502 = list(filter(lambda x : x > 50,marks))
print(above502)
above503 = [x for x in marks if x > 50]

# program 3
numbers = [11,22,33,44,66,33]
evenOdd = []
for x in numbers:
   if x % 2 == 0:
      evenOdd.append("even")
   else:
      evenOdd.append("odd")
print(evenOdd)
print(list(map(lambda x:"even" if x % 2==0 else "odd",numbers)))
print(["even" if x % 2 == 0 else "odd" for x in numbers])

# program 4
numbersB  = [11,22,33]
total = 0
for x in numbersB:
   total = total + x
print(total)

from functools import reduce
print(reduce(lambda acc,el:acc+el,numbersB))



      
      







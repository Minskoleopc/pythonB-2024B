# list - methods -- loop -- CRUD
#          0   1  2 3  4
numbers = [11,22,33,44,55]
print(numbers)
# retrive 
print(numbers[0])
print(numbers[1])

# update 
numbers[0] = 111
print(numbers)

# add 
numbers.append(66)
print(numbers)

#remove
numbers.remove(66)
print(numbers)


# program 2
# list 
#           0         1         2          3       4
names = ["chinmay","sarika","shraddha","ramesh","suresh"]
print(type(names))

# loop 
# range()
print(len(names))
e = len(names)
print(e)

for x in range(len(names)):
    #print(x)
    print(names[x])

# program 2
#          0         1       2        3
fruits = ["apple","mango","grapes","banana"]
print(fruits)

for x in range(len(fruits)):
    #print(x)
    print(fruits[x])

for x in range(len(fruits)-1,-1,-1):
    #print(x)
    print(fruits[x])

# without range()
fruits = ["apple","mango","grapes","banana"]
for x in fruits:
    print(x)

# while loop
#           0        1       2       3
fruits = ["apple","mango","grapes","banana"]
i1 = 0 
while(i1 < 4):
    print(fruits[i1])
    i1 = i1 + 1








# tuple 

# dictionary

# set

# string  
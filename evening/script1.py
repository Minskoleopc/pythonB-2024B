print(1)
print(2)
print(3)
print(4)
print(5)

#range(startIndex,endIndex(not included),stepSize)
# bydefault start - zero

# print 0 to 2
for x in range(3):
    print(x)

# program 2
for x in range(1,3):
    print(x)

for x in range(1,4):
    print(x)

for x in range(1,4):
    print("hello")

# program 3
for x in range(1,6):
    print(x)

# print table of 3
for x in range(1,11):
    print(x * 2)

# print table of 2 using step size 
# by default stepsize is 1 

for x in range(1,11,2):
    print(x)

for x in range(2,21,2):
    print(x)

for x in range(3,31,3):
    print(x)

# program 4
# print 5 to 1
for x in range(5,0,-1):
    print(x)

# print table of 5 in reverse
for x in range(50,0,-5):
    print(x)

for x in range(30,0,-3):
    print(x)


# break statement with for loop
for x in range(5):
    if x == 2:
        break
    print(x)

for x in range(6):
    print(x)
    if x == 3:
        break

for x in range(10,5,-1):
    if x == 8:
        break
    print(x)


















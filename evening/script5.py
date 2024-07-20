#           0          1        2
names = ["chinmay","shirish","rohit"]
print(type(names))
print(names[0])

# retrive 
print(names[0])

# update 
names[0] = "tanmay"
print(names)
# add 
names.append("vijeet")
print(names)
# delete 
names.remove("tanmay")
print(names)
# element avaible ?
print('rohit' in names)

fruits = ["apple","mango","banana"]
# loop - for - range 
for x in range(3):
    print(fruits[x])

# for without range 
for x in fruits:
    print(x)

# while 
y = 0
while( y < len(fruits)):
    print(y)
    print(fruits[y])
    y = y + 1

# how many elements in list?
#           0       1          2        3          4
cities = ["pune","mumbai","banglore","kolkata","chennai"]
f = len(cities)
print(f)

# append()
cities.append("wardha")
print(cities)
#   0        1         2           3          4          5
#['pune', 'mumbai', 'banaglore', 'kolkata', 'chennai', 'wardha']
#pop()
cities.pop()
print(cities)
cities.pop(2)
print(cities)
cities.remove("chennai")
print(cities)
# append() , pop() , pop(2), remove()

# program 2
# insert()
#            0       1       2        3
fruits = ["apple","mango","banana","grapes"]
fruits.insert(3,"papaya")
print(fruits)

# program 3
# count()
fruits = ["apple","mango","banana","grapes","apple"]
f = fruits.count("apple")
print(f)

# extend()
fruits.extend(['orange',"cherry","chikoo"])
print(fruits)

# program 4
#                0          1        2          3
vegetables = ["brinjal","potato","cabbage","cauliflower"]
vegetables.sort()
print(vegetables)

# program 5
#['brinjal', 'cabbage', 'cauliflower', 'potato']
vegetables.reverse()
print(vegetables)

vegetables.clear()
print(vegetables)

# program 6
#                0          1        2         3
vegetables = ["brinjal","potato","cabbage","cauliflower"]
e = vegetables.index("potato")
print(e)




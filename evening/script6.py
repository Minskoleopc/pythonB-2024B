#           0          1      2
listA = ["chinmay","rahul","mayur"]
# listB = listA
# listB[0] = "tanmay"
# print(listB)
# print(listA)

listB = listA.copy()
listB[0] = "tanmay"
print(listB)
print(listA)


# methods 
#             0      1       2
# fruits = ["apple","mango","banana"]
# fruits.append("papaya")
# print(fruits)

# fruits.insert(2,"cherry")
# print(fruits)

# fruits.pop()
# fruits.pop(2)
# fruits.remove("apple")
# print(fruits)

fruits = ["apple","mango","banana","apple"]
# fruits.sort()
# fruits.reverse()
# fruits.extend(['chikoo',"papapya"])
# print(fruits)

# fruits.clear()
# print(fruits)

e = fruits.count("apple")
print(e)

f = fruits.index("mango")
print(f)


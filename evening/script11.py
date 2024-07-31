# int , float , string , boolean ,list , tuple , dict

# set 

setA = {11,22,33,44,55,66,66}
print(setA)
# set stores the value by index ??
#print(setA[0]) No
# how to define set ?

setB = {"chinmay","ram","sham","laksman","sachin"}
print(setB)

# how to find value available in set ?
setB = {"chinmay","ram","sham","laksman","sachin"}
print("chinmay" in setB)
print("Chinmay" in setB)
# how loop over set ?

setE = {"pune","mumbai","banglore","kolkata","chennai"}
for x in setE:
    print(x)


#  dict - No , tuple - Yes , List - Yes , String - Yes
#  set - No 

# does set allows you to store duplicate values?

listA = ["chinmay","chinmay","chinmay"]
print(listA)

tupleA = ("chinmay","chinmay","chinmay")
print(tupleA)

setA = {"chinmay","chinmay","chinmay"}

dictA  = {
    "age":12,
    "age2":13
}
print(dictA)


# how to find the length of set
setD = {11,22,33,44,55}
print(len(setD))

# methods 
# add()
setA = {11,22,33,44,55}
setA.add(66)
print(setA)

# clear()
setA.clear()
print(setA)


setF = {11,22,33,44,55}
# setG = setF
# setG.add(4444)
# print(setG)
# print(setF)
setE = setF.copy()
setE.add(555555)
print(setE)
print(setF)



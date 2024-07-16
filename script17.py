# sets in python
a = 10
print(a)
print(type(a))

b = 12.3
print(b)
print(type(b))

c = "chinmay"
print(c)
print(type(c))

d = [11,22,33,44]
print(d)
print(type(d))

e = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
print(e)
print(type(e))

f = (12,3,4,5)
print(f)
print(type(f))

# set
# how to define a set 
setA = {11,22,33,44,55,66,55}
print(setA)

# does set stores the value by index ?
setB = {44,55,66,77,33,44,55}
print(setB)
#print(setB[0])

# element available in set ??
print(666 in setB)

# for 
setC = {"chinmay","ram","satish","jayant","ramesh"}
print(setC)
for item in setC:
    print(item)

setD = {11,22,33,44}
print(len(setD))


# program 2
# Set --- object ---- methods 

# program 1
setA = {11,22,33}
setA.add(44)
print(setA)

#program2

setA = {11,22,33}
setA.pop()
print(setA)

setC = {11,22,33,44,55}
setC.remove(44)
print(setC)

setD = {"chinmay","ninad","raj","satish"}
setD.remove("ninad")
setD.pop()
print(setD)
print(setD)

# program 3
setE = {"chinmay","satish","ram","ramesh"}
# print(setE)
# setF = setE
# setF.remove("chinmay")
# print(setF)
# print(setE)
setF = setE.copy()
setF.remove("chinmay")
print(setF)
print(setE)

# program 4
setH = {11,22,33,44,55,66,77,88,99,100} 
setH.clear()
print(setH)

#program5
setG = {33,44,55,66,77}
setG.update([99,200,1333])
setG.update((222,333,4444))
print(setG)
# queries 















































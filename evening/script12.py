
# program 1
setA = {11,22,33}
setB = {22,33,44}
setC = setA.union(setB)
print(setC)

# program 2
setC = {11,22,33,22}
setD = {44,55,66,11,33}
e = setC.intersection(setD)
print(e)
setC.intersection_update(setD)
print(setC)

# program 3

setG = {44,55,66}
setH = {66,77,88}

print(setG.difference(setH))
print(setH.difference(setG))

# setG.difference_update(setH)
# print(setG)

setH.difference_update(setG)
print(setH)

# program 4

setK = {11,22,33,44}
setH = {44,55,33}

print(setK.symmetric_difference(setH))
setK.symmetric_difference_update(setH)
print(setK)

# program 5
setH1 = {66,77}
setH2  = {88,55,33}
#print(setH1.isdisjoint(setH2))

setH1.update([122,33,44])
print(setH1)

# program 6

setN = {11,22}
setM = {11,22,33,66}

print(setN.issubset(setM))
print(setM.issuperset(setN))
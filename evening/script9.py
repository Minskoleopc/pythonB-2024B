# info = {
#     "firstName":"chinmay",
#     "lastName":"deshpande",
#     "age":23
# }
# print(info)
# print(len(info))

# print(info['age'])
# e = info.get('lastName')
# print(e)

# #clear()
# info.clear()
# print(info)


# # program 2
# info = {
#     "firstName":"chinmay",
#     "lastName":"deshpande",
#     "age":23
# }
# info2 = info.copy()
# info2['age']= 24
# print(info2)
# print(info)
# info.update({"city":"pune"})
# print(info)

# info2.popitem()
# info2.pop("lastName")
# print(info2)

# # program 2
# info = {
#     "firstName":"chinmay",
#     "lastName":"deshpande",
#     "age":23
# }

# e = dict.fromkeys(["fn","ln","ag"])
# print(e)
# e.setdefault('lastName',"Dani")
# e.setdefault('city',"pune")
# print(e)


# vehicle  = {
#     "color":"red",
#     "type":"sedane",
#     "regNo":123
# }

# for x in vehicle:
#     print(x,vehicle[x])

# for x in vehicle.values():
#     print(x)

# for x in vehicle.keys():
#     print(x)

# for x,y in vehicle.items():
#     print(x,y)


g = (1,2)
print(g)
print(type(g))

# does tuple stores the value by index ?
print(g[0])

# program 3
#            0           1      2      3
tupleC = ("chinmay","shirish","ram","ramesh")
tupleC = "chinmay","shirish","ram","ramesh"
print(type(tupleC))
print("chinmay" in tupleC)
print(len(tupleC))

#range()
for x in range(len(tupleC)):
    #print(x)
    print(tupleC[x])

#without range()
for x in tupleC:
    print(x)

#while loop
i1 = 0
while(i1 < len(tupleC)):
    print(tupleC[i1])
    i1 = i1 + 1


tupleC = "chinmay","shirish","ram","ramesh"
# tupleC[0] = "tanmay"
tupleC = list(tupleC)
tupleC.append("sarika")
tupleC = tuple(tupleC)
print(tupleC)

tupleC = ("chinmay","shirish","ram","ramesh","chinmay")
f = tupleC.count("chinmay")
print(f)

g = tupleC.index("shirish")
print(g)

# unpacking 
g = (11,22,33,44)
a ,b,c,d = g
print(a)
print(b)
print(c)
print(d)










# #          0        1      2     3
# names = ["amol","satish","ram","sham"]
# print(names)
# # retrive 
# print(names[0])
# # add 
# names.append("sarika")
# names.insert(2,"hello")
# #update 
# names[0] = "ninad"
# # delete
# names.pop()
# names.pop(1)
# names.remove("amol")

#          0            1     2   3
info = ["chinmay","deshpande",77,66]
print(info)
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":77,
    "rollNo":66
}
print(info)
print(type(info))

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":77,
    "rollNo":66,
    "lastName":"dani"
}
# retrive 
print(info['firstName'])
print(info['lastName'])
# update
info['firstName'] = "tanmay"
print(info)
# does dictionary stores duplicate key-value / property-value?
# how to find specfic key/ property exist in dictionary
print("age" in info)
print("city" in info)
# add the property
info['city'] = "pune"
print(info)
# how to loop over dictionary 
vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}
print(vehicle)
for key in vehicle:
    print(key,vehicle[key])

# how to find total number of properties in dictionary
q2 = len(vehicle)
print(q2)



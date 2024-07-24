# dict 

info = {
    # key:value 
    # property:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "age":23
}

# program 1
# print(info["firstName"])
# info["firstName"] = "tanmay"
# print(info)
# print("firstName" in info)
# print(len(info))
# for key in info:
#     print(key,info[key])

# methods 
vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}


# print(type(vehicle))
# print(vehicle['color'])
# q1 = vehicle.get('regNo')
# print(q1)

# program  1
print("hello")
#print(vehicle['Color'])
print(vehicle.get("Color"))
print("bye")


# program 2
student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23
}
print(student)

# student.clear()
# print(student)

# copy()
# student2 = student
# student2['age'] = 47
# print(student)
# print(student2)

# student2 = student.copy()
# student2['age'] = 47
# print(student)
# print(student2)

# program 4

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    'rollNo':47
}

student.pop("firstName")
print(student)

student.popitem()
print(student)

# program 5
student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    'rollNo':47
}

student.update({"city":"pune"})
print(student)

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    'rollNo':47
}

# for x in student.values():
#     print(x)

# for x in student.keys():
#     print(x)

# for x,y in student.items():
#     print(x,y)

# program 6
student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    'rollNo':47
}

e = student.setdefault('langauge',"marathi")
print(e)
print(student)

# program 7
e = dict.fromkeys(["color","gender","firstName","lastName","height"])
print(e)

# 5 dict ------ tuple
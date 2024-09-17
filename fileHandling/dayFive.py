# python object object ====> binary ------serialization
# binary object        ====> python object ------- deserialization

# class Employee:
#     def __init__(self,fn,ln) -> None:
#         self.firstName = fn 
#         self.lastName = ln 

#     def display_name(self):
#         print(self.firstName + self.lastName)


# import pickle 
# f = open('emp2.dat','wb')
# n = int(input('Enter the number of student'))
# for x in range(n):
#     fn = input('please enter firstName')
#     ln = input('please enter lastName ')
#     e = Employee(fn,ln)
#     pickle.dump(e,f)
# f.close()


# f = open('emp2.dat','rb')
# while True:
#     try:
#         e = pickle.load(f)
#         e.display_name()
#     except EOFError:
#         print('end of the file')
#         break

# # try except
# print("hello")
# try:
#     print(10/0)
# except:
#     print("error occur....")
# print("bye")


#chinmay sarika poorva rahul sham rohit
#'chinmay    '
#'rohit      '
#'deepak     '

# reclen = 10

# with open('name.bin',"wb") as f:
#     n = int(input('enter the number of name'))
#     for x in range(n):
#         name = input('enter the names :') # chinmay  sham
#         name = name + ((reclen - len(name))) * " " # 'chinmay   '
#         name = name.encode()
#         f.write(name)

# program 1
# reclen = 10
# with open('cities.bin','wb') as f:
#     n = int(input('please enter the number of cities'))
#     for i in range(n):
#         city = input('please enter a city name ...') # "pune"
#         city = city + (reclen - len(city)) * " " #"pune      "
#         city = city.encode()
#         f.write(city)

import os
reclen = 10
position = 0
size = os.path.getsize('cities.bin') # 30
n = int(size/reclen)
with open('cities.bin','rb')as f:
    for i in range(n):
        f.seek(0)
        str = f.read(10)
        str = str.decode()
        print(str)
        position = position+ reclen 
        

# search the city name in file

# replace the name 

# delete the record































# # inheritance 

# class Student:
#     firstName = "chinmay"
#     lastName = "deshpande"
#     adharCard = 123

#     def displayName(self):
#         print(self.firstName + self.lastName)


# class Teacher:
#     firstName = "chinmay"
#     lastName = "deshpande"
#     adharCard = 123
#     salary = 123123

#     def displayName(self):
#         print(self.firstName + self.lastName)
    
#     def displaySalary(self):
#         print(self.salary)
        
# amolT = Teacher()
# print(amolT.firstName)
# print(amolT.lastName)
# print(amolT.adharCard)
# print(amolT.salary)
# amolT.displayName()
# amolT.displaySalary()

# amolS = Student() 
# print(amolS.firstName)
# print(amolS.lastName)
# print(amolS.adharCard)



class Student:
    firstName = "chinmay"
    lastName = "deshpande"
    adharCard = 123

    def displayName(self):
        print(self.firstName + self.lastName)



class Teacher(Student):
    salary = 123123    
    def displaySalary(self):
        print(self.salary)

amolT2 = Teacher()
print(amolT2.firstName)
print(amolT2.lastName)
print(amolT2.adharCard)
print(amolT2.salary)

amolT2.displayName()
amolT2.displaySalary()

# program 1
# single inheritance - parent contructor , child no contructor
# single inheritance - parent contructor , child  contructor
# multi-level
# herarchical 
# multiple

# 7 pm
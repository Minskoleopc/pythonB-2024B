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


# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     salary = 1000
#     def displaySalary(self):
#         print(self.salary)

# amol = Teacher("amol","rao")
# print(amol.firstName)
# print(amol.lastName)
# print(amol.salary)
# amol.displayName()
# amol.displaySalary()

# single inheritance
# program 2
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,salary):
        super().__init__(fn,ln)
        self.salary = salary
    
    def displaySalary(self):
        print(self.salary)

amolT = Teacher("amolT","raoT",2444)
print(amolT.firstName)
print(amolT.lastName)
print(amolT.salary)
amolT.displayName()
amolT.displaySalary()


# program 3
# multilevel

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)


class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
    
    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)

chinmay = Son("manohar","deshpande","shirish","chinmay")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)
print(chinmay.fname)

chinmay.displayFName()
chinmay.displayName()
chinmay.displaySname()






























# 7 pm
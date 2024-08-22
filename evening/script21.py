#single  inheritance

class Student:
    def __init__(self,fn,ln):
        self.firstName  = fn 
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)


class Teacher(Student):
    def __init__(self, fn, ln,salary):
        super().__init__(fn, ln)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","rao",2344)
print(amol.firstName)
print(amol.lastName)
print(amol.salary)
amol.displayName()
amol.displaySalary()

#multilevel inheritance

class GrandFather:

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)


class Father(GrandFather):
    def __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFname(self):
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
print(chinmay.fname)
print(chinmay.lastName)

chinmay.displayName()
chinmay.displayFname()
chinmay.displaySname()


#herarchial inheritance



class Mother:
    def __init__(self,fn,ln) -> None:
        self.firstName = fn 
        self.lastName = ln

    def displayMname(self):
        print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
     def __init__(self, fn, ln,ddn):
        super().__init__(fn, ln)
        self.dname = ddn

     def displayDname(self):
        print(self.dname + self.lastName)


chinmay = Son("kanchan","deshpande","chinmay")
gauri = Daughter("kanchan","deshpande","gauri")

print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)

chinmay.displayMname()
chinmay.displaySname()

print(gauri.firstName)
print(gauri.lastName)
print(gauri.dname)
gauri.displayMname()
gauri.displayDname()



# multiple inheritance

class Mother:

    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstName = fn 
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)
       

class Father:

    def __init__(self,fn,ln):
        print("father constructor called")
        self.firstName = fn 
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)
       

class Son(Mother,Father):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname+ self.lastName)

chinmay = Son("parent","deshpande","chinmay")
chinmay.displayName()
chinmay.displaySName()

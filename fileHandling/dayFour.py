# program 1 

# f1 = open('virat-kohli.jpg','rb')
# f2 = open('virat2.png','wb')
# bytes = f1.read()
# f2.write(bytes)
# f1.close()
# f2.close()

# program 2

# with open('f2.txt','w') as f:
#     f.write('i am learning ...')
#     f.write('i am learning python ...')

# with open('f2.txt','r') as f:
#     a = f.read()
#     print(a)


# program 2
# python object -----> binary file ---- serialization
# binary object -----> python object ---- deserialization


class Employee:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

#a = Employee("chinmay","deshpande")

import pickle
f = open('emp.data','wb')
n = int(input('number of objects ....'))

for x in range(n):
    fn = input('enter the fn')
    ln = input('enter the ln')
    e = Employee(fn,ln)
    pickle.dump(e,f)
f.close()



































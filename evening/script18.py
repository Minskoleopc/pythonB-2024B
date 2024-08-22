class Person:
    firstName = None
    lastName = None 
    age = None 
    rollNo = None

    def displayName(self):
        print(self.firstName + self.lastName)

amol =  Person()
# setting the values outside the class

amol.firstName = "amol"
amol.lastName = "rao"
amol.age = 56
amol.rollNo = 66

print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)
amol.displayName()


# class using constructor 
class Person():
    def __init__(self,fn,ln,ag,rn):
        self.firstName = fn 
        self.lastName  = ln
        self.age = ag 
        self.rollNo = rn 
    
    def displayName(self):
        print(self.firstName + self.lastName)

amol = Person("amol","rao",45,55)
chinmay = Person("chinmay","deshpande",34,22)
chinmay.displayName()

class Bank:

    # constructor
    def __init__(self,fullN,accNo,bal):
        self.fullName = fullN
        self.accNo = accNo
        self.balance = bal 
        self.transactions = []

    # deposit() method
    def deposit(self,amt):
        self.balance = self.balance + amt
        self.transactions.append(amt)
        return self.balance

    # withdrawl()
    def withdrawl(self,amt):
        if amt < self.balance:
            self.balance = self.balance - amt
            self.transactions.append(-amt)
            return self.balance
        else:
            print("Insufficient balance :"+str(self.balance))

    # lastFive transactions
    def lastFiveTransactions(self):
        return self.transactions[-5::]

amol = Bank("amol rao",123,1000)
amol.deposit(100)
amol.withdrawl(5)
amol.deposit(1000)
amol.withdrawl(50)
amol.deposit(10000)
amol.withdrawl(500)
amol.deposit(1000000)
amol.withdrawl(5000)

print(amol.lastFiveTransactions())
print(amol.transactions)


# python ---- oops , filehandling , function , regEx , directories
# python - dataanaylsis

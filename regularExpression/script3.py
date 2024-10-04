
# search()
# findall()
# match()
# group()
# split()
# sub()


# \w [a-z A-Z 0-9]
# \W [not[a-z A-Z 0-9]]
# \d [0-9]
# \D not [0-9]
# \b - blank space
# \A - refers to start of string 
# \Z  - end of strings 

# * -- zero or more
# + -- one and more
#a[\w]*
#a[\w]+
import re

str = "one two three four five six seven eight nine ten right"
e = re.search(r't[\w]*\Z',str)
print(e.group())

# e = re.search(r'\At[\w]*',str)
# print(e)


# program 3

str = "anil ajay aman anand ankur amit atul atharva"
e = re.findall(r'\ba[n][\w]*\b',str)
print(e)

e = re.findall(r'\ba[nm][\w]*\b',str)
print(e)

str  = "chinmay 7-11-1989 amol 19-08-1990 mayuri 21-02-1989"
a  = re.findall(r'\d{1,}-\d{1,}-\d{4}',str)
print(a)


str = "The meeting will start either at 9am or  9pm"
c = re.findall(r'[0-9][ap][m]',str)
print(c)





















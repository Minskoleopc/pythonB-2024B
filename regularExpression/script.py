
# chinmay-7709192441
# raj - 9766909110

#[a-z A-Z 0-9]
#man ma8

import re
str = "man sun mop run"
obj = re.search(r'm\w\w',str)
print(obj.group())

# program 2
# [A-Z  a-z 0-9]

str2 = "man sad mad cat sat sun mate fate"
result  = re.search(r's\w\w',str2)
if(result):
    print(result.group())

# program 3

# str2 = "man sad mad cat sat sun mate fate"
# listA = re.findall(r's\w\w',str2)
# print(listA)


str2 = "man sad mad cat sat sun mate fate 123"
listA = re.findall(r'\w\w\w',str2)
print(listA)

# program 3
# match

str3 = "python is good language"
e = re.match(r'p\w\w',str3)
print(e)
print(e.group())

# program 4
#not [a-z A-Z 0-9]
str4 = "This ; is the : 'Core' python's book"
f1 = re.split(r'\W+',str4)
print(f1)

str5 = "chinmay-7709192441"
f2 = re.split(r'\W+',str5)
print(f2)

# program 5
str6 = "I am learning javascript"
f5 = re.sub(r'javascript','python',str6)
print(f5)













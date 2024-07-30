fn = "chinmay"
ln = 'deshpande'
middleName = '''
    shirish  is learning javascript , 
    while chinmay is learning js
'''
middleName = """
    shirish  is learning javascript2 , 
    while chinmay2 is learning js
"""

# program 2
print(type(fn))

# program 3 
#str  stores the value by index 

str2 = "chinmay"
#  0    1   2   3   4   5   6
#  c    h   i   n   m   a   y

print(str2[0])
# range()
for char in range(7):
    #print(char)
    print(str2[char])

# without range()
for x in str2:
    print(x)

# using while()

i1  = 0
while(i1 < len(str2)):
    print(str2[i1])
    i1 = i1 + 1

# methods in str

# program 1
str3 = "chinmay"
s1  = str3.upper()
print(s1)

str4 = "Chinmay"
s2 = str4.lower()
print(s2)

str5  = "chinmay"
s3 = str5.capitalize()
print(s3)

str6 = "CHINMAY"
s6 = str6.isupper()
print(s6)

str7 = "chinmay"
s7 = str7.islower()
print(s7)

str8 = "Sanjay Is good Person"
s8 = str8.istitle()
print(s8)


# program 2

str9 = "pune"
s9 = str9.startswith('p')
print(s9)
s10 = str9.startswith('pun')
print(s10)
s11 = str9.startswith('Pun')
print(s11)

str10 = "Pune"
str12 = str10.endswith("ne")
str13 = str10.endswith("e")
str14 = str10.endswith("E")
print(str12)
print(str13)
print(str14)

# program 5
str11 = "111222"
str15 = str11.isdecimal()
# isdigit()
print(str15)

str12 = "asdasda"
str16 = str12.isalpha()
print(str16)


str13 = "11asdasda"
str14 = "asdasda"
str15 = "222"

print(str13.isalnum())
print(str14.isalnum())
print(str15.isalnum())



# program 6
str = "ninad"
e = str.count("n")
print(e)
str2 = "mayuri"

info = ["chinmay","shirish","deshpande"]
print(info)
e2 = "-".join(info)
print(e2)

info2 = ["chinmaydeshpande","gmail.com"]
e3 = "@".join(info2)
print(e3)
 
# program 7
firstName = "chinmay"
lastName = "deshpande"
# My firstName is chinmay and lastName is deshpande

lastName = "deshpande"
print("My firstName is {} and lastName is {}".format(firstName,lastName))
print(f"My firstName is {firstName} and lastName {lastName}")

# program 8
city = " chandrapur"
e2 = len(city)
print(e2)

e3 = city.lstrip()
print(len(e3))

city2 = " chandrapur "
e4 = city2.rstrip()
print(len(e4))

city2 = " chandrapur "
e5 = city2.strip()
print(len(e5))


city2 = "pune"
# 0  1   2   3
# p  u   n   e
print(city2.index('u'))
print(city2.find('U'))




























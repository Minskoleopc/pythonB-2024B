
# #*
# a an ann
# #a[\w]*
#[\w] --> [A-Z a-z 0-9]
# \b - blank space
# \d -  digit ---> 0 ,1 , 2, 3,4,5,6,7,8,9
import re
str = "an apple a day keeps doctor away"
# w2 = re.findall(r'a[\w]*',str)
# print(w2)

# program 2
str2 = re.findall(r'\ba[\w]*',str)
print(str2)

# program 3
str3 = "The meeting will be conducted on 1st and 21st of every month"
# str3 = re.findall(r'\d[\w]*',str3)
# print(str3)

str4 = re.findall(r'\d[\d]*',str3)
print(str4)

# program 4 
# search with exact 5 charact
str5 = "one two three four five six 7 8 9 10"
str5 = re.findall(r'\b\w{5}\b',str5)
print(str5)

#program 5
# search with more than 4 character
str6 = "one two three four five six 7 8 9 10"
str6  = re.findall(r'\b\w{4,}',str6)
print(str6)


str7 = "one two three four five six 7 8 9 10"
str7  = re.findall(r'\b\w{3,5}',str7)
print(str7)


# program 7
str8 = "one two three four five six 7 8 9 10"
str8  = re.findall(r'\b\d{1,}\b',str8)
print(str8)









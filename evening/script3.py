# break statement with while 

i3 = 1

while(i3 <= 5):
    print(i3) # 1 # 2 # 3
    if i3 == 3:
        break 
    i3 = i3 + 1 # 2 # 3


i3 = 1
while(i3 <= 5):
    if i3 == 3:
        break 
    print(i3)  #1 # 2
    i3 = i3 + 1  #2 # 3

# continue statement with while 

i4 = 1
while i4 <= 5:
    if i4 == 3:
        i4 = i4 + 1 #4
        continue
    print(i4) # 1 # 2 # 4  #5
    i4 = i4 + 1 # 2 # 3 # 5 # 6
    
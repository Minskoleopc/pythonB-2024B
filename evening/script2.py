# continue statement with for 

for x in range(1,6): # 2 # 3 # 4  #5 #6
    if x == 3:
        continue
    print(x) # 1 # 2 # 4 #5

for x in range(5,0,-1):
    if x == 3:
        continue
    print(x)

# while loop

# intialization
#while(condition):
    #statements
    #increment/decrement

# print 1 to 3

i1 = 1
while(i1 <= 3):
    print(i1) # 1 # 2 # 3
    i1 = i1 + 1 # 2 # 3 # 4

# print hello 3 times 
i2 = 1
while(i2 <= 3):
    print("hello")
    i2 = i2 + 1

# print 1 to 5 
i3 = 1
while(i3 <= 5):
    print(i3) # 1 # 2 # 3 #4 # 5
    i3 = i3 + 1 #2 # 3 # 4 #5 #6

# print 3 to 0
i4 = 3
while(i4 >= 0):
    print(i4) # 3 # 2 # 1 # 0
    i4  = i4 - 1 # 2 # 1 # 0 # -1

# print 5 to 1
i5 = 5
while(i5 >= 1):
    print(i5)
    i5 = i5 -1

# table of 2
i6 = 2
while(i6 <= 20):
    print(i6) # 2 # 4 # 6 ------- 20
    i6 = i6 + 2 # 4 # 6 #8------- 22


# table of 5 in reverse 
i7 = 50
while i7 >= 5:
    print(i7) # 50 # 45 ---------- 5
    i7 = i7 - 5 # 45 # 40 ------------- 0





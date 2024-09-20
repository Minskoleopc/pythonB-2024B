# import os 
# reclen = 10 

# size = os.path.getsize('cities.bin') # 30
# n = int(size/reclen) # 3
# with open('cities.bin',"r+b") as f:
#     newName = input('please enter new name to insert') # "jaipur"
#     replace = input('please enter a name to replace') # "pune"
#     newName = newName + (reclen - len(newName)) * " " #"jaipur    "
#     replace = replace + (reclen - len(replace)) * " " # "pune     "
#     newName = newName.encode() #"b jaipur      "
#     replace = replace.encode() #"b pune        "

#     position = 0
#     found = False

#     for x in range(n):
#         f.seek(position)
#         cr = f.read(reclen) #
#         if cr == replace:
#             found = True
#             break
#         else:
#             position = position + reclen
#     if found:
#         f.seek(position)
#         f.write(newName)
#         print('city succesfully replaced')

#pune
#"pune      " ===> "'b pune      " =====>  "              "

import os 
reclen = 10 

size = os.path.getsize('cities.bin') # 30
n = int(size/reclen) # 3
with open('cities.bin',"r+b") as f:
    delete = input('please enter city to be deleted') 
    delete = delete + (reclen - len(delete)) * " " 
    delete = delete.encode()
    emptyrecord =b" "* reclen  # "          "  
    position = 0
    found = False

    for x in range(n):
        f.seek(position)
        cr = f.read(reclen)
        if cr == delete:
            found = True
            break
        else:
            position  = position + 10

    if found:
        f.seek(position)
        f.write(emptyrecord)
        print('record deleted successfully')










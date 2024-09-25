# # print("hello")
# # x = int(input('Enter a number 1..?'))
# # y = int(input('Enter a number 2..?'))
# # print(x/y)
# # print('Bye')


# # program 2
# # print("hello")
# # try:
# #     x = int(input('Enter a number 1..?')) # 10
# #     y = int(input('Enter a number 2..?')) # 0
# #     print(x/y) 
# # except:
# #     print("error .....occured")
# # print("bye")

# # program 3 
# # print('hello')
# # try:
# #     x = int(input('Enter the number 1...?'))
# #     y = int(input('Enter the number 2'))
# #     print(x/y)
# # except ZeroDivisionError:
# #     print('please enter the correct input')
# # except ValueError:
# #     print('please enter the numbers ')
# # except:
# #     print('please enter the valid input')
# # print("bye")
    
# # program 4

# try:
#     #          0   1  2  3 4
#     numbers = [11,22,33,44,55]
#     n = int(input('please enter the index..'))
#     print(numbers[n])
# except IndexError:
#     print("please correct the index number")
# finally:
#     print('i will always execute...')

# # try  except else finally


# Basic try - except block

# program 1
print("hello")
try:
    x = 1/0
except ZeroDivisionError:
    print("you can't divide by zero")
print("bye")


#program 2
# try:
#     e = int(input("please enter a number :"))
#     f = int(input("please enter a number 2 :"))
#     print(e/f)
# except ValueError:
#     print("A value error occured")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except Exception as e:
#     print("any exception not known")


# program 3 
# Generic wat of raising exception 

# try:
#     numbers = [11,22,33]
#     e = int(input("please enter a number :"))
#     f = int(input("please enter a number 2 :"))
#     print(e/f)
#     print(numbers[4])
# except ValueError:
#     print("A value error occured")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except Exception as e:
#     print("any exception not known")
#     print(e)

# program 4
# try except else 
try:
    x = int('a')
    print("hello")
except ValueError:
    print("A value error occured")
except Exception as e:
    print(e)
else:
    print("i will run if no exception is raised")



#program 5
# try except else finally

# try:
#     x = 1/2
# except ZeroDivisionError:
#     print("you cannot divide by zero..")
# else:
#     print("no exceptio raised")
# finally:
#     print("this will always execute")

# finally block always execute irrespective of 
# exception raised or no exception raised

# program 6
# Raising the exception manually

def check_age(age):
    if age <= 18:
        raise ValueError("age must be greater than 18")
    return True

try:
    check_age(17)
    print("success")
except ValueError as e:
    print(e)


# program 7 
# Exception --
# customised


class UnderAgeError(Exception):
    pass

def check_age(age):
    if age <= 18:
        raise UnderAgeError("age must be greater than 18")
    return True

try:
    check_age(17)
    print("success")
except UnderAgeError as e:
    print(e)

# program 8
# assert 

def checkPositive(x):
    assert x > 0 ,"x must be positive"


try:
    checkPositive(-1)
    print('positive number...')
except AssertionError as e:
    print(e)


# program 9
try:
    with open('filetext2.txt',"r+") as f:
        c = f.read()
        print(c)
except FileNotFoundError:
    print("File not found")

# finally:
#     f.close()


# Keyerror exception


























































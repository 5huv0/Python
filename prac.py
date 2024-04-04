a = int(input("Input the value of a : "))
b = int(input("Input the value of b : "))

sum = a + b

print("The sum of A & B is : ", sum)

#-------------------------------------------------------------------------------

side = int(input("The side of the square is : "))

area = side * side

print("The area of the square is : ", area)

#-------------------------------------------------------------------------------

float1 = float(input("The first floating point number is : "))
float2 = float(input("The second floating point number is : "))

avg = ((float1 + float2) / 2)

print("The average of floating numbers is : ", avg)

#-------------------------------------------------------------------------------

a = int(input("Input A : "))
b = int(input("Input B : "))

if(a >= b ):
    print("True")
else:
    print("False")


#-------------------------------------------------------------------------------

userN = str(input("Your first name : "))

print(len(userN))


#-------------------------------------------------------------------------------


strg = "Can you give me 500$ so that i could bought you a 490$ PC and dont worry i will return you the remaining $ to you"

print(strg.count("$"))


#-------------------------------------------------------------------------------


num = int(input("Input your number : "))

if(num % 2 == 0):
    print(num , "is a even number")
else:
    print(num , "is a odd number")


#-------------------------------------------------------------------------------

userIn1 = input("Enter 1st number : ")
userIn2 = input("Enter 2nd number : ")
userIn3 = input("Enter 3rd number : ")

if(userIn1 > userIn2 and userIn1 > userIn3):
    print(userIn1 , "is the largest number")
elif(userIn2 > userIn1 and userIn2 > userIn3):
    print(userIn2 , "is the largest number")
else:
    print(userIn3 , "is the largest number")


#-------------------------------------------------------------------------------

num = int(input("Enter a number : "))

if(num % 7 == 0):
    print(num , "is 7's multiple")
else:
    print(num , "is not 7's multiple")
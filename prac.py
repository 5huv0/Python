# a = int(input("Input the value of a : "))
# b = int(input("Input the value of b : "))

# sum = a + b

# print("The sum of A & B is : ", sum)

#-------------------------------------------------------------------------------

# side = int(input("The side of the square is : "))

# area = side * side

# print("The area of the square is : ", area)

#-------------------------------------------------------------------------------

# float1 = float(input("The first floating point number is : "))
# float2 = float(input("The second floating point number is : "))

# avg = ((float1 + float2) / 2)

# print("The average of floating numbers is : ", avg)

#-------------------------------------------------------------------------------

# a = int(input("Input A : "))
# b = int(input("Input B : "))

# if(a >= b ):
#     print("True")
# else:
#     print("False")


#-------------------------------------------------------------------------------

# userN = str(input("Your first name : "))

# print(len(userN))


#-------------------------------------------------------------------------------


# strg = "Can you give me 500$ so that i could bought you a 490$ PC and dont worry i will return you the remaining $ to you"

# print(strg.count("$"))


#-------------------------------------------------------------------------------


# num = int(input("Input your number : "))

# if(num % 2 == 0):
#     print(num , "is a even number")
# else:
#     print(num , "is a odd number")


#-------------------------------------------------------------------------------

# userIn1 = input("Enter 1st number : ")
# userIn2 = input("Enter 2nd number : ")
# userIn3 = input("Enter 3rd number : ")

# if(userIn1 > userIn2 and userIn1 > userIn3):
#     print(userIn1 , "is the largest number")
# elif(userIn2 > userIn1 and userIn2 > userIn3):
#     print(userIn2 , "is the largest number")
# else:
#     print(userIn3 , "is the largest number")


#-------------------------------------------------------------------------------

# num = int(input("Enter a number : "))

# if(num % 7 == 0):
#     print(num , "is 7's multiple")
# else:
#     print(num , "is not 7's multiple")


#-------------------------------------------------------------------------------

# movie1 = input("Input you fav movie 1 : ")
# movie2 = input("Input you fav movie 2 : ")
# movie3 = input("Input you fav movie 3 : ")

# list = []

# list.append(movie1)
# list.append(movie2)
# list.append(movie3)

# print(list)


#-------------------------------------------------------------------------------
# make a list and check if the list is palindrome or not 

# list = [1, 2, 3, 2, 1]
# listC = list.copy()
# listC.reverse()

# if(listC == list):
#     print("It is  palindromic")
# else:
#     print("It is not palindromic")


#-------------------------------------------------------------------------------

# grades = ("C", "A", "B", "A", "A", "B" ,"A")


# count = grades.count("A")
# print(count)


#-------------------------------------------------------------------------------

# list = []

# list.append(str(input("Input grades : ")))
# list.append(str(input("Input grades : ")))
# list.append(str(input("Input grades : ")))
# list.append(str(input("Input grades : ")))
# list.append(str(input("Input grades : ")))
# list.append(str(input("Input grades : ")))

# sorted = list.sort()

# print(list)

# print(sorted)


#-------------------------------------------------------------------------------

# dict = {
#     "table" : "a piece of furniture" ,
#     "cat" : "a small animal",
#     "theory" : "list of fact and figures"
# }

# print(dict)


#--------------------------------------------------------------------------------


# subjects = {"python", "java", "C++", "python", "js", "java", "python", "java", "C++", "C"}
# print(len(subjects))


#--------------------------------------------------------------------------------

# dict = {}

# x = int(input("enter the marks of phy : "))
# dict.update({"Physics" : x})

# y = int(input("enter the marks of chem : "))
# dict.update({"Chemistry" : y})

# z = int(input("enter the marks of bio : "))
# dict.update({"Biology" : z})


# print(dict)



#--------------------------------------------------------------------------------



# set = ("9.00", 9)

# print(set)


#--------------------------------------------------------------------------------

# number = int(input("Input which times table you want to see : "))
# stop = int(input("Input where you want to stop the time table : "))
# i = 1


# while i <= stop:
#     mult = number * i
#     print(number ,"x", i, "=", mult)
#     i += 1 



#--------------------------------------------------------------------------------

# list = [1, 3, 9, 16, 25, 56, 78, 45]
# length = len(list) - 1
# i = 0
# newL = []


# while i <= length:
#     print(list[i])
#     i += 1


#--------------------------------------------------------------------------------


# search = int(input("enter : "))

# num = (1, 3, 9, 16, 25, 56, 78, 45)
# i = 0
# length = len(num) - 1


# while i <= length : 
#     if(num[i] == search):
#         print("found")
#         break  # can also use continue
#     else:
#         print("finding...")
#     i += 1


#--------------------------------------------------------------------------------

# for i in range(100 , 0, -1):
#     print(i)


#--------------------------------------------------------------------------------

# n = int(input("Enter number : "))
# sum = 1
# i = 1

# while i <= n:
#     sum += i
#     i += 1
 
# print("Total sum : ", sum)

#--------------------------------------------------------------------------------

# n = int(input("Enter number : "))
# factorial = 1
# i = 1

# while i <= n:
#     factorial *= i
#     i += 1
 
# print("Total factorial : ", factorial)


#--------------------------------------------------------------------------------


# def list(a, b, c, d, e, f, g):
#     list = [a, b, c, d, e, f, g]
#     return list


# print(list(1, 2, 3, 4, 5, 6, 7))


#--------------------------------------------------------------------------------

# def list(a, b, c, d, e, f, g):
#     list = [a, b, c, d, e, f, g]
#     return list

# lengthList = list(1, 2, 3, 4, 5, 6, 7)


# print(len(lengthList))


#--------------------------------------------------------------------------------


# def factorial(n):
#     factorial = 1
#     i = 1

#     while i <= n:
#         factorial *= i
#         i += 1
#     return factorial    

# print(factorial(5))


#--------------------------------------------------------------------------------

# def func(n):
#     if(n % 2 == 0 and n != 0):
#         print("Even")
#     elif(n % 2 != 0):
#         print("Odd")
#     elif(n == 0):
#         print("It is 0")

# func(0)        


#--------------------------------------------------------------------------------

# def sum(n):
#   if(n == 0):
#     return 0
#   return sum(n-1) + n

# summ = sum(9)   
# print(summ)

#--------------------------------------------------------------------------------

# def list_print(list , idx = 0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     list_print(list , idx + 1)

# fruits = ["mango", "banana", "apple"]    

# list_print(fruits)


#--------------------------------------------------------------------------------

# class Students():
#     def __init__(self, Fname, Phy, Math, Chem):
#         self.name = Fname
#         self.phy = Phy
#         self.math = Math
#         self.chem = Chem

#     def avg(self):
#         average = (self.phy + self.math + self.chem) / 3
#         print(s1.name, "youe average mark is : ", average)


# s1 = Students("mahi", 80, 78, 98)
# print(s1.name, s1.phy, s1.chem, s1.math)
# s1.avg()


#--------------------------------------------------------------------------------
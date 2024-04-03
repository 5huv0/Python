## if-elif-else
a = int(input("a : "))
b = int(input("b : "))

if(a > b):
    print("a is greater than b")
elif(a < b):
    print("a is less than b")
else:
    print("both are equal")
    

#----------------------------------------------------------------------------------------------------

light = str(input("Traffic Light : "))

if(light == "red"):
    print("You can not cross now")
elif(light == "yellow"):
    print("Wait a minute let it be green")
elif(light == "green"):
    print("You can cross now")
else:
    print("Light is broken")

#-----------------------------------------------------------------------------------------------------------

marks = int(input("Obtained Mark : "))

if(marks >= 90 and marks <= 100):
    print("A+")
elif(marks >= 85 and marks <= 89):
    print("A")
elif(marks >= 80 and marks <= 84):
    print("A-")
else:
    print("B")

#--------------------------------------------------------------------------------------------------------------

food = input("food : ")

eat = "yes" if food == "biriyani" else "no"

print(eat)


#--------------------------------------------------------------------------------------------------------------

food1 = input("item : ")

print("Eat it ") if food1 == "beef" or food1 == "mutton" else print("Do not eat it ")


#---------------------------------------------------------------------------------------------------------------

#type casting

a = 10
b = "2"
c = int(b)

sum = a + c

print (sum)
# Class and object

# class Student:
#     name = "shuvo"


# s1 = Student()
# print(s1.name)

# class Car:
#     color = 'Blue'
#     brand = "Audi"

# car1 = Car()
# print(car1.color, car1.brand)

#----------------------------------------------------------------

# Constructor
class Student:
    collegeName = "DCC"
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("you know nothing...")

s1 = Student("mahi", 88)
print(s1.name)
print(s1.marks)
print(s1.collegeName)

s2 = Student("gobin", 67)
print(s2.name)
print(s2.marks)


s3 = Student("hog",68)
print(s3.name)
print(s3.marks)

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
    name = "mia"
    def __init__(self, fullname):
        self.name = fullname
        print("you know nothing...")

s1 = Student("mahi")
print(s1.name)

s2 = Student("gobin")
print(s2.name)


s3 = Student("hog")
print(s3.name)

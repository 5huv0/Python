#----------------------------------------------------------------------
# del keyword

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("shuvo")
# print(s1)
# del s1
# print(s1)
        
#----------------------------------------------------------------------
# public and private attribute

# class Account:
#     def __init__(self, accNo, accPass):
#         self.accNo = accNo
#         self.__accPass = accPass

#     def resetPass(self):
#         print(self.__accPass)    


# user1 = Account("1", "88745")
# user1.resetPass() # this is used in a class thats why working
# print(user1.__accPass) # this is not using inside the class that is why it is not working

        
#----------------------------------------------------------------------
# Inheritance

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started....")

#     @staticmethod
#     def stop():
#         print("Car stopped!!!!")

# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name

# class Supra(Toyota):
#     def __init__(self, type):
#         self.type = type

# car1 = Supra("diesel")
# car1.start()
# print(car1.color, car1.type)

#----------------------------------------------------------------------
# Super method of inheritance

# class Car:

#     def __init__(self, type):
#         self.type = type

#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started....")

#     @staticmethod
#     def stop():
#         print("Car stopped!!!!")

# class Toyota(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         super().start()
#         self.name = name
        
    
# car1 = Toyota("supra", "fuel")
# print(car1.type, car1.start())


#----------------------------------------------------------------------
# classmethods 

# class Person:
#     name = "mukul"


#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changeName("kumar")
# print(p1.name)
# print(Person.name)



#----------------------------------------------------------------------

# property decorator

# class Students:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

    
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    



# std1 = Students(89,98,97)
# print(std1.percentage)


# std1.phy = 76
# print(std1.percentage)


#----------------------------------------------------------------------

# polymorphism : operator overloading

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img


    def showNum(self):
        print(self.real, "i + ", self.img, "j" )

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
    # def __mul____(self, num2):
    #     newReal = self.real * num2.real
    #     newImg = self.img * num2.img
    #     return Complex(newReal, newImg)
    
    # def __truediv____(self, num2):
    #     newReal = self.real / num2.real
    #     newImg = self.img / num2.img
    #     return Complex(newReal, newImg)



num1 = Complex(2, 3)
num1.showNum()

num2 = Complex(5, 7)
num2.showNum()

num3 = num1 + num2
num3.showNum()

num3 = num1 - num2
num3.showNum()

# num3 = num1 * num2
# num3.showNum()

# num3 = num1 / num2
# num3.showNum()

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

class Car:

    def __init__(self, type):
        self.type = type

    color = "black"
    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped!!!!")

class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)
        super().start()
        self.name = name
        
    
car1 = Toyota("supra", "fuel")
print(car1.type, car1.start())


#----------------------------------------------------------------------
#----------------------------------------------------------------------
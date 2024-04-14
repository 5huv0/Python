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

class Account:
    def __init__(self, accNo, accPass):
        self.accNo = accNo
        self.__accPass = accPass

    def resetPass(self):
        print(self.__accPass)    


user1 = Account("1", "88745")
user1.resetPass() # this is used in a class thats why working
print(user1.__accPass) # this is not using inside the class that is why it is not working

        
#----------------------------------------------------------------------
# Inheritance


#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------
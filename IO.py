# Open Read files



# f = open("./files/demo.txt", "r")

# data = f.read()
# data1 = f.readline()
# print(data, data1)

# f.close()

#-------------------------------------------------------------------

# Open Write files



# f = open("./files/demo.txt", "w")

# data = f.write("This is a new line in my code")
# print(data)

# f.close()


#--------------------------------------------------------------------

# Open Append files




f = open("./files/demo.txt", "a")

data = f.write("\n ok now add a new line i my file ")
print(data)

f.close()
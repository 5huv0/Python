# Open Read and Close files

f = open("./files/demo.txt", "r")

data = f.read()
data1 = f.readline()
print(data, data1)

f.close()
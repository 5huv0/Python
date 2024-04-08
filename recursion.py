# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)

# show(5)    


#-----------------------------------------------------------

def factorail(n):
    if(n == 1 or n == 0):
         return 1
    return factorail(n - 1) * n

print(factorail(int(input("Enter the value : "))))
# range(start? , stop, step?) here starting is by deafult 0 , if we put only 1 value it will be the stop value, step is increment 

seq = range(10)

for i in seq:
    print(i)

for j in range(6): # only stop given
    print(j)

for k in range(2, 9): # start and stop
    print(k)

for k in range(1, 9, 2): # start and stop and step
    print(k)
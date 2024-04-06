collection = {1, 2, 3, 4, 5, 6, "hi", "ok"}

#creating empty set 

newColl = set()

print(collection, newColl)

#-------------------------------------------------------------------

# Set methods 



# set.add() add an element
# set.remove(ele) remove elemets
# set.clear() empties the set
# set.pop() remove a random value


print(collection.pop())


collection.remove("hi")
print(collection)
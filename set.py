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


#-------------------------------------------------------------------


# Set important methods


# set.union(set2) combine both sets and return a new set
# set.intersection(set2) combine common values and returns a new set


set1 = {1, 2, 3, 4, 5, 7}
set2 = {10, 20, 30, 40, 50, 7}

union = set1.union(set2)

intersection = set1.intersection(set2)

print(union, intersection)
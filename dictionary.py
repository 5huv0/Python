# It is like objects 
info = {
    "name" : "shuvo",
    "age" : 23,
    "hobby" : "gaming",
    "learning" : {
        "one" : "C",
        "two" : "Python",
        "three" : "Java script",
        "four" : "C++"
    }
}


print(info["learning"]["one"])


# Methods of dictionary

# dict.keys() return all keys
# dict.values() return all values
# dict.items() return all (key value) pairs as tuples
# dict.get() return the key according to value
# dict.update(newDict) inserts the specified items to the dictionary

print(info.items())

print(info.get("hobby"))

info.update({"city" : "dhaka"})

print(info)
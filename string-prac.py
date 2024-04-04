strg = "this a new string.\ni want to go to on next line.\nfor this i will use escape sequence character "
strg2 = "this a new string.\ti want tab.\tfor this i will use escape sequence character"

print(strg, strg2)

length = len(strg)

print(length)

print(strg[2])

#---------------------------------------------------------------------------------------------------------------------------

# SLICING

strg = "my hobby is playing video games"

print(strg[1 : 5])

strg = "i love songs"

print(strg[-6 : -2])

#---------------------------------------------------------------------------------------------------------------------------


# String Functions

# str.endsWith(".")  returns true if string ends with substring 
# str.capitalize() capitalize first character oof the string
# str.replace(old, new) replaces all of old value with new value
# str.find(word) returns first index of first times it finds that word
# str.count(".") counts how many times the substring exists in the string
# STRINGS

# Basics
'hello'
"hello"

"I'm a dog"
'He said, "Drop it."'

#Indexing
mystring = 'abcdefg'
print(mystring[0]) # a

# negative indexing is supported to find the last indexing
print(mystring[-1]) # g

print(mystring[3]) # d

# Slicing
print(mystring[4:]) # efg

print(mystring[2:5]) # cde

print(mystring[:]) # returns entire string

print(mystring[::2]) # returns entire string skipping every other index

# strings are immutable, so you could not write mystring[0] = 'x'

# Basic Methods
w = mystring.upper()
print(w)

x = mystring.capitalize()
print(x)

y = 'Hello World'.split()
print(y)
# split will naturally split at white spaces between characters in a string,
# if a character is passed as a param, it will be split there instead
z = mystring.split('e')
print(z)

# Print Formatting
pf1 = "Insert another string here: {}".format("INSERT ME!")
print(pf1)

pf2 = "Item One: {} Item Two: {}".format("dog", "cat")
print(pf2)

pf2 = "Item One: {y} Item Two: {x}".format(x="dog", y="cat")
print(pf2)

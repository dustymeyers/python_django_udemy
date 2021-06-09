# Dictionaries

my_stuff = {"key1":"value", 'key2':'value2', 'key3': {'123':[1, 2, 'grabMe']}}
print(my_stuff['key1']) # value
print(my_stuff['key2']) # value2

print(my_stuff['key3']['123'][2]) #grabMe
my_stuff = {'lunch': 'pizza', 'bfast': 'eggs'}
print(my_stuff['lunch']) # pizza
my_stuff['lunch'] = 'burger' # dictionaries are mutable
my_stuff['dinner'] = 'pasta' # defines a new key/value pair if not already declareds
print(my_stuff['lunch']) # burger
print(my_stuff['dinner']) # pasta

#Booleans
True
False
0 # more common to see True/False
1

# Tuples, tuples are immutable
# t[0] = 'NEW' will not work
t = (1, 2, 3)
print(t[0])

t = ('a', True, 123)
print(t)

#SETS
# unorderd lists of unique elements
x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
x.add(4) # will not appear when printed since 4 was already added
print(x)

converted = set([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]) # will convert the list into a set {1, 2, 3}
print(converted)

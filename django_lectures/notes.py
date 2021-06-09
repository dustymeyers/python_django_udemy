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

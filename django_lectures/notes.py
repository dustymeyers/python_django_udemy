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

############################
### Comparison Operators ###
############################

# Greater than
1 > 2

# Less than
1 < 2

# Greater than or Equal
1 >= 0

# Equality
1 == 1
1 == "1" # this will return false, STRONGLY TYPED
'hi' == 'bye' #this will also return False

# Inequality
1 != 2


#########################
### Logical Operators ###
#########################

# AND
(1 > 2) and (2 < 3) # both must be equal to return true

# OR
(1 > 2) or (2 < 3) # at least one must be equal to return True

# Multiple logical Operators
(1 == 2) or (2 == 3) or (4 == 4)

################################
### IF, ELIF, ELSE Statments ###
################################

if 1 < 2:
    print('yes')

if 1 < 2:
    if 2 < 3:
        print('True!')

if 1 < 2:
    print('First Block')
    if 20 < 3:
        print('Second Block') # this will not execute

if 2 < 1:
    print('hello') # this will not execute
else:
    print('last')

if 1 ==1:
    if 1 > 2:
        print('hello')
    elif 3 == 3:
        print('elif ran')
    else:
        print('last')

#############
### LOOPS ###
#############

# For LOOPS

seq = [1,2,3,4,5,6]

for item in seq:
    # code here
    print(item) # prints each item in the list, it will print that item
    # item is kittykat

d = {'Sam': 1, 'Frank': 2, 'Dan': 3}

for item in d:
    print(item) # just like the list, it will print out each item in the dictionary, but don't expect it to be in a specific order
    # will only print the keys

for k in d:
    print(k)
    print(d[k]) # this allows us to list the actual values of each key

mypairs = [(1, 2), (3, 4), (5, 6)]

for item in mypairs:
    print(item)

# tuple unpacking
# for (tup1, tup2) in mypairs:
for tup1, tup2 in mypairs:
    print(tup2)
    print(tup1)

# WHILE LOOPS
i = 1

while i <5:
    print("i is {}".format(i))
    i = i + 1

# Range Function
for item in range(10):
    print(item)
# will print each number up to but not including 10

#List comprehension

x = [1, 2, 3, 4]
out = []

for num in x:
    out.append(num**2)

print(out)

# instead do

out = [num**2 for num in x]

print(out)

#################
### Functions ###
#################

def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    """
    print("my first python function! {}".format(param1))

def hello():
    return "hello"

result = hello()

print(result)

def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, I need integers"

result = addNum("2", "3")
# will result in concatonation making a string "23" instead of number 5
# refactored for type check
print(result)

# Lambda Expression

# Filter
mylist = [1, 2, 3, 4, 5, 6, 7, 8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)

print(list(evens))

evens2 = filter(lambda num: num%2 == 0, mylist)

print(evens2)

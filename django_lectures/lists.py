# Lists

# mylist = [1,2,3]
mylist = ['ta;iefa',1,2,3,23.2,True,'asdf',[1,2,3]]
print(mylist)

mylist = ['a','b','c']

print(mylist)

# indexing
print(mylist[0]) # 'a'

print(mylist[-1]) # 'c'

print(mylist[:3]) # ['a','b','c']

# lists are mutable
print('before reassignment:', mylist)
mylist[0] = 'New Item' # changes a to new item
print('after reassignment:', mylist)

# Methods
mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append("NEW ITEM") # Will add it to the end of the list
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
listtwo = ['x','y','z']

mylist.append(listtwo) # will add the new list to the end of the original, will not merge the two!
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.extend(listtwo) #merges the two lists
print(mylist)

item = mylist.pop()
print(mylist) # the last item in the list is now gone
print(item) # this is the item that was removed from the list

item = mylist.pop(3) # remove item at index 3
print(mylist)
print(item)

mylist = [4,6,1,7,43,2]
mylist.reverse() # does exactly what you think
print(mylist)

mylist.sort() #sorts from highest to lowest, can sort mixed data type lists but is bad practice
print(mylist)

# Nested Lists
mylist = [1, 2, ['x', 'y', 'z']]
print(mylist[2][1]) # nested list indexing, will give back y

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0]) # 1
# LIST COMPREHENSION
first_col = [row[0] for row in matrix] # will return the 0 index for each nested list in a list, [1, 4, 7]

print(first_col)

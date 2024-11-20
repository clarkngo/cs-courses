'''
append() - Add an element to the end of the list                #append(item)
extend() - Add all elements of a list to the another list       #extend([...])
insert() - Insert an item at the defined index                  #insert(index, item)
remove() - Removes an item from the list                        #remove(a known item), del list[2]
pop() - Removes and returns an element at the given index       #return an item that is popped
clear() - Removes all items from the list
index() - Returns the index of the first matched item           #retuns index that is found first in the list
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order                #sort on the same data type in ascending order
reverse() - Reverse the order of items in the list              #sort on the same data type in descending order
copy() - Returns a shallow copy of the list
'''

#****************************************************************
# 1. List 
#****************************************************************

# here is how to create an empty list
mylist = [] # empty list

# another way to create a list with the initial values
mylist = [1, 5, 4, 2, 8, 7, 3, 6, 9]

# How to assign values to a List
# mylist = ['apple', 24, 'Kate', 23, [2,3,4]]

# How to access values to a list
mylist[0]  # first item (forward (0th index))
mylist[1]  # first item (forward (0th index))
mylist[len(mylist)]  # first item (forward (0th index)) --> error exclusive
mylist[-1] # last item (backwards)

# How to slice the entries in a List [x:y] ==> x to y-1 (=item before y)
#                                    [x:] ==> x to the last
#                                    [:y] ==> first to y-1 (=item before y)
#                                    [:]  ==> all
# don't get confused between slice and range
# slice[start:stop:step]
# range[start, stop, step)
mylist[1:3] # 1 to 3-1
mylist[3:]  # 3 to the end
mylist[:3]  # first to 3-1
mylist[:-2] # first to one item before (the 2nd to the last)

# now, I want to access the 2nd item in the nested list.
mylist[4]
mylist[4][2]

# modifying entries
mylist[1] = 'PEAR'
print(mylist)
mylist[-1] = (2,3,4)
print(mylist)

# How to add an entry in a list
# insert(index, new_value) 
mylist.insert(4, 'Seattle')
mylist.insert(5, 54)
mylist.insert(6, 'Seattle')

# append(new_value) # no need to add index since we know it is appending
mylist.append(-293)

mylist.count('Seattle') # returns the # of occurrences of the value, freq. or histogram

# How to remove an entry in a list
# item = pop(index) index-th item , pop() => last
item = mylist.pop(3)
item = mylist.pop() # returns the last item from the list and removes the item from the list

# remove(value) the first occurrence of value
mylist.remove('Seattle')

mylist.clear()

del(mylist[-1])

del mylist # Hasta la vista


# 
# let's look at the slicing to create a new list object
#
# slicing is a method to display the all or subset of a list
#
z = list(range(1,100)) # [start:stop:step] 
# help(range)  range(stop) -> range object
#              range(start, stop[, step]) -> range object

z[0:10:1]       # start = 0 to stop = 9, by 1
z[0:100:10]
z[1:100:10]

# start,end,step = optional params with defaults
# start = 0, end = len(z), step = 1
z[:10]   # start=start, end=10, step=1
z[90::1] # start=90, end=end, step=1 --> same as z[90::] remove defaults
z[::10]  # start=start, end=end, step=10 --> same as z[0::10] remove defaults

list_num = [1, 5, 4, 2, 8, 7, 3, 6, 9]
list_num.sort(reverse=True)     # 9,8,7,6,5,4,3,2,1
print(list_num)

list_num.sort()                 # 1,2,3,4,5,6,7,8,9
print(list_num)


print(max(list_num))            # 9
print(min(list_num))            # 1
print(sum(list_num))            # 45

# Challenge question
# How would you get the average of the list in one line of expression?
average = sum(list_num)/len(list_num)


# How to traverse the list
mylist = [1, 5, 4, 2, 8, 7, 3, 6, 9]
for i in mylist: # traversing to each item directly in the list
    print(i, end=' ')   # print all items / line
    #print(i)           # print one item  / line

for i in range(0, len(mylist)): # traversing thru the index to the list
# for i in range(len(mylist)):  # <- simpler way to express the range since start default = 0  
    print(f"item {i} = ", mylist[i])

# few important built-in methods
mylist.sort()   # sort the list Note: modifying the list (aka *IN PLACE*)
mylist.reverse() # reverse the order of items in the llst.
mylist.count()  # count the number of occurrence, frequency
len(mylist)     # returns the number of items in the list


# Let's quickly look at how to generate random numbers

import random
random.randrange(0, 100) # selecting one random value from 0 - 100
random.sample(range(0, 100), 10) # selecting 10 random #s in 0-99
random.sample(range(-100, 100), 10) # selecting 10 random #s in -99 to +99

#
# More LIST examples
# Sum the list of numbers
list_num = random.sample(range(-100, 100), 10)
# init. sum
s = 0
for val in list_num:
    s = s + val
print("total sum is ", s)

s = 0
for i in range(len(list_num)): # using the range to traverse
    s = s + list_num[i]
print("total sum is ", s)

for i in list_num:
    print(i)
else: # else block
    print("no more item in the list")

#
# -- nested list -> nested loops (5 x 3)
#
list_num = [[6, 2, 3], [5, 2, 11], [4, 9, 22], [-3, 9, 13], [10, 1, 9]]
for i in range(5):
    for j in range(3):
        print(list_num[i][j])
#
# -- What if I want to print nested lists with different sizes?
#
list_num = [[3], [5, 2, 11], [9, 22], ['k', -3, 9, 13], [10, 1, 9]]
for i in range(len(list_num)):
    print("\n")
    for j in range(len(list_num[i])):
        print(list_num[i][j])


#
# With the user's input character, the program prints a message that says vowel or not. If not vowel, it continues if not, stops.
#
vowels = "aeiouAEIOU"
#infinite loop
while True:
    v = input("Enter a vowel: ")
    if v in vowels:
        break
    print("No! That's not a vowel. Try again")
    print("You entered ", v)
print("Good job!")



# Copying a list

# this way, they both refer to the same python object
a = [1, 2, 3]
b = a
print(a)    # [1, 2, 3]
print(b)    # [1, 2, 3]
a[0] = 10
print(a)    # [1, 2, 3]
print(b)    # [1, 2, 3]


# ---------------------------------------------------------
# SHALLOW COPY V. DEEP COPY
# ---------------------------------------------------------
# So, we have different types of copy methods, shallow copy and deep copy to avoid this type of copy
#
# * Shallow copy creates a copy of the object but references element of the nested objects copied at the time of creation.
#
# Shallow copy creates a copy of the objects from the source
# When the source changes the objects, source and copied objects work independently in the first layer
# However, when the source changes the contents of the nested objects, the its new contents will be copied to the copied object.
# 
# Let's say we shallow copied a house, old and new
# You added additional room in your old house, and the new(copied) house will not be synched (referenced)
# You changed the door in the room in your old house, and your new house will be synched (referenced)
# 
# If you know that list won't grow or shrink and the values of nested object need to be maintained then use shallow copy.
# (e.g.) RGB value change or (X,Y) point pair change between 2 copied objects
#
# * Deep copy creates a copy of the object and the elements of the object as an independent object
#
import copy
o = [1, 2, 3]   # original list
s = copy.copy(o) # "s"hallow copy c = o.copy() or copy.copy(o)
print(o)    # [1, 2, 3]
print(s)    # [1, 2, 3]
s[0] = 10
print(o)    # [1, 2, 3]
print(s)    # [10, 2, 3]

d = copy.deepcopy(o) # "d"eep copy d = copy.deepcopy()
print(o)    # [1, 2, 3]
print(d)    # [1, 2, 3]
d[0] = 10
print(o)    # [1, 2, 3]
print(d)    # [10, 2, 3]

hex(id(o))
hex(id(s))
hex(id(d))

#****************************************************************
# 2. Tuple
#****************************************************************
# How to define a tuple
mytuple = () # empty tuple

# a tuple with initial values
mytuple = ("R", "#FF00000", "G", "#00FF00", "B", "#0000FF")
#   or without ()
mytuple = "R", "#FF00000", "G", "#00FF00", "B", "#0000FF"

# How to access values to a list
mytuple[0]  # first item (forward (0th index))
mytuple[-1] # last item (backwards)

# How to slice the entries in a tuple [x:y] ==> x to y-1 (=item before y)
#                                     [x:] ==> x to the last
#                                     [:y] ==> first to y-1 (=item before y)
#   
mytuple[1:3] # 1 to 3-1
mytuple[3:]  # 3 to the end
mytuple[:3]  # first to 3-1
mytuple[:-2] # first to one item before (the 2nd to the last)
i=2
mytuple[i:i+2]


# no addition (immutable)
# no insert (immutable)
# no append (immutable)
# no remove (immutable)

# How to traverse the tuple
for i in mytuple:
    print(i, end=' ')   # print all items / line
    #print(i)            # print one item  / line

for i in range(0, len(mytuple)):
    print(f"item {i} = ", mytuple[i]) # print formatting

# more example (sub-tuples inside a tuple)
points = ((1.2,-2.3), (13.3,-2.9), (24.3,-3.5)) # (x, y) coordinates
for point in points:
    x, y = point
    print(f"x = {x}, y = {y}")

# Can you shorten the for loop?
for (x, y) in points: 
    print(f"x = {x}, y = {y}")



# few important built-in methods (multiple assignment or unpacking
x, y = 0.24, 3.28
a, b, c, d, e, f = mytuple # 'unpacking' mytuple example above
p1, p2, p3 = points # 'unpacking points example above
len(mytuple)    # returns the number of items in the tuple


# Note: Tuples may be created directly or converted from lists. 
x = list(mytuple)
y = tuple(x)







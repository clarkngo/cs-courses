
# Dictionaries in Python are a list of items that are unordered and can be 
# changed by use of built in methods. Dictionaries are used to create a map 
# of unique keys to values.
# List and Dictionary are the most used data types in Python
# It is a composite data type.
# - mutable
# - grow or shirnk the data type on the fly
# - can be nested meaning dict can contain another dict or list or tuple
# - accessing an entry is different than list or tuple or string, via a key
#
# -- let's create a empty dictionary
#    and go over how we can define a dictionary data type
#
# 
# empty dictionary
d = {}

# create a dict (1)
d = {'Name': 'John', "Choice": (2,3,4)}
d
{'Name': 'John', "Choice": (2, 3, 4)}

# create a dict (2) using the dict() to create
d = dict({'Name': 'John', "Choice": (2,3,4)})
d
{'Name': 'John', 'Choice': (2, 3, 4)}

# create a dict (3) with an assignment

d = dict(Name = 'John', Choice = (2, 3, 4))
d
{'Name': 'John', 'Choice': (2, 3, 4)}

# create a dict (4) using the dict() to create
# each item as a pair <-- using a list
# if you're getting tuples as an input to create a dictionary, this 
# format would be very convenient when you're using return value from a function
d = dict([('Name','John'), ('Choice',(2, 3, 4))])

#
# -- how do we access the dictionary data?
#
d = dict([('Name','John'), ('Choice',(2, 3, 4))])
d
{'Name': 'John', 'Choice': (2,3,4)}
d['Name']
'Jack'
d['Jack'] # error --> KeyError: 'Jack'
d['Choice']
(2, 3, 4)

d.get('Name') #funciton () == d['Name']
'John'
d.get('Choice') #funciton ()
d['Choice']     # direct access []


# -- let's make some changes to the dictionary. 
#    modification of value by accessing 'key'
#    please remember key - immutable, value - mutable
#    therefore, use the key to modify its associated value

d['Name']
'John'
d['Choice'] = (2, 1, 5)
{'Name': 'John', 'Choice': (2, 1, 5)}

#
# -- how about adding a key value pair to the dictionary?
#
d['Address'] = 'Downtown' # d[new_keyword] = new_value for the keyword
d['Job'] = 'IT Profession'

#
# -- how about removing key value pair?
#
d.pop() # error -> help(d.pop())
        # D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        # help(d.pop)
d.pop('Address')        
c = d.pop('Job') # c = 'Seattle'
d.popitem() # returns the last tuple item (last in first out) => stack
#
# -- how to delete or clear the entire dictionary
#
d.clear() # remove all the items
del d     # will completely destory its allocation

# -- Let's look at different ways to validate/display keys and values
#    once it is defined
d = {'Jim': 1253, 'Tim': 9923, 'John': 4923, 'Jake': 2342}
d.keys()
d.values()
d.items()
# these can be used in conjunction with list() to display in the list format
list(d.items())
list(d.values())

# Key or value exist in a dictionary
# when the dictionary is being accessed it is accessed via keys for items()
'Jim' in d # True
1253 in d # False
1253 in d.values()
1253 in d.keys()
'Jim' in d.keys()
'Kate' in d.keys()
'Kate' not in d.keys()

# -- We can also merge two dictionaries
d1 = {'a': 10, 'b': 8, 'd': 6, 'e': 11}
d2 = {'f': 6, 'g': 11}
d1.update(d2) # d1 + d2
d3 = {**d1, **d2}

ab


# -- Sorting
sorted(d3.keys())
sorted(d3.values())
sorted(d3.items())

# it is straightforward to think that sort by key since it is unique
# but there is a situation where sorting by value is important for instance
# give me a word that has the highest frequency.

# This method returns list of keys based on reverse sorted value (high-low).
sorted(d3, key=d3.get, reverse=True) # where get(key, default=None, /) 

# Challenge Question
# print a set of letters in which count is greater than 4
# or average of the frequency
for letter, count in d3.items():
    if count > 6:
        print(letter)





#****************************************************************
# Set (unordered list)
#****************************************************************
# myset = set(<iter>) # <iter> = list or tuple
# How to define an empty set

my_set = set()

set1 = set(['a1', 'a2', 'a3', 'a2', 'a4', 'a5']) # you can use iterators (list or tuple)
set2 = {'b1', 'b2', 'a1', 'a1', 'b5'} # you can also use {} don't get confused with dictionary {"James":1423, "Kay":4392} {key:value}
set3 = {} # would this be dictionary or set? it is dictionary, type(set3)

#
# to find out if a given iterable is a ordered or unordered 
#
[1,2,3] == [2,3,1] # False
{1,2,3} == {2,3,1} # True

'a1' in set1

#      
# set is mutable, editable
#
set1.add('c2')
set1.pop() # getting it out in an arbitrary order
set1.discard('b2')

set2.add('c1')
set2.discard('b2') # nothing happends when the item not present
set2.remove('z2') # KeyError when the item not present

#
# However, the elements of the set are immutable
#
set1[0] = 'z1' # TypeError 'set' doesn't support item assignment


len(set1)
5
len(set2)
4

set1 = {'a1', 'a2', 'a3', 'a2', 'a4', 'a5'} # you can use iterators (list or tuple)
set2 = {'b1', 'b2', 'a1', 'a1', 'b5'} # you can also use {} don't get 


set1.union(set2)
set1|set2 # union of set1 and set2
{'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b5'}

set1.intersection(set2)
set1&set2 # intersection of set1 and set2
{'a1'}


set1.difference(set2)
set2.difference(set1)
set1-set2 # = set1 but not in set2
{'a3', 'a5', 'a2', 'a4'}
set2-set1 # = in set2 but not in set1
{'b2', 'b5', 'b1'}

set3 = {'a1','a2'}
set3.issubset(set1)
set1.issubset(set3)

set1 ^ set2 # (set1 | set2) - (set1 & set2)

set1 <= set2 # try it in Python shell
False
set1 >= set2 # try it in Python shell
False
set3 = {'b1', 'b2'}
set3 <= set2 # subset (all inclusive)

a = set('foo') # removing the dups try it in Python shell
a = set([1,2,3]) # individualize all the element of the iterable as a single item
a 
# output: {'o', 'f'} since 'o's are repeated


# note that there is no accessor to an item in a set since it is unrodered data type
# only way you can access is via for loop (traversing)
# to print the elements in a set
for d in set1:
    print(d)

#****************************************************************
# String
#****************************************************************
string1 = ""
string1 = "20190450 Oct 17 20:29  Information ESENT 916 DllHost"

# How to access values with slicing
string1[0]
string1[-1]
string1[0:10]
string1[12:30]
string1[::-1] # reverse the string

# replace(), strips(), [r|l]find('x')
newstring = string1.replace('2019', '2020')
string1 = string1.replace('2019', '2020') # not modifying the string

# Technicailly speaking what immutable means, you cannot
# modify it directly
string1[0] = 'X' # immutability

# -- then is an integer immutable?
# -- how about boolean? --> They are immutable

'T' in string1
False
'K' in string1
True

for i in string1:
  print(i)


# built-in function
str1 = "$ 2145"
str1.isalnum()
str1[0].isnumeric()
str1[1].isspace()
str1.startswith(' ')
str1.startswith(' ')

str1 = "1423"
str1.isalpha() # True
str1 = "1423 "
str1.isalpha() # False (blank space character added at the end)

str1 = '      test '
str1.lstrip() # removing white spaces before and after
str1.rstrip() # removing white spaces before and after
str1.strip()  # removing white spaces before and after

str1.find('t')
str1.rfind('t')

# built in functions
str1 = "This is CityU"
str1.upper()
'THIS IS CITYU'
str1.lower()
'this is cityu'
str1.lower().upper()

# split() removes the character and split

str1 = "Today is Thrusday, and\tI cannot wait for the weekend!"
str1.split() # split on all white spaces including tabs and newlines, empty space
str1.split(' ', 2) # split for the only first 2 items
str1.split(',')

# printing justification

str1.rjust(100, ' ')
str1.ljust(100, ' ')
str1.cjust(100, ' ') # <-- error
str1.center(20, '*')

print("{:>100}".format(str1))
print("{:<100}".format(str1))
print("{:^100}".format(str1))


# special escape character
#print('this is David's worksplace') # error!
print("this is David's worksplace")
print('this is David\'s worksplace')

print('David said "hi"')
print("David said \"hi\"")
print("David said \t \"hi\"")
print("David said \n \"hi\"")
print("David said \a \"hi\"") # Windows/OS default notification bell
print("David said \v \v \"hi\"")

# multiple lines
print(''' Hi David
How are you?
Bye!''')
print('Hi David\How are you?\nBye!')


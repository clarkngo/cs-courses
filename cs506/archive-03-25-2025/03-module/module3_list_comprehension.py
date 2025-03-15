'''
LIST COMPREHENSION:
List comprehensions provide a concise way to create lists. Common applications are to make new lists 
where each element is the result of some operations applied to each member of another sequence or iterable, 
or to create a subsequence of those elements that satisfy a certain condition. (www.python.org)

This is a type of 'programming' design pattnern to create an efficient and compact way of repeated implementation.
It is not delivering any new solutions or new data types but rather new syntax to make iteration faster.

syntax:                [expression for item in list if conditional]
                            |                 |             |
for item in list: ----------|-----------------+             |
    if conditional: --------|-------------------------------+
        expression  --------+

new_things = []
for THING in old_things:
    if condition_based_on(THING):
        new_things.append("something with " + THING)

--->
              -------------------------      +++++      =========================================
new_things = ["something with " + THING  for THING  in  old_things  if  condition_based_on(THING)]
              -------------------------      +++++      =========================================
'''
numbers = []
n = 0
while n < 10:
    numbers.append(n ** 2)
    n += 1

for n in range(5):
    numbers.append(n * 2)
# print(numbers)

numbers = [n ** 2 for n in range(5)]
# print(numbers)

# store the first letter of each word to another list
listOfWords = ["this","is","a","list","of","words"]
items = [word[0] for word in listOfWords ]
Items = [word[0].upper() for word in listOfWords ]


''' you can think of this as a function returning the iterators.. 
that is iteratorable = (for n in range(5))
then do something with the iteratorable (x ** 2, or x * 2, x % 2 etc...)
Finally, these will be stored in to another list (numbers)
'''

'''
syntax:                [expression for item in list if conditional]
                            |                 |             |
for item in list: ----------|-----------------+             |
    if conditional: --------|-------------------------------+
        expression  --------+
'''

# extract all the digits from a string
str = "My address is 15400 1st St SE Bothell WA 98012"
numbers = [x for x in str if(x.isdigit())]

# extract all the non-digits from a string
str = "My address is 15400 1st St SE Bothell WA 98012"
lettersnumbers = [x for x in str if(x.isalpha())]

# more example
L = []
for i in range(10):
    if i % 3 != 0:      # only changes to the previous example
        L.append(i*i)

L = [i*i for i in range(10) if i % 3 != 0]

# first go thru the list, if the list contains odd values
# double the value and store it into doubled_odd[]
numbers = [1,2,3,4,5]
doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)
        print("n = ", n, " value = ", n*2)
# print(doubled_odds)

# the expr for loop inside[] essentially returns a list 
# which will then be stored in another list
doubled_odds = [n * 2 for n in numbers if n % 2 == 1] 

# how about file handler?
# read a file, then print a line that contains a word "image"
with open('test.txt', 'r') as f:
    lines = [line for line in f if "image" in line]
    lines = [print(line) for line in f if "image" in line]
print(lines)

# Let's see how this comprehension can be used in conjunction with functions
# create a double (*2) function
def double(x):
    return x * 2
# can I use list comprehension calling the function when a value is even?
doubled = [double(x) for x in range(10) if x%2 == 0]

# double the value if a value is divisible by 2 and 5 (which is 10s)
num_list = [double(y) for y in range(100) if y % 2 == 0 and y % 5 == 0]
print(num_list)

'''
Comprehension is short and compact and precise but Loop is more general expression.
For instance, when you want to make any modification, Loop is easier, than Comprehension
for n in range(5):
    numbers.append(n ** 2)
    foo(numbers) <-- got added later 
'''        
# let's flatten a 2D matrix to 1D list
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = []

for rows in matrix1:
    for row in rows:
        matrix2.append(row)
# print(matrix2)
# 
# Nested for loops
#
matrix2 = []
# matrix2 = [row for row in matrix1 for r in row]
matrix2 = [row for rows in matrix1 for row in rows] # pay attention to 'what gets stored eventually'
# print(matrix2)

# Challenge Question:
L=[]
for i in range(10):
    for j in [200, 500, 900]:
        L.append([i,j])
print(L)

#Can you convert this nested for loop with list comprehension?
# --> [[i,j] for i in range(10) for j in [200,500,900]]

# What do these comprehension do?
# --> [f(i) for i in range(3)]

# What would be the correct comprehension for the following nested loop?
NL=[]
N = [1, 2, 3, 4, 5]
L = ['A', 'B', 'C', 'D', 'E']
for n in N:
    for l in L:
        NL.append([n,l])

# NL = [[n, l] for n in N for l in L]

''' 
Here is the Dictionary Comprehension
The same principle applies to the dictionary data type
Syntax:
{key: value for (key, value) in iterable}

Let's define a dictionary, and this time, I'd like to swap between keys and values.
'''

# key (no value) from the for loop
# value will be i**2
# output: {0:0, 1:1, 2:4, 3:9, 4:16}
dict = {}
for i in range(4):
    dict[i] = i**2
# print(dict)

# dictionary comprehension
dict = {i:i**2 for i in range(4)}
# print(dict)

numbers = range(10)
dict1 = {}
# Add values to 'dict1' using for loop
for n in numbers:
    if n%2 == 0:
        dict1[n] = n**2

dict1 = {n: n**2 for n in numbers if n%2 == 0}


dict1 = {'a':'apple', 'b':'book', 'c':'cat', 'd':'dog'}
flipped = {}
for key, value in dict1.items():
    flipped[value] = key # make sense?
# print(flipped)

'''
{}
{for key, value in dict1.items()}
{value for key, value in dict1.items()}
flipped = {value for key, value in dict1.items()}
how do we assign a key-value pair in dictionary?
key:value!
flipped = {key:value for key, value in dict1.items()}
Tada!
'''
flipped = {}
flipped = {value:key for key, value in dict1.items()}
# print(flipped)


dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# modifying each value based on keys in the dictionary, for instance (key:value*2)
double_dict1 = {key:value*2 for (key,value) in dict1.items()}
# now let's modify keys based on values (unlikely but for the sake of comprehension topic)
double_dict1 = {key*2:value for (key,value) in dict1.items()}


'''
but which one is easier to read?
(A) flipped = {value:key for key, value in dict1.items()}
(B) flipped = {
                value:key 
                for key, value in dict1.items()
              }

(A) matrix2 = [r for row in matrix1 for r in row]
(B) matrix2 = [
                r 
                for row in matrix1 
                    for r in row
              ]

new_things = [
                "something with " + THING
                 for THING  in  old_things:
                    if  condition_based_on(THING):
             ]

Since Python allows empty lines within {} and [], take advantage of it.
Please note that make the comprehension reading comprehensible and don’t abuse them
I highly recommend writing your comprehensions over multiple lines. 
Comprehensions don’t need to be one-liners to be useful.
'''

'''
using enumerate(list|tuple|string)
produces the pair of value in the input list using numbered index

Enumerate function runs on list, tuple or string and returns index, and element

'''

# enumerate() provides an interation counter of an iterator
#             includes a counter to an iterable and returns it in a form of enumerated object.
#             is used in for loops and be converted into a list or tuples using list()
# using enumerate, list can be written as dictionary
# Syntax: enumerate(iterable, start=0) # iterable = {list, tuple, dict, string, set}

L1 = ['eat', 'sleep', 'repeat']
S1 = 'you'
T1 = ('eat', 'sleep', 'repeat')

obj1 = enumerate(L1)
obj2 = enumerate(S1)
obj3 = enumerate(T1, start=2)

# Let's use the enumerate object in loops
for item in enumerate(L1):
    print(item) # (0, 'eat'), (1, 'sleep'), (2, 'repeat') --> tuple!

for count, ele in enumerate(T1):
    print(count, ele)

letters = ['a', 'b', 'c', 'd']
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
# the following comprehension makes the input list into dictoinary
# using enumerate()
{j:i for i, j in enumerate(letters)}

dict1 = {}
for i, j in enumerate(letters):
    dict1[j] = i
# print(dict1)

colors = ["red", "blue", "yellow"]
for index, color in enumerate(colors):
    print(index, color)

colors = [('red', 256), ('green', 128), ('blue', 0)]
for a, (b, c) in enumerate(colors): # for a, (b, c) in enumerate(colors): be careful with # of values
    print(a, b, c)


# Module 1 topic: Variable, type casting, _, arithmetic, logical operators, precedence in operators

"""
This is the first Python program.
Show in the python shell (python and ipython)
Alsho show in the demo.py and run it
"""
str = "Hello World (from demo.py)!"
print(str)


import math

#****************************************************************
# Variables and print the values
#****************************************************************
# Value assignment
x = 1                       # int
y = 3.14                    # float
name = 'City U @ Seattle'   # str
is_cool = True              # bool

# Assign binary value to the variable
# assign number as binary 
# prefix 0b 
num1 = 0b111101
print("value = ", bin(num1))
num2 = 0b110101
print("value = ", bin(num2))

print(0b10) # binary
print(0o10) # octal
print(0x10) # hexadecimal

# Multiple assignment
x, y, name, is_cool = (1, 3.14, 'City U @ Seattle', True)
x, y, name = (1, 3.14, 'City U @ Seattle', True) # Error!
x, y, name, _ = (1, 3.14, 'City U @ Seattle', True) 

# Variable naming convention

# print the values of each variable
print(x)
print(name)

print(type(x))          # getting the type information of variables
print(type(is_cool))

# Type conversion (casting)
x = str(x)
print(type(x))          # getting the type information of variables

y = int(y)
print(type(y))          # type conversion

z = float(y)
print(type(z))  
print(z)

int(3.14)
int("3.14")
int("test")

float(3)
float("3.14")
float("test")

str(3.14)
str(124_243)


a = 'City'
b = 'University'
(a + ' ' + b)
('a' + 'b') * 5

brd = '''
-+-+-
X| |
-+-+-
 |O|
-+-+-
 |O|O
-+-+-
'''
print(brd)

#****************************************************************
# The following statements can be executed at the Python Shell
#****************************************************************

a = 5
b = 6
c = 2
a/c
b/c

# unary operator
>>> a ** c
>>> -b
>>> +b
>>> a//c    # What do you think this operator does?
>>> round(a/c)
>>> round(3.141592, 3)
>>> round(3.141592, 4)
>>> round(3.141549, 4)

>>> a + b
>>> a - b
>>> a * b
>>> a / b
>>> a % b
>>> abs(-1)
>>> a**b
>>> math.sqrt(a)


num1 = 0b111101
num2 = 0b110101

bin(num1 | num2)
bin(num1 & num2)
bin(num1 << 2)
print (num1 << 1) # x 2
print (num1 << 2) # x 4


#
# associativitiy precedence
# go to help("*") then verify they are in the same precedence
#
>>> 5 * 2 % 3 
>>> 5 * (2 % 3)
# L -- R (if they have the same precedence, L first)
# but here is one operator that has R-L associativity
>>> 2 ** 3 ** 2
>>> (2 ** 3) ** 2
>>> 2 ** (3 ** 2) # right first then left

# type precedence int * float = float because of larger size allocated for the data type
# import sys     sys.getsizeof(z)
>>> 2 * 2.3

>>> 10 > 100
False
>>> 10 != 100
True
>>> 'str' == 'str'
True
>>> 'str' == 10
False
>>> (10 < 100) and (1 > 0)
True

# Truth table
>>> True and True
True
>>> False and True
False
>>> not (10 < 100)
False
>>> not (not (10 < 100))
True


round(int(8.5 + 0.5))


# you can start adding two numbers, and python will temporarily store the value to _

5+8
_
_ + 10
a = _

# don't care, ignore me, I'm not that important at the moment
a, b, c = (1,2,3)
a, _, c = (1,2,3)
a, *_, b = (1, 2, 3, 4, 5, 6, 8)

# slight var. name variations for easy readability
min_ = min([1,2,3,4])

# digit separator

x = 1000000000
x = 1_000_000_000

int   = 32 bits (4 bytes)
float = 64 bits (8 bytes)




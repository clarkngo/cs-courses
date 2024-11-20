# Module 1 topic: IF, nested, LOOPS, nested, User Input, Range


# 
# -- Now let's look at IF statements
#
num = 3
# if 'condition':
#    'statement(s)'
# else:
#    'other statement(s)'
if num > 0:
    print(num, "is a positive number.")
print("program continues outside if block")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("program continues outside if block")


num = -1
if num > 0:
    print(num, "is a positive number.")
else:
    print(num, "is a negative number.")
print("program continues outside if block")

#
# -- Here is how to read an input from the command prompt
#    input will be always string so get ready to conver as needed
#

print("Please Enter an integer number: ")
num = int(input())

num = int(input("Please Enter an integer number: "))
print("The input string is :", num)

if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print(num, " is zero.")
else:
    print(num, " is a negative number.")

#
# -- now let's look at the nested if blocks
#

if num >= 0:
    if num == 0:
        print(num, "is zero")
    else:
        print(num, "is a positive number")
else:
    print(num, " is a negative number")


print("Please Enter an integer number")
num = int(input())

if num > 0:
    print(num, "is a positive number")
elif num == 0:
    print(num, "is zero")
else:
    print(num, " is a negative number")


# -- Before we jump into the loop controls, I'd like to briefly introduce
#    bulit-in range() function. This function creates a list of 
#    consecutive numbers from given input values, range(start, stop and step)
# these can be used as index/controller for looping or iteration over arrays 
# like list, tuple, dictionary, set.

print(range(10))
range(0, 10) # range object
print(list(range(10))) # we need to list-ify
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10, 2)))
[0, 2, 4, 6, 8]
print(list(range(0, 10, 3)))
[0, 3, 6, 9]

# simple for loop whlie printing a number
for i in range(10):
    print(i)

# simple for loop whlie printing an even number
for i in range(30):
    if i%2 == 0 and i%5 == 0:
        print(i)

#
# Before I go further, let me introduce how to generate random numbers.
#
import random
num = random.randint(1,6)   # inclusive end for a single random value
num = random.randrange(1,6) # exclusive end for a single random value
rlist = random.sample(range(0, 30), 5) # 5 random numbers from 0 to 29
m = ['O', 'X']
random.choice(m) # random choice from non-empty list

for i in random.sample(range(0,30), 10):
    print(i)

for i in random.sample(range(0,30), 10):
    print(i)
else: # else block
    print("no more item in the list")

#
# Sum the list of 10 random numbers
#
list_num = random.sample(range(0,30), 10)

# initialize final sum
sum = 0
for val in list_num: # adding the values in the list
    sum = sum + val
print("total sum is ", sum)

sum = 0
for i in range(len(list_num)): # using the range to traverse
    sum = sum + list_num[i]
print("total sum is ", sum)


#
# Nested loop
#
for i in range(1,5):
    for j in range(i):
        print(i, end=" ")


ttt = [['X', 'O', 'X'], ['-', 'O', 'X'], ['X', '-', '-']]
for i in range(len(ttt)):
    for j in range(len(ttt)):
        print(ttt[i][j], end=" ")
    print("\n")


# Sum only even numbers, x = user input
# Challenge1. Write a program to sum first x even numbers, where x is a user input

list_num = [6, 2, 3, 5, 2, 11, 4, 9, 22, -3, 9, 13, 10, 1]
i = 0
sum = 0
while i < len(list_num): #try while list_num[i]%2 == 0: then fix
    if(list_num[i]%2 == 0):
        sum = sum + list_num[i]
    i = i + 1
print("The total sum of even numbers is ", sum)

i = 0
sum = 0
while i < len(list_num): 
    if(list_num[i]%2 == 0):
        sum = sum + list_num[i]
    i = i + 1
else:
    i = 0
    print("Outside while loop and the final sum is ", sum)


# with the user's input character, the program prints a message that says vowel or not. If not vowel, it continues if not, stops.
vowels = "aeiouAEIOU"
#infinite loop
while True:
    v = input("Enter a vowel: ")
    v = v.lower()
    if v in vowels:
        break
    print("No! That's not a vowel. Try again")
    print("You entered ", v)
print("Good job!")



#
# -- Different ways to print values in Python
#

name = 'Tom'
age  = 40
# Concatenation
print('Hello, My name is ' + name + ' and I am ' + str(age)) # age --> str(age)

a = 123
'this is a = %d' %(a)
'this is a = 123'
'this is a = %f' %(a)
'this is a = 123.000000'
"this is a = %1.f" %(a)
"this is a = %2.f" %(a)
"this is a = %3.f" %(a)
"this is a = %4.f" %(a)
'this is a = %.2f' %(a)
'this is a = 123.00'
x = 'Friday'
print("Today is %s and I am %d." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

# %d for integer
# %f for float
# %.2f for decimal points .XX
# %X.2f for decimal points -----.XX
# %s for string


int_numb = 12
my_str   = 'This is my string'
flt_numb = 3.14159

print(int_numb, my_str, flt_numb)
# basics
print("int_numb = ", int_numb)
print("flt_numb = ", flt_numb)
print("my_str = ", my_str)
# string-fy
print("int_numb = " + str(int_numb))
print("flt_numb = " + str(flt_numb))
print("str_numb = " + my_str)

# formatted
s = "Tom"
age = 123
s = f'Hello, My name is {s} and I am {age}'
print(s)

print(f'int_numb = {int_numb}, flt_numb = {flt_numb}, str = {my_str}')
print("{}! {}!".format("Hello", "Seattle")) 

print(f"{}! {}!".format("Hello", "Seattle")) #Error




# adjustment
"|{:<30}|".format("how are you?") #right adjustment
"|{:^30}|".format("how are you?") #center adjustment
"|{:>30}|".format("how are you?") #left adjustment



# formating by position
print('first number is {value1} and second number is {value2} then final string is \'{value3}\''.format(value1 = int_numb, value2 = flt_numb, value3 = my_str))
print('first number is {v1} and second number is {v2} then final string is \'{v3}\''.format(v1 = int_numb, v2 = flt_numb, v3 = my_str))
print('first number is {0} and second number is {1} then final string is \'{2}\''.format(int_numb, flt_numb, my_str))
print('first number is {} and second number is {} then final string is \'{}\''.format(int_numb, flt_numb, my_str))
print("value is {}".format(round(10.92)))



s = "Tom"
print(f'Hello, My name is {s} and I am {age}')
s = f'Hello, My name is {s} and I am {age}'
print(len(s.upper()))
print(s.capitalize())
print(s.replace("Tom", "Jin"))

# Sample program to gather input and manipulate the input.

print("Please enter your name")
name = input()
print(f"you are {name}")
print("How old are you?")
age = int(input())
new_age = age + 1
print(f"you're {age} and you will be {new_age} next year")


x, y = input("Enter a two value: ").split()# default delimiter = " "
print("Number of boys: ", x) 
print("Number of girls: ", y) 



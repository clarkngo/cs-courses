
# -- function definition
#  Function DEFINITION 
# def function_name(parameters):
#     ''' doc string or help(function_name), function_name.__doc__ '''
#     statements
#     return something
#

# -- function definition without args, and return statements
def function1():
    ''' Function Name: function1()
        Argument: None
        Return Value: None
        Summary: Prints a greeting message '''
    name = "Harry"
    print("Hello, ", name, "! Good morning!")

def function2():
    ''' Function Name: function1()
        Argument: None
        Return Value: None        
        Summary: Prints a greeting message '''
    name = "Sally"
    print("Hello, ", name, "! Good morning!")

function1()
function2()

# -- function definition with arguments
# this function prints the name + message inside the function greeting
def greeting (name):
    print("Hello, " + name + "! Good morning!")

print("What is your name? ")
name = input()
greeting(name)

# -- function definition with return value
# this function returns a string that has the name and message,
# then it prints the message
def greeting2 (name):
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
name = input()
print(greeting2(name))


# -- MORE on function arguments
#    how about passing the message and name to be more flexible
def greeting3 (name, msg):
   print("Hello, " + msg + "! " + name)

print("What is your name? ")
name = input()
print("Enter the greeting message ")
msg = input()
greeting3(name, msg) # try without msg and explain the error message

#
# -- can we pass a list to a function?
#    I have a list of people and would like to greet individually with message.
def greeting_my_friends(friends_list, msg):
    for f in friends_list:
        print(msg + " " + f + "!")

friends1 = ("Jason", "Brenna", "Shannon")
friends2 = ["Jason", "Brenna", "Shannon"]

msg = input("Enter the greeting message ")
greeting_my_friends(friends1, msg)
greeting_my_friends(friends2, msg)

#
# passing a list, set, tuple
def addnumbs(x, y):     # a = [3, 4]
# def addnumbs(x, y, _):  a = [3, 4, 6]
# def addnumbs(x, y, *_): a = [3, 4, 5, 6, 7]
    return x+y
a = [3, 5]
# print(addnumbs(a)) --> x[0], x[1] passing a list itself
print(addnumbs(*a)) # list, tuple, set all work the same.

#
# Python program to find the common elements in two lists 
#
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
  
    if (a_set & b_set): 
        print(a_set & b_set) 
    else: 
        print("No common elements")  

a = [1, 2, 3, 4, 5] 
b = [5, 6, 7, 8, 9] 
common_member(a, b) 

a = [1, 2, 3, 4, 5] 
b = [6, 7, 8, 9] 
common_member(a, b) 

#
# -- how about passing a dictionary to a function?
def addnumbs(d):     
    s = 0
    print(d)
    for k, v in d.items():
        print(k, " ", v)
        s = s + v
    return s
d = {'a': 1, 'b': 2}
s = addnumbs(d)
print(s)

#
# passing a dictionary
def greeting_my_friends2(friends_dict):
    for key in friends_dict:
        print(friends_dict[key], " " + key + "!") # key 
# d = {key: value} == {'name':'message'}
friends_greeting = {'Jason':'Good morning', 'Brenna':"I miss you", 'Shannon':"How have you been sis!"}

# -- let's look at Scope of Variables
# 1. Local variable, global variable can have the same name
# 2. Local variables means local to the block (scope).
# 3. Local variables cannot be shared with the variable in the global scope.

v = 10 # global variable 
def printnow():
    v = 20 # local variable
    print(v) # you're printing the local v = 20
v = 30 # global variable updated from 10 to 30
printnow() # (local) v in the function is 20
print(v) # you're printing the global v = 30

# 3. Local variables cannot be shared with the variable in the global scope.
# case #1
v = 1
def add_print_X(): # ERROR!
    v = v + 10 # x can be accessed for reading but not writing in a local function # UnboundLocalError: local variable 'v' referenced before assignment
    print(v)
    '''
    Here is the reason why ...
    "v = v + 1"
    ^    ^
    2nd  1st
    1st = reading a global v
    2nd = writing the result to a local which shadows the global v.
    Therefore, Python doesn't know which v to write to, either local or global.
    '''
def add_print_O():
    global v # fix: use global keyword to indicate "i am accessing a global variable called v"
    v = v + 10
    print(v)

add_print_O()
add_print_X()

#
# Let's look at nested functions where you have a choice between global
# and local variables defined in the caller function.
#
v = 1
def printA():
    # v = v + 10 #<- this is unbound error since both local and global exist in a single assignment. 
    global v  # And global key works because it is indeed a global variable.
              # And you only have a global v available, right?
    v = v + 10 # works
    print(v)
v = 10
printA()

#
# # what if there are 2 choices, global vs. other local variables in the caller function, nested functions.
v = 1 # global v
def printA():
    v = 10 # local v in printA
    def printB():
        v = v * 10 # well, the problem is the fact thta printB() has v in the global scope AND v in printA() scope. Which one to use? Previously, i could use global, but now I may sometimes use caller's v. That is when you use nonlocal (caller's scope)
        # Can I use global v here as well? YES of course. 
        # So, the fix is to use global for global v
        #                to use nonlocal for caller's v (printB())
        print(v)
    printB()
    print(v)
v = 10
printA()


#
# Now, tell me what would the output of the following cases when
# using global vs. nonlocal
v = 10 # global variable 
def printA():
    v = 10
    def printB():
        global v 
        '''
                    printB:  300
                    printA:  10
                    main:  300
        '''
        nonlocal v
        '''
                    printB:  100
                    printA:  100
                    main:  30
        '''                    
        v = v * 10
        print("printB: ", v)
    printB()    
    print("printA: ", v) 
v = 30 
printA() 
print("main: ", v) # you're printing the global v

# 
# Summary: When a nested function stack present, the callee (printB) 
# has to know which scope to use. Global or Caller? 
# If Global, use global and If Caller, use nonlocal when read and write are
# happening in a single statement, X = X / 10. Need to be explicit and consistent. Oherwise, Pythong gets confused.
# Note that global and nonlocal maintain the exclusive scope to variables.

#
# More examples of using global and nonlocal keywords
#
from colorama import init
from colorama import Fore, Back, Style

s = 0 # global
def print1():     
    # global s
    s = 100
    print(Fore.LIGHTYELLOW_EX + "print1-A---: %03d at %d" %(s, id(s)))
    def print2():
        nonlocal s # go to the state
        s = s + 200 # 100 + 200
        print(Fore.GREEN + "print2----------: %d at %d" %(s, id(s)))
        return
    print2()
    print(Fore.LIGHTYELLOW_EX + "print1-B---: %03d at %d" %(s, id(s)))
    return

# init for colorama module
init() 

# main starts
print(Fore.RED + "main-A:   %03d at %d" %(s, id(s)))
print1()
print(Fore.RED + "main-B:   %03d at %d" %(s, id(s)))


#Global v Nonlocal----------------------------------
name = "Harry" # remove when nonlocal
def greeting2(name):
    name = "Hello, " + name + "! Good morning!"
    print("greeting2-A = " + str(hex(id(name))))

    def greeting3():
        global name # this will print the same address as name (global)
        # nonlocal name # this will fix the problem of getting outside of local scope telling that "name is not defined in the local scope and to keep search outwards"
                      # Since the assignment limits the search for x to the local scope, it can't be found and I get the error.
        print(name) # when I do this, I access via Local scope(first) -> Enclosing scope(second) -> Global(third) -> Built-in(last)
        # therefore this 'name' is enclosed name defined in greeting2()
        name = name.upper() # new object at a new address
        print(name)
        print("greeting3 = " + str(hex(id(name))))
        return name
    
    print(greeting3())
    print("greeting2-B = " + str(hex(id(name))))
    return name

print("What is your name? ")
# pdb.set_trace()
name = input()
print("main-A = " + str(hex(id(name))))
print(greeting2(name))
print("main-B = " + str(hex(id(name))))
print(name)


# -- what is wrong with the following code and how would you fix
#   UnboundedLocalError?
# Note that the assignment limits the search for x to the local scope, it can't be found and I get the error.
def foo():
    x = 23
    def bar():
        # the reason why we are getting this error is 
        # self modifying operation such as += which means READ/WRITE operations at the same time
        x = x + 1 # fix via nonlocal. nonlocal / global are exclusive
        return x
    return bar()
print(foo())



# This example will throw an error UnboundedError
#----------------------------------------------------
def greeting2 ():
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
# this name is global
name = input()
print(greeting2())
#----------------------------------------------------

#Fix1 (use global)-------------------------
#  (1) remove global or use it as local 
#  (2) use global key to modify
def greeting2 ():
    global name
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
name = input()
print(greeting2())
#---------------------------------------------------

#Fix2 (passing the argument)-------------------------
def greeting2 (name):
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
# this name is global
name = input()
print(greeting2(name))
#---------------------------------------------------

#
# -- another example of using variable at a different scope
#
# name = "Harry" # this is a global variable
# def name_change():
    #    global name    accessing the global var
    # name = "Sally"
    # print("inside name_change(): ", name) # Sally (from local)

# name_change()
# print("outside name_change(): ", name) # Harry (from global)
name = "Johnson" # this is a global variable
def function1():
    name = "Harry"
    def function2():
        # nonlocal name #(follow the block)
        name = "Sally"
        print("Function2: ", name)
    function2()
    print("Function1:", name)

print("Outside Before:", name)
function1()
print("Outside After:", name)

'''
#1
c:\CityU\CS160\M1>test.py --> without nonlocal name in function2()
Outside Before: Johnson
Function2:  Sally
Function1: Harry
Outside After: Johnson
'''
'''
#2
c:\CityU\CS160\M1>test.py --> with nonlocal name in function2()
Outside Before: Johnson
Function2:  Sally
Function1: Sally <-- * name modified in function1() ie. Harry is replaced by ="Sally" assignment
Outside After: Johnson
'''

'''-------------------- OPTIONAL (built-in) try to avoid using builtin names ----------------------'''
'''
x = 'global x'
def foo():
    # y = 'local y'
    # global x
    x = 'local x'
    print (x)
foo()
print(x)
'''

'''
def test(z):
    x = 'local x'
    print(z)

test('local z') # try z out of scope
'''
''' built-in (min vs min(list))
# import builtins
# print(dir(builtins))

 def my_min():
    pass

m = min([5, 2, 1, 3])
print (m)
'''
'''
def outer():
    x = 'outer x'
    def inner():
        #nonlocal x # only available in the nest function blocks
        x = 'inner x' 
        print(x)
    inner()
    print(x)
outer()    
'''

''' (summary)
x = 'global x'
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x' 
        print(x)
    inner()
    print(x)
outer()    
print(x)
'''


def greeting3 (name, msg = "Good Morning!"): # default argument
   print("Hello, " + name + "! " + msg)

print("What is your name? ")
name = input()
print("Enter the greeting message ")
msg = input()
if len(msg) == 0:
    greeting3(name)
else:
    greeting3(name, msg) 













''' Exception handling 
def division(divisor):
    return 100/divisor
'''
def division(divisor):
    try:
        return 100/divisor
    except ZeroDivisionError:
        print('Error: Invalid Argument.')
        # return -1

print(division(10))
print(division(0)) 
print(division(50))


# Generator is very close to list comprehension
# Generator expression



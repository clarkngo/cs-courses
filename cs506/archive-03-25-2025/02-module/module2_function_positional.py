import pdb

#
# -- positional argument using a builtin function
complex(3,8) # 1st to 1st, 2nd to 2nd 3+8j
complex(8,3) # 8+3j
# Positional arguments can also be passed to a function using an iterable object.
# function (*iterable) # iterables are list, tuples, sets etc where one element can be accessed one at a time via for loop
x = [3, 8]
complex(*x)

# help(complex) # that shows real and imag keyword
y = {'real':3, 'imag':8}
complex(**y)

# -- keyword argument by providing keywords with intial value to it
#    this overrides the positional argument when all the parameters are kwargs
complex(real=3, imag=8)
complex(imag=8, real=3)

# -- however, if argument list contains both positional and keyword arguments,
#    then the order still matters in keywords with default value.
#    the specified keyword argument should come later
complex(real=3, 8) # this is NOT ok  (SyntaxError: positional argument follows keyword argument)
complex(3, imag=8) # this is ok  (Python think that default argument is an optional!


# -- more examples in the positional argument
#
def division_op(x, y=1):   # x = pos. argument, y = 1 keyword's value (optional)
#def division_op(x=1, y):   # the specified keyword/argument should come after no default -- not good
    ret = 0
    if y: 
        print("x = ", x, " y = ", y)
        ret = x/y
    else: # if y == 0
        print("x = ", x)
        ret = x
    return ret

result = division_op(4, 10)# positional arguments
result = division_op(4)# positional arguments
result = division_op(y=4, x=10) # positional arguments it's ok
result = division_op(y=4, x) # not allowed the default argument before keyword
# (SyntaxError: positional argument follows keyword argument)

#
# -- Arbitrary arguments
def greeting3 (*names): # receive those parameters in a form of list
    for name in names:
        print("Hello ", name)
# std IO
greeting3("David", "John", "Jin-")
greeting3("David", "John-")
greeting3("David-")

#
# More example
def foo(*x):
    s = 0
    for v in x:
        s += v
    return s
print(foo(1))
print(foo(1, 2))
print(foo(1, 2, 3))
print(foo(1, 2, 3, 4))

# -- compare with an argument in list
#
def addnumbs(x, y):     # a = [3, 4]
    return x+y
a = [3, 5]
print(addnumbs(*a)) # '*' = passing or receiving "more than 1"

# -- let's expand a little more
#    
def addnumbs(*x):
    s = 0
    for v in x:
        s += v
    return s

x = [1, 2, 3, 4]
print(foo(*x)) # when *x used, i am passing 1, 2, 3, 4 individually.
               # this makes the addnumbs to receive *x (multiple parameters)
               # otherwise, i get the following TypeError:
               #      takes 1 positional argument but 4 were given
x = [1, 2, 3, 4, -4, -3, -2, -1]
print(foo(*x))


# -- Let's try more on Arbtrary arguments on computing an area
#    of different shapes by passing a tuple
# compare and contrast how they pass a tuple
#                v                            v  v
def compute_area(dim): result = compute_area((3, 2))
#                v                            vvvv
def compute_area(*dim): result = compute_area(3, 2)
#
def compute_area(*dim): 
    result = 0
    if (len(dim) == 1): # x and pi for 2D circle
        result = 3.14 * dim[0] ** 2
    elif (len(dim) == 2): # x, y for 2D rect
        result = dim[0] * dim[1]
    elif (len(dim) == 3): # x, y, z for 3D volumn
        result = dim[0] * dim[1] * dim[2]
    else:
        print("invalid input params")
    return result

result = compute_area(2)
print("result is ", result)
result = compute_area(3, 2)
print("result is ", result)
result = compute_area(3, 2, 9.2)
print("result is ", result)
i = [2,3]
result = compute_area(*i)
print("result is ", result)

# -- Let's now use the key-value words argument for different shapes
#
def compute_area_new(**kwargs): 
    print(kwargs)
    ret = 0
    if len(kwargs) == 1:
        ret = kwargs['radius'] ** 2 * 3.14
    elif len(kwargs) == 2:
        ret = kwargs['width'] * kwargs['width']
    elif len(kwargs) == 3:
        ret = kwargs['width'] * kwargs['height'] * kwargs['length']
    return ret

result = compute_area_new(width = 2, height = 3, length = 2)
print(result)
result = compute_area_new(radius = 3)
print(result)


def foo(arg, *args, **kwargs): # arg is required! *args (pass by value <- tuple) without a star (pass by ref.)
    print(arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo() # error since arg <- required not present
foo("event log failed")
foo("event log failed", "abc")
foo("event log failed", 1,2,3,0.23)
foo("event log failed", 1,2,3,0.23, key="name", value="Jin Chang")

#
# general rule when a list or tuple are passed in
# functional arguments are recevied as tuple when * is used.
#
def addnumbs(x): 
    print(x)    
    x[0] = -99
    
a = [3, 5, 39]
addnumbs(a)
print(a)
#  a -> x : a list to a list
# *a -> x : items to a list # error
#  a -> *x: a list passed in as a tuple the list inside ([...]) cannot modify # error immutable
# *a -> *x: items are passed in as a tuple (...) # error immutable

#
# What if you want to make the change persisted?
#
# pass by value *a -- *x
# even if you modified the value inside the function,
# the value doesn't persist outside
def addnumbs(*x): 
    print(x)
    y = list(x)
    y[0] = -99
    x = tuple(y)
    print(x)
    
a = [3, 5]
b = (3, 5)
c = {3, 5}
addnumbs(*a)
print(a)

# Now this will make the changes persisted.
# pass by reference sending a single, receiving multiple
def addnumbs(*x): 
    print(x)
    x[0][1] = -99 # 
    print(x)
    
a = [3, 5]
b = (3, 5)
c = {3, 5}
addnumbs(a)
print(a)

# passing  a  --- receiving  x --> list-list, tuple-tuple no change in mutability -- pass by value/reference
# passing *a  --- receiving *x --> tuple (immutable) -- pass by value
# passing  a  --- receiving *x --> tupled list/set (mutable) -- pass by reference
# passing *a  --- receiving  x --> 2 passing and 1 receiving error!




# # Challenge Question
# -- I want you to now crunch some numbers for me.
# -- your function "compute_area()" does the following
#    name: compute_area
#    args: width and height of a rectangle
#    return value: the area of the rectangle
#    summary: compute the area by multiplying those 2 numbers
# -- after you got the value returned from compute_area
#    print 2 decimal points (extra point)
#
# (ANS)   
# def compute_rect(D):
#     return D[0] * D[1]
# D = [100, 2.1]
# print('{:.2f}'.format(compute_rect(D)))
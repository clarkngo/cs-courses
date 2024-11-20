#
# lambda argument(,) to the expression : expression to be evaluated
#
lambda  a : a + 10
# nameless comes here...
(lambda a : a + 10) (10)
(lambda a : a + 10) (-10)

add = lambda a : a + 10
add(1)
add(2)


F = lambda x : x * x
F(5, 2)

F = lambda x, y: x * y
F(5, 2)

F = lambda x, y, z: max(x, y, z)
F(4, 2, 1)

F = lambda *x : max(*x)
F(10, 2, 8)
F(10, 2, 8, 9, 11, 23)

# "The value of the key parameter should be a function" that (1) takes arguments and (2) returns a key to use for sorting purposes. 
# [(x, y, z)]
# I want to go thru a list, and sort by either, X x[0], Y x[1] or Z x[3] value in order regardless

P = [(1, -10, 0), (3, 8, -9), (-2, 2.3, -8.2), (3, 11, -8)]

# help(P.sort) (*, key=None...)
# help(sorted)
#                  input arg   
#                        return val.
#                      v   vvvv
sorted(P, key = lambda x : x[0])
sorted(P, key = lambda x : x[1])
sorted(P, key = lambda x : x[2])

# Lambdas are limited to one expression only, the result of which is the return value.
# I want to go thru a list, and sort by the name in alphabetical order
S = ["ethan", "danny", "Cathy", "bob", "Adam"]
sorted(S, key = lambda s : s.upper())


# function template (functional programming)
def multnum_x(n):
    return lambda x : x * n

# creating a template
# f = lambda x : x * 3
multi3 = multnum_x(3) # n = 3
multi3(10)

multi5 = multnum_x(5) # n = 5
multi5(20)

multi100 = multnum_x(100) # n = 5
multi100(0.3)

multnum_x(100)(0.3) # compact version


L = [10, 20, 30, 40]
comp = lambda x: x > 25
for v in L:
    print(f'{v} ', comp(v))


# Both list.sort() and sorted() have a key parameter to specify a function to be called 
# on each list element prior to making comparisons.
def intify(x):
    try:
        x = int(x)
    except:
        x = 0
    return x

sorted(['7', "0", 5, 2, 1, "-1", -2, "9"], key=intify)    

#
# Challenge question
#  What does the following lambda function do?
#  ans: extracting the 2nd to the last digit in a given number
func = lambda p: int(p/10)%10
func(1202)

def C2F(C):
    F = []
    for v in C:
        F.append(v * (9/5) + 32)
    return F

C = [0, 36, 85, 100] # celcius temperture     
# equivalent lambda expression is
list(map(lambda x:(x*(9/5) + 32), C))    
list(map(lambda x:(x * 6.65), C)) # converting dollar to yuan

def over_10(IN):
    OUT = []
    for v in IN:
        if v > 10:
            OUT.append(v)
    return OUT

IN = [0, 3, 15, 20]
# equivalent lambda expression is
list(filter((lambda x: x > 10), IN))

# Filtering the even numbers from a given list
def even_func(x):
    if x % 2 == 0:
        return True

L = [29, 21, 88, 102]
list(filter(even_func, L))
list(filter((lambda x: x % 2 == 0), L))

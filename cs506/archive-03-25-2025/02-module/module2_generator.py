# Generator
# 

mylist = [1, 3, 5, 7, 9, 11]

def funct1(nums):
    for num in nums:
        yield num*num # yielding (soft returning) the n*n while iterating


sq_val = funct1(mylist)

for i in sq_val:
    print(i)
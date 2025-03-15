#
# - File operation
#
# 
# --- printing the strings obtained from a user input and write to a file
#
try:
    f = open('test.txt', 'r')
    contents = f.read()
    print(contents)

finally: #This type of construct makes sure the file is closed even if an exception occurs.
    f.close() # <<-- to ensure the file is closed after finished reading.

try:
    f = open('test1.txt', 'w')
    print('What do you want to say?')
    str = input()
    f.write(str)

finally: #This type of construct makes sure the file is closed even if an exception occurs.
    f.close() # <<-- to ensure the file is closed after finished writing.

#
# -- appending to the EOF
#
try:
    f = open('test1.txt', 'a')
    print('What do you want to say again?')
    str = input()
    f.write("\n")
    f.write(str)
    
finally: #This type of construct makes sure the file is closed even if an exception occurs.
    f.close() # <<-- to ensure the file is closed after finished writing.


# 
# -- traditionally, we have been using open -- close a file for any operation
#
f = open('test.txt', 'r')
contents = f.read()
print (contents)
f.close()

#
# -- new way of opening a file with the context manager
#
with open('test.txt', 'r') as f:
    contents = f.read()
    print (contents)
    # no need to close with the context manager!!

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

line_number = 1
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(str(line_number) + ") " +line)
            line_number = line_number + 1


#
# for a demo purpose, I'll just simply open for reading
f = open('test.txt', 'r')
f.readline() # read a line at a time
f.readlines() # read all the lines
['This is the first line\n', 'This is the second line\n', 'This is the third line\n', 'This is the forth line\n', '\n']
f.read() # read a whole contents
f.read(5) # raad next 5 characters

# file pointer, f.tell(), f.seek(0) // rewind
f.tell()
99
f.seek(0) # back to 0th character, the beginning of the file
0
f.close()


#
# - Exception Handling
#

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


bGo = True
i = 0
while bGo and i < 3:
    try:
        x = (10/int(input("Enter a denominator : ")))
    except ZeroDivisionError:
        print("Zero Division Error is raised!")
        bGo = False
    except ValueError:
        print("Enter an integer!")
        bGo = False
    i = i + 1
# unexpected operation was executed. cannot trust x
if bGo == True:
    print(x)
else:
    x = -999
    print("not so trustful value!", x)



L = ['3', '8', '2', '10', '-9', '2', "", 'c']
for i in range(10):
    try:
        if(int(L[i])):
            print(L[i])
    except ValueError:
        print("Unexpected input value!")
        continue
    except IndexError:
        print("Out of bound!")
        continue
    # except (ValueError, IndexError):
    #     print("Fix your darn program!")
    #     continue


try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:# as fnf_error:
    print("ERROR:", end="")
    # print(fnf_error)

a = [0,1,2]
try:
    b = True
    if b == False:
        if(a[0] == 0):
            raise Exception("Oh My Exceptoin: Divided-by-zero??")
        a[2] = a[1]/a[0]
    else:
        print('fourth element is %d ' % a[3])
except IndexError as error:
    # print("Out of Bound!")
    print("Exception: " + str(error))


L = [2, 3, 4, 2, -3]
for i in range(len(L)):
    print(L[i])
    assert(L[i] > 0), "Cannot have a negative value!"


import traceback
try:
    raise Exception("This is the error message")
except:
    errorFile = open('errorInfo.log', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was writtent to errorInfo.log')


#
# OS modules
#

import os
os.getcwd()
os.chdir('c:\\')
os.getcwd()
os.chdir('C:\\Windows')
os.getcwd()
c = os.getcwd()
os.chdir('c:\\')
os.chdir(c)
c = os.getcwd()
os.makedirs('test')
os.path.getsize('C:\\Windows\\system32\\explorer.exe')
3486320
os.path.getsize('C:\\Windows\\system32\\calc.exe')
26112

os.path.exists('C:\\')
True
os.path.exists('R:\\')
False
os.path.exists('c:\\qvue.exe')
True
os.path.exists('c:\\qvue.dat')
False
os.path.isfile('c:\\qvue.dat')
False
os.path.isfile('c:\\qvue.exe')
True
os.path.isfile('c:\\JC')
False
os.path.isdir('c:\\JC')
True


''' FILE OPERATION '''
import os

totalsize = 0
num_files = 0

for filename in os.listdir('C:\\Windows'):
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Windows', filename))
    num_files = num_files + 1
    print(filename)

print(totalsize, "bytes")
print("number of files: ", num_files)



''' PDB '''
'''
Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where
'''
def function1(a, b):
    return a/b
def function2(x):
    a = x
    b = x - 1
    return function1(a, b)

function1(1)
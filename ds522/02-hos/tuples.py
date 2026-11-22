tup1 = ("physics", "chemistry", 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

empty_tup = ()
print(empty_tup)

empty_tup = (1, 2, 3)
print(f"Assign values to the previously empty tuple: {empty_tup}")

str_tup = ("alpha", "bravo", "charlie")
int_tup = (0, 1, 2, 3, 4, 5)
mix_tup = (20.50, True, "Math", -50, 1+2j)

print(f"A tuple of strings: {str_tup}")
print(f"A tuple of integers: {int_tup}")
print(f"A tuple of mixed data types: {mix_tup}")

print(f"Third item: {str_tup[2]}")
print(f"First and second items: {int_tup[0:2]}")
print(f"Another way of accessing the 1st and 2nd items: {int_tup[:2]}")
print(f"Last item: {mix_tup[-1]}")
print(f"Accessing in reverse: {int_tup[::-1]}")

#mix_tup[-1] = "complex data type"
#print("Modified mix tuple:", mix_tup)

updated_tup = str_tup + int_tup + mix_tup
print("Updated Tuple:", updated_tup)

updated_list = [item + 100 for item in int_tup]
updated_tuple = tuple(updated_list)
print("Original Tuple:", int_tup)
print("Updated Tuple:", updated_tuple)

new_list = [6, 7, 8, 9, 10]
int_list = list(int_tup)

for element in new_list:
    int_list.append(element)

int_tup2 = tuple(int_list)
print("Original Tuple:", int_tup)
print("Updated Tuple 2:", int_tup2)

x, y, z = str_tup
print (f"x: {x}, y: {y}, z: {z}")

x, *y = str_tup
print (f"x: {x}, y: {y}")
print(type(y))

#x, y = str_tup
#x, y, p, q = str_tup

print("For loop:")
for num in int_tup2:
    print(num, end = ' ')

index = 0

print("\n\nWhile Loop:")
while index < len(int_tup2):
    print(int_tup2[index])
    index += 1

indices = range(len(int_tup2))
for i in indices:
    print("tup[{}]: ".format(i), int_tup2[i])

def get_first_item(n):
    return n[0]

def sort_list(tuples):
    return sorted(tuples, key=get_first_item)

print(sort_list(('Uniform', 'Charlie'), ('Lima', 'Beta'), ('Zulu', 'Alpha'), ('Apple', 'Mango'), ('Banana', 'Olives'), ('Cherry', 'Echo')))

# Challenge
# Tuples are immutable but lists are mutable. Immutable means that the data structure's size is
# created and fixed at creation. While this makes the data structure less flexible when using it,
# it also means that we don't need to resize the data structure if more elements are added. Lists
# are mutable and therefore can grow, but this requires logic around copying the items and reallocating
# the memory. Dictionaries are completely different as they are stored as hash tables in memory. 
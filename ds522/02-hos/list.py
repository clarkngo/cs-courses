empty_list = []
print(empty_list)

str_list = ["alpha", "bravo", "charlie"]
int_list = [0, 1, 2, 3, 4, 5]

print(str_list[2])
print(int_list[0:2])
print(str_list[-1])
print(int_list[::1])

print(f"Original value at index i: {str_list[1]}")
str_list[1] = 'beta'
print(f"Updated value at index i: {str_list[1]}")

str_list.append('delta')
print(str_list)

str_list.append(['echo', 'foxtrot'])
print(str_list)

str_list.insert(1, "bravo")
print(str_list)

str_list.extend(('gold', 'hotel', 'india'))
print(str_list)

str_list.extend(int_list)
print(str_list)

str_list_1 = ["Juliett", "Kilo", "Lima"]
str_list_2 = list(('Mike', 'November'))
joined_str_list = str_list + str_list_1 + str_list_2
print(f"Joined list: {joined_str_list}")

joined_list = [item for sublist in [str_list_1, str_list_2] for item in sublist]
print(f"Another joined list: {joined_list}")

# Challenge
# The plus operator creates a new list while the extend operator changes the current one.
# Using the plus operator is therefore useful when we need to keep the original lists the
# same and not change them in any way. The extend operator is useful when we don't need the
# original list, and it's useful to not have to use a different variable name to refer to the list.

str_list.remove("beta")
print(f"After removing beta: {str_list}")

last_1 = str_list.pop()
print(f"After popping without arguments: {str_list}")
print(f"Popped item: {last_1}")

str_list.pop(-1)
print(f"After popping of the item in last index: {str_list}")

zero = str_list.pop(8)
print(f"After popping 0 : {str_list}")
print(f"Popped item: {zero}")

print(f"After clearing the int_list: {int_list}")

del str_list[4]
print(f"After deleting item in index 4: {str_list}")

#del int_list
#print(f"After deleting int_list: {int_list}")

print("For loop:")
for i in str_list:
    print(i)

print("List Compehension:")
[print(i) for i in str_list]

print("List after sorting:", int_list)

int_list_1 = [10, 1, 8, 20, 15, 6, 47]
print("Unsorted list:", int_list_1)

sorted_list = sorted(int_list_1)
print("Sorted list:", sorted_list)

sorted_list.reverse()
print("Reversed list:", sorted_list)
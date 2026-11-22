print("\nFor Loop with List\n")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

print("\nFor Loop with Tuple\n")
numbers = (6, 7, 8, 9, 10)
for num in numbers:
    print(num)

# Part 2 Addition: Range Object
print("\nWith Range Object\n")
for i in range(0, 10, 2):  # (start, end, step)
    print("Range: " + str(i))

# Part 3 Addition: Iterating by Sequence Index
print("\nBy Sequence Index\n")
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print(f'Fruit in range {index} is {fruits[index]}')
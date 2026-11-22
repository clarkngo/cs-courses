import random

# 1. Create a list of 50 random integers (between 1 and 100)
numbers = [random.randint(1, 100) for _ in range(50)]

# 2. Find all even numbers and save them in a new list
even_numbers = [num for num in numbers if num % 2 == 0]

# Print results to verify
print("Original List of 50 Integers:")
print(numbers)
print("\nFiltered Even Numbers:")
print(even_numbers)
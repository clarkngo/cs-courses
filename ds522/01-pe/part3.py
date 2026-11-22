# 1 & 2. Prompt user to input at least 10 values separated by commas or spaces
user_input = input("Enter at least 10 numbers (separated by spaces or commas): ")

# Clean the input by converting commas into spaces, then split by whitespace
cleaned_input = user_input.replace(',', ' ')
number_list = [int(x) for x in cleaned_input.split()]

# 3. Find all the odd numbers in the list
odd_numbers = [num for num in number_list if num % 2 != 0]

# Print the results
print("\nYour entered numbers:", number_list)
print("Odd numbers found:", odd_numbers)
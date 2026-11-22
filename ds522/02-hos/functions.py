def print_numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        numbers.append(i)
        i = i + 1
    return numbers

user_limit = int(input("Give a limit: "))
print(print_numbers(user_limit))

def print_text(str):
    print(str)
    return

print_text("First call to the user-defined function.")
print_text("Second call to the user defined function.")
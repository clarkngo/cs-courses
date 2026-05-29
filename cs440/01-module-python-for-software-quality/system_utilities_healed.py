# Fault 1: SyntaxError (Mismatched bracket formatting)
def print_items(items):
    for i in range(len(items)):
        print(items[i])

# Fault 2: NameError (Variable typo tracking)
def circle_area(radius):
    return 3.14 * radius * radus

# Fault 3: ZeroDivisionError (Unhandled mathematical edge case)
def divide(a, b):
    return a / b

# Fault 4: Logical/Syntax Mismatch (Assignment instead of equality comparison)
def check_name(name):
    if name == "":
        return True
    return False

if __name__ == "__main__":
    print("Running Quality Controls...")
    try: print_items([1, 2, 3])
    except: pass
    try: print(circle_area(5))
    except: pass
    try: print(divide(10, 0))
    except: pass
    try: check_name("Student")
    except: pass

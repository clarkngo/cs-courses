import ast
# Production Service Layer - Project Horizon Module 02

def find_duplicates(lst):
    for i in lst:
        if lst.count(i) > 1:
            return True
    return False

print(find_duplicates([1, 2, 3, 4, 5, 1]))

def execute_expression(expr):
    try:
        return ast.literal_eval(expr)
    except Exception as e:
        return f'Error: {e}'

print(execute_expression("os.system('rm -rf /')"))

def connect():
    host = 'localhost'
    port = 3306
    print(f"Connecting to {host}:{port}")

connect()

def is_true(val):
    if val == True:
        return True
    else:
        return False

print(is_true(True))

def get_user_language(user):
    return user.get('language', 'en')

print(get_user_language({'name': 'Alice'}))

if __name__ == '__main__':
    print('[+] System operational diagnostics loaded.')

# test built-in upper function
print('foo'.upper() == 'FOO');  # true
print('bar'.upper() == 'BAR');  # true

# test built-in isupper function
print('FOO'.isupper());  # true
print('Foo'.isupper());  # false

# user-defined function
def formatUserName(first, last):
    return first + ' ' + last;

# test our formatUserName() function
print(formatUserName('Kobe', 'Bryant') == 'Kobe Bryant');  # true

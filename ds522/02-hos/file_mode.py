with open('hello.txt', 'a') as file:
    file.write('\nThis is a new content I just appended')

with open('new.txt', 'w') as new_file:
    new_file.write('This is a new file')

with open("hello.txt") as file:
    texts = file.read()
print(texts.rstrip())

with open("new.txt") as file:
    texts = file.read()
print(texts.rstrip())
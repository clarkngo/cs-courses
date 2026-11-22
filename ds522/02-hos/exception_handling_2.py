try:
    with open("textfile", "r") as f:
        f.write("This is a test file for exception handling")
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file successfully")
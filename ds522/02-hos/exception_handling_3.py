try:
    with open("textfile", "w") as f:
        try:
            f.write("This is a test file for exception handling")
            raise IOError
        finally:
            print("Closing file")
except IOError:
    print("Error: can't find file or read data")
def student_info(name, major, gpa, level=1):
    """This prints the passed info into this function"""
    print(f"Name: {name}")
    print(f"Major: {major}")
    print(f"GPA: {gpa}")
    print(f"Year level: {level}")
    return

print("----- Positional Arguments ----- ")
student_info("Ezra Berthalomew Johnson", "Neuroscience; Arts", 3.95, 4)

print("----- Keyword Arguments ----- ")
student_info(name="John Jones", gpa=3.85, major="Physics", level=2)

print("----- Default Argument Value ----- ")
student_info(name="Kento Nanami", gpa=3.58, major="Finance")
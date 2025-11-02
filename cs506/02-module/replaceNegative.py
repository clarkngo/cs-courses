original = [8, 20, -10, 55, -777]
for i in range(len(original)):
    print(original[i])

for i in range(len(original)):
    if original[i] <0:
        print(abs(original[i]))
    else:
        print(original[i])
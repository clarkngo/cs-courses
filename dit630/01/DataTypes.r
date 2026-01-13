# Create a character variable A
A <- "123"

# Print the type of A
print(class(A))

# print the length of A
print(nchar(A))

# check if the type of A is numeric
print(is.numeric(A))

# Numeric
B <- 456

# Logical
C <- TRUE
print(class(C))

# Date
D <- as.Date("2021-12-20")
print(class(D))

# Convert A from character to numeric
numeric_A <- as.numeric(A)
print(class(numeric_A))

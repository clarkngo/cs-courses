# Create a list
A <- list("a", "b", 1, 2)
print(A)

# View the internal structure of the list
str(A)

# Check the underlying data type of the list
print(typeof(A))

# Get the number of elements in the list
print(length(A))

# Retrieve a single element using an integer (returns a sublist)
print(A[1])

# Retrieve multiple elements using an integer vector (returns a sublist)
print(A[c(1:2)])

# Retrieve elements using a logical vector
print(A[c(TRUE, FALSE, FALSE, FALSE)])

# Modify a value in the list
A[[2]] <- "n"
print(A)

# Delete an element from the list
A[[2]] <- NULL
print(A)
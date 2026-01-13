# Create two vectors
vector1 <- c(-1, 1, 2, 4, 6)
vector2 <- 4:8

# Print vectors
print(vector1)
print(vector2)

# Vector operation
print(vector2 + 1)
print(vector1 + vector2)

# Select vector's elements by position
# Print the 2nd element of vector2
vector2[2]

# Print all elements of vector2 expect for the 2nd element
print(vector2[-2])

# Select vector's element by value
print(vector1[vector1 > 0])

# Show all elements of vector1 in vector2
print(vector1[vector1 %in% vector2])
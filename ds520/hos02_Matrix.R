# Create a matrix (filled column-wise by default)
mat1 <- matrix(data = 1:6, nrow = 3, ncol = 2)
print(mat1)

# Create a matrix filled row-wise using byrow = TRUE
mat2 <- matrix(data = 1:6, nrow = 3, ncol = 2, byrow = TRUE)
print(mat2)

# Create a matrix by specifying only one dimension (R figures out the other)
mat3 <- matrix(data = 1:6, ncol = 3)
print(mat3)
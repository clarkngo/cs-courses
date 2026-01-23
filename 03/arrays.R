# The vector to construct the array
vector <- 1:24

# The column names
dim1 <- c("A1", "A2")

# The row names
dim2 <- c("B1", "B2", "B3")

# The 3rd dimension names
dim3 <- c("C1", "C2", "C3", "C4")

# The 2 x 3 x 4 array, data=vector, dim=c(2,3,4), dimnames=list(dim1, dim2, dim3)
myarray <- array(vector, c(2,3,4), list(dim1, dim2, dim3))
print(myarray)
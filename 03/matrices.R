# row names and column names
row_names <- c("A1", "A2", "A3", "A4", "A5")
column_names <- c("B1", "B2", "B3", "B4", "B5", "B6")

# create a 5 X 6 matrix
matrix1 = matrix(1:30, nrow=5, ncol=6, dimnames=list(row_names, column_names))
print(matrix1)

# Fill matrix by row
matrix2 = matrix(1:4, nrow=2, ncol=2, byrow=TRUE)
print(matrix2)

# Fill matrix by column
matrix3 = matrix(1:4, nrow=2, ncol=2, byrow=FALSE)
print(matrix3)
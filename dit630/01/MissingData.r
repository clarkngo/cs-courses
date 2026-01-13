A <- c(1, NA, 2)
B <- c(1, NULL, 2)
C <- c(NA, NA, NA)
D <- NULL

# Show vector A and B
print(A)
print(B)

# Check if A has NA value
print(any(is.na(A)))

# Check if B has a NULL value
print(any(is.null(B)))

# Check if ALL elements of C are NA
print(all(is.na(C)))

# Check if D is NULL
print(is.null(D))
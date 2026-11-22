# Create a vector
my_vector <- c(1, 2, 3, 4, 5)
print(my_vector)

# Check Data Type
print(typeof(my_vector))
print(class(my_vector))

# Check Length
print(length(my_vector))

# Create Range with Colon Operator
range_vec <- 1:10
print(range_vec)

# Indexing Elements
print(my_vector[2])                 # Second element
print(my_vector[c(2, 5)])           # Second and fifth elements
print(my_vector[-2])                # All except second
print(my_vector[c(TRUE, FALSE, TRUE, FALSE, TRUE)]) # Logical indexing
print(my_vector[my_vector > 3])     # Values > 3

# Modify Vector
my_vector[2] <- 20
print(my_vector)
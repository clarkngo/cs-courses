# Creating vectors
v1 <- c(26, 25, 43, 24, 37)
v2 <- c(43, 12, 32, 34, 11)

# Function to return the vector name with the greater mean
greater_mean <- function(v1, v2) {
  if (mean(v1) > mean(v2)) {
    print("v1")
  } else {
    print("v2")
  }
}

# Call the function
greater_mean(v1, v2)
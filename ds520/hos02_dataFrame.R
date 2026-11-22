# Load the tibble package for modern print layout
library(tibble)

# Create a data frame with patient information
Obesity_df <- data.frame(
  patientID = c(1, 2, 3, 4),
  height_in_cm = c(173, 162, 185, 182),
  weight_in_kg = c(80, 58, 100, 83),
  age = c(19, 24, 22, 28),
  obesity = c(TRUE, FALSE, TRUE, FALSE)
)

# Print the original data frame
print(Obesity_df)

# View the structure of the data frame
str(Obesity_df)

# Access a column using $ notation
print(Obesity_df$weight_in_kg)

# Apply a summary statistic (mean) to a column
print(mean(Obesity_df$weight_in_kg))

# Access a column by name using indexing
print(Obesity_df["height_in_cm"])

# Convert the data frame to a tibble for modern print layout
Obesity_tbl <- as_tibble(Obesity_df)
print(Obesity_tbl)
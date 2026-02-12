# 1. Read the data 
iris_data <- read.csv("iris2.csv") 

# 2. Data Cleaning: Remove missing values (NA) and Duplicates 
clean_iris <- na.omit(iris_data) 
final_iris <- unique(clean_iris) 

# 3. Data Filtering: Find only 'Setosa' with petal length > 1.5 
setosa_subset <- subset(final_iris, variety == "Setosa" & petal.length > 1.5) 

# 4. Save your clean work 
write.csv(setosa_subset, "clean_results.csv") 
# Step 0: Install and load ISLR
# 1. Install the ISLR package
install.packages('ISLR')

# 2. Load the library
library(ISLR)

# Step 1: Load and Explore the data
# 1. Create a data frame for the dataset
data(package = "ISLR")
carseats <- Carseats

# 2. Count and list the features (attributes) in the dataset
names(carseats)        # List feature names
length(carseats)       # Number of features (columns)

# 3. How many instances (rows) are there in the dataset?
nrow(carseats)

# 4. Produce the histogram for "Sales" and save it to a PDF
pdf("sales_histogram.pdf")
hist(carseats$Sales, main = "Histogram of Sales", xlab = "Sales", col = "skyblue")
dev.off()

# 5. Add an attribute "High" ("Yes" if Sales > 8, "No" otherwise)
carseats$High <- ifelse(carseats$Sales > 8, "Yes", "No")

# 6. Verify that carseats has the new "High" attribute
head(carseats)
str(carseats)

# 7. Answer: Count of "Yes" and "No" in the High attribute
table(carseats$High)

# 8. Convert values in "High" to factors
carseats$High <- as.factor(carseats$High)

# Step 2: Train the Model
# 1. Load the tree package
install.packages("tree") # Run if tree package is not already installed
require(tree)

# 3a. Create a decision tree classifier excluding the numeric 'Sales' variable
tree.carseats <- tree(High ~ . - Sales, data = carseats)

# 3b. Show the model summary
summary(tree.carseats)

# Step 3: Assess and Visualize the classifier performance
# 1. Obtain detailed metrics from summary
summary(tree.carseats)

# 2. Print tree details (listing)
tree.carseats

# Save tree structure output to a text file / PDF
sink("tree_details.txt")
print(tree.carseats)
sink()

# 3. Visualize the decision tree and save plot to a PDF file
pdf("tree_plot.pdf")
plot(tree.carseats)
text(tree.carseats, pretty = 0)
dev.off()
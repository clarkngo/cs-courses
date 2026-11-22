require("class")
?knn

install.packages('psych')
install.packages('tmvnsim')

require("datasets")
library(help = "datasets")

# 1. How many instances are there in the dataset?   
nrow(iris)
# or
dim(iris)

# 2. How many labels/classes (species) are there in the dataset? What are they?   
levels(iris$Species)
# or
unique(iris$Species)

# 3. How many features are there in the dataset? What are they?   
ncol(iris) - 1  # excluding Species column
colnames(iris)

# 4. Load the psych library:   
library(psych)
  
# 5. Plot a scatterplot of Petal Length against Petal width:   
plot(iris$Petal.Width, iris$Petal.Length, 
     main="Petal Length vs Petal Width", 
     xlab="Petal Width", ylab="Petal Length")

# 6. Plot a scatterplot of Sepal Length against Sepal width:   
plot(iris$Sepal.Width, iris$Sepal.Length, 
     main="Sepal Length vs Sepal Width", 
     xlab="Sepal Width", ylab="Sepal Length")

# 7. Plot the scatter plots and correlations between the iris features using pairs.panels:   
pairs.panels(iris[1:4], 
             main="Iris Feature Pairs and Correlations", 
             hist.col="cyan")

# Step 2: Preparing to train the model
# 1. Set the random number seed:   
set.seed(15)

# 2. Randomize the order of instances in the dataset:   
rnd_idx <- sample(rep(1:150))

# 3. Randomize the iris dataset:   
iris <- iris[rnd_idx, ]

# 4. Normalize the data to minimize the effect of outliers on the distance metric:   
normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}

# 5. Create a new data frame with normalized values:
iris.new <- as.data.frame(lapply(iris[, c(1, 2, 3, 4)], normalize))

summary(iris.new)

# 7. Plot the histogram for each of the four features to confirm your answer above:   
# a. Sepal Length Histogram:
hist(iris.new$Sepal.Length, col = 'red', breaks = 12)

# b. Sepal Width Histogram:
hist(iris.new$Sepal.Width, col = 'green', breaks = 12)

# c. Petal Length Histogram:

hist(iris.new$Petal.Length, col = 'blue', breaks = 12)
# d. Petal Width Histogram:

hist(iris.new$Petal.Width, col = 'purple', breaks = 12)

# Step 3: Training the modelDivide the iris.new dataset into train and test sets (80/20 split), 
# and set Species from the older iris (column #5) set as targets:  
# a. 
iris.train <- iris.new[1:120,]   
# b. 
iris.train.target <- iris[1:120, 5] 
# c. 
iris.test <- iris.new[121:150,]   
# d. 
iris.test.target <- iris[121:150, 5]   
# Finally, we can train a kNN model:   
# a. Let us first try k = 5:   i. 
model1 <- knn(train = iris.train, test = iris.test, cl = iris.train.target, k = 5)

# b. Let us see how we did with the confusion matrix:   
table(iris.test.target, model1)

# Step 1: Loading the credit dataset and storing it in a variable called loan
loan <- read.csv("/cloud/project/credit_data.csv")
colnames(loan) 

# Focus on 8 relevant features (where "Credibility" contains the target labels):   
# loan.subset <- loan[, c('Credibility', 'Age..years.', 'Sex...Marital.Status', 'Occupation', 'Account.Balance', 'Credit.Amount', 'Length.of.current.employment', 'Purpose')]
loan.subset <- loan[, c(1, 14, 10, 18, 2, 6, 8, 5)]

# Analyze the dataset structure:   
str(loan.subset)

# Step 2: Preparing to train the modelNormalize the data using the previously 
# defined normalization function and lapply() (excluding the target column at index 1):   
loan.subset.norm <- as.data.frame(lapply(loan.subset[, 2:8], normalize))

# Confirm values range between 0 and 1 by generating a summary:   
summary(loan.subset.norm)

# Set the random number seed for reproducibility:   
set.seed(15)
# Randomize the order of instances to select 80% for training:   
rnd_idx <- sample(1:nrow(loan.subset.norm), size = nrow(loan.subset.norm) * 0.8, replace = FALSE)

# Divide the dataset into train and test sets (80/20 split) and set column #1 as the target:   
train.loan <- loan.subset.norm[rnd_idx, ]
test.loan <- loan.subset.norm[-rnd_idx, ]

# Create dataframes for the target labels:   
train.loan.target <- loan[rnd_idx, 1]
test.loan.target <- loan[-rnd_idx, 1]

# Step 3: Training some modelsLoad the class library:   
require("class")

# Train a kNN model with $k = 1$ (knn.1):   
knn.1 <- knn(train = train.loan, test = test.loan, cl = train.loan.target, k = 1)

# Train models with k = 29 and k = 35 (named knn.29 and knn.45 as specified in the prompt instructions):   
knn.29 <- knn(train = train.loan, test = test.loan, cl = train.loan.target, k = 29)
knn.45 <- knn(train = train.loan, test = test.loan, cl = train.loan.target, k = 35)

# Step 4: Evaluating the modelsDetermine the accuracy of the model (example for k=1):   

acc.1 <- 100 * sum(test.loan.target == knn.1) / NROW(test.loan.target)
acc.29 <- 100 * sum(test.loan.target == knn.29) / NROW(test.loan.target)
acc.45 <- 100 * sum(test.loan.target == knn.45) / NROW(test.loan.target)

# Step 5: Optimizing the model
# 1 & 2. Run an algorithm that iterates over several values of $k$ from 1 to 45:
i <- 1
k.optm <- 1
for (i in 1:45) {
  knn.mod <- knn(train = train.loan, test = test.loan, cl = train.loan.target, k = i)
  k.optm[i] <- sum(test.loan.target == knn.mod) / NROW(test.loan.target)
  k <- i
  cat(k, '=', k.optm[i], '\n')
}

# 3. Plot the accuracy against "k" curve:   
plot(k.optm, type = "b", xlab = "k- Value", ylab = "Accuracy rate", 
     main = "kNN optimization - Accuracy", col = "green")

# 4. Plot the error rate against "k" curve:
plot(1 - k.optm, type = "b", xlab = "k- Value", ylab = "prediction error rate", 
     main = "kNN optimization - Error", col = "red")






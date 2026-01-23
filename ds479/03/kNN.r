# --- SECTION 1: ENVIRONMENT SETUP ---
# Install necessary packages if they are not already installed [cite: 228, 234, 235]
# install.packages("caret")
# install.packages("tidyverse")

# Load the core libraries [cite: 261, 263]
library(caret)
library(tidyverse)

# --- SECTION 2: IMPORT AND INSPECT DATA ---
# Load the dataset from your local working directory [cite: 268]
ads <- read_csv("Social_Network_Ads.csv")

# Review the data structure and first few rows [cite: 273, 275]
ads %>% glimpse()
ads %>% head(5)

# Convert the target variable 'Purchased' into a factor for classification [cite: 361, 371]
ads$Purchased <- ads$Purchased %>% as.factor()

# --- SECTION 3: DATA PARTITIONING ---
# Set a seed for reproducibility of random results [cite: 376]
set.seed(479)

# Create an 80/20 split for training and testing sets [cite: 377, 378]
in_train <- createDataPartition(ads$Purchased, p = 0.8, list = FALSE)
ads_train <- ads[in_train, ]
ads_test <- ads[-in_train, ]

# Isolate the feature matrices (Age and EstimatedSalary) [cite: 393, 394, 395]
training_set <- ads_train[c("Age", "EstimatedSalary")]
testing_set <- ads_test[c("Age", "EstimatedSalary")]

# --- SECTION 4: PREPROCESSING (SCALING) ---
# Create the preprocessing object using 'center' and 'scale' [cite: 417, 421, 429]
ad_preprocess <- preProcess(training_set, method = c("center", "scale", "nzv"))

# Apply the scaling to both training and testing feature matrices [cite: 430, 431]
training_set <- predict(ad_preprocess, training_set)
testing_set <- predict(ad_preprocess, testing_set)

# --- SECTION 5: MODEL TRAINING ---
# Train the KNN model using 10-fold cross-validation [cite: 444, 446]
set.seed(479)
knn <- train(y = ads_train$Purchased, 
             x = training_set, 
             method = 'knn', 
             trControl = trainControl(method = 'cv', number = 10))

# --- SECTION 6: PREDICTION AND EVALUATION ---
# Use the trained model to predict outcomes on the test set [cite: 459, 463]
ad_prediction <- predict(knn, newdata = testing_set)

# Generate a confusion matrix to evaluate model accuracy [cite: 460, 463, 469]
confusionMatrix(ad_prediction, ads_test$Purchased)
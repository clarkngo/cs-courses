
install.packages("pROC")
install.packages("smotefamily")

# Load required libraries
library(caret)
library(e1071)
library(ggplot2)
library(pROC)
library(smotefamily)

# Import and Inspect Data
social_data <- read.csv("/cloud/project/Social_Network_Ads.csv")

# Convert target to factor
social_data$Purchased <- factor(social_data$Purchased,
                                levels = c(0, 1),
                                labels = c("No", "Yes"))

str(social_data)
summary(social_data)

# Train-Test Split
set.seed(123)
trainIndex <- createDataPartition(social_data$Purchased, p = 0.7, list = FALSE)
trainData <- social_data[trainIndex, ]
testData <- social_data[-trainIndex, ]

# Feature Scaling
preProc <- preProcess(trainData[, c("Age", "EstimatedSalary")], method = c("center", "scale"))
trainData[, c("Age", "EstimatedSalary")] <- predict(preProc, trainData[, c("Age", "EstimatedSalary")])
testData[, c("Age", "EstimatedSalary")] <- predict(preProc, testData[, c("Age", "EstimatedSalary")])

# Model Training with Cross-Validation
fitControl <- trainControl(method = "cv", number = 10,
                           classProbs = TRUE, summaryFunction = twoClassSummary)
knnFit <- train(Purchased ~ Age + EstimatedSalary,
                data = trainData,
                method = "knn",
                trControl = fitControl,
                metric = "ROC")

print(knnFit)

# Predictions
pred <- predict(knnFit, newdata = testData)
pred_probs <- predict(knnFit, newdata = testData, type = "prob")

# Confusion Matrix Heatmap
cm <- confusionMatrix(pred, testData$Purchased)

print(cm)
# Confusion Matrix Heatmap
cm_table <- as.data.frame(cm$table)

ggplot(cm_table, aes(Prediction, Reference, fill = Freq)) +
  geom_tile() +
  geom_text(aes(label = Freq), vjust = 1) +
  scale_fill_gradient(low = "white", high = "red") +
  ggtitle("Confusion Matrix Heatmap")

# ROC Curve & AUC
roc_obj <- roc(testData$Purchased, pred_probs[, "Yes"])
plot(roc_obj, col = "blue", main = "ROC Curve")
auc(roc_obj)

# Classification Metrics
precision <- posPredValue(pred, as.factor(testData$Purchased))
recall <- sensitivity(pred, as.factor(testData$Purchased))
f1 <- (2 * precision * recall) / (precision + recall)

cat("Precision:", precision, "\n")
cat("Recall:", recall, "\n")
cat("F1 Score:", f1, "\n")
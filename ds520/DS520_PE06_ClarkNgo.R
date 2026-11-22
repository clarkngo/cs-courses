# Load the dataset
data <- read.csv("real_estate_clean.csv")

# View dataset contents in a nice table format
View(data)

# Explore basic dimensions and structure
dim(data)
head(data)
summary(data)

# Plots and Correlations for columns 2 to 5 (excluding index column 'No')
pairs(data[2:5])
cor_matrix <- cor(data[2:5])
print(cor_matrix)

# Train the multiple linear regression model
model <- lm(House.Price ~ House.age + MRT.Distance + Number.of.Stores, data = train_data)

# View model coefficients
print(model)
coef(model)

# Set random number seed for reproducibility
set.seed(15)

# Randomize and split data: 70% for training and 30% for testing
idx <- sample(2, nrow(data), replace = TRUE, prob = c(0.7, 0.3))

train_data <- data[idx == 1,]
test_data <- data[idx == 2,]

# Train the multiple linear regression model
model <- lm(House.Price ~ House.age + MRT.Distance + Number.of.Stores, data = train_data)

# View model coefficients
print(model)
coef(model)

# --- Visualizations ---
# 1. Plot for House age
plot(data$House.Price ~ data$House.age, main="Unit Price vs. House Age", col="red", xlab="House Age", ylab="House Price")
abline(lm(data$House.Price ~ data$House.age, data = train_data), col="blue")

# 2. Plot for Distance to MRT
plot(data$House.Price ~ data$MRT.Distance, main="Unit Price vs. Distance to MRT", col="blue", xlab="MRT Distance", ylab="House Price")
abline(lm(data$House.Price ~ data$MRT.Distance, data = train_data), col="green")

# 3. Plot for Number of stores
plot(data$House.Price ~ data$Number.of.Stores, main="Unit Price vs. Number of Stores", col="green", xlab="Number of Stores", ylab="House Price")
abline(lm(data$House.Price ~ data$Number.of.Stores, data = train_data), col="red")


# Predict unit prices on the test dataset
predictions <- predict(model, test_data)

# Plot unit price predictions against actual test prices
plot(predictions ~ test_data$House.Price, main="Unit Price Predictions Against Actual", xlab="Actual House Price", ylab="Predicted House Price", col="blue")
abline(0, 1, col="red", lty=2) # Adds an ideal y = x reference line

# View detailed regression analysis, ANOVA, R-squared, F-statistic, p-values, residuals, and degrees of freedom
summary(model)

# Confirm coefficients match the summary table estimate column
coef(model)
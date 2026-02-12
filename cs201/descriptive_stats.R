# Define a dataset of house prices (in thousands)
houses <- c(250, 275, 300, 280, 1200) 

# Calculate Mean and Median
mean(houses)
median(houses)

# Visualizing the Outlier Effect
hist(houses, main="House Prices Distribution", col="lightblue")
abline(v = mean(houses), col="red", lwd=3)    # Red line for Mean
abline(v = median(houses), col="blue", lwd=3) # Blue line for Median

# Calculate Variance and Standard Deviation
var(houses)
sd(houses)

# Visualizing Spread
boxplot(houses, horizontal=TRUE, main="Spread of House Prices", col="lightgreen")

# Calculate the Z-score for the luxury mansion (1200k) 
# Formula: (value - mean) / sd 
(1200 - mean(houses)) / sd(houses) 


# Using the summary() function for a quick look
summary(houses)
# Create a sequence of numbers (The X-axis) 
x <- seq(-4, 4, length=100) 

# Calculate the density for a Standard Normal Distribution (Mean=0, SD=1) 
y <- dnorm(x) 

# Plot the Bell Curve 
plot(x, y, type="l", lwd=2, col="blue", main="The Standard Normal Distribution")

# pnorm: What percentile is a score of 1300?
pnorm(1300, mean = 1060, sd = 210)

# qnorm: What score do you need to be in the 99th percentile?
qnorm(0.99, mean = 1060, sd = 210)

# Generate two sets of data with different spreads
narrow <- rnorm(1000, mean = 50, sd = 5)
wide   <- rnorm(1000, mean = 50, sd = 15)

# Plot side-by-side
par(mfrow=c(1,2))
hist(narrow, xlim=c(0, 100), main="Low SD (Narrow)", col="orange")
hist(wide, xlim=c(0, 100), main="High SD (Wide)", col="purple")
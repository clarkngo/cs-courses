par(mfrow=c(1,2))

# Simple histogram
hist(mtcars$mpg)

# With specified 12 bins and color
hist(mtcars$mpg, breaks=12, col="red",
     xlab="Miles Per Gallon", main="Colored Histogram with 12 bins")
par(mfrow = c(1,2))
# Box Plot
boxplot(mtcars$mpg, main = "Box plot", ylab = "Miles per Gallon")

# Using parallel box plots to compare groups
boxplot(mpg ~ cyl, data=mtcars,
        main="Car Mileage Data",
        xlab="Number of Cylinders",
        ylab="Miles Per Gallon")
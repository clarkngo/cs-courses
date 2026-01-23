# Setup side-by-side layout
par(mfrow = c(1,2))

# Basic Box Plot
boxplot(mtcars$mpg, main = "Box plot", ylab = "Miles per Gallon")

# Parallel Box Plots to compare groups (MPG by Cylinder)
boxplot(mpg ~ cyl, data=mtcars,
        main="Car Mileage Data",
        xlab="Number of Cylinders",
        ylab="Miles Per Gallon")
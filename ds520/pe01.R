# Load and view dataset structure directly
data(iris)
str(iris)
summary(iris)

# On macOS, open a native window:
quartz()

# Generate plots
par(mar = c(7, 5, 1, 1))
boxplot(iris, las = 2)

pairs(iris[, 1:4], col = iris[, 5], oma = c(4, 4, 6, 12))
par(xpd = TRUE)
legend(0.85, 0.6, as.vector(unique(iris$Species)), fill = c(1, 2, 3))
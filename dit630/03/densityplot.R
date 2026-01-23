library(ggplot2)

par(mfrow=c(2, 1), mai=c(0.5, 0.5, 0.5, 0))

density_carat <- density(diamonds$carat)

# Create the minimal graph with all the defaults in place
plot(density_carat)

# Add title
plot(density_carat, main="Carat of diamonds")

# Colors the curve blue and fills the area under the curve with solid red
polygon(density_carat, col="red", border="blue")
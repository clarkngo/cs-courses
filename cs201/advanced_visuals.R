library(ggplot2) 
library(ggplot2movies) 

# Histogram with a color gradient based on count
ggplot(movies, aes(x = rating)) + 
  geom_histogram(aes(fill = ..count..)) +
  scale_fill_gradient("Count", low = "blue", high = "red")

# Creating a Kernel Density Estimation plot
ggplot(movies, aes(x = rating)) + 
  geom_density(fill = "red", alpha = 0.3)


# Split the plot into panels based on cylinder type  
ggplot(mpg, aes(x = displ, y = hwy)) +   
  geom_point() +  
  facet_grid(. ~ cyl) 

# Trying different professional "skins"  
p <- ggplot(mpg, aes(x = displ, y = hwy, color = drv)) + geom_point()  

p + theme_bw()        # Clean black and white  
p + theme_minimal()   # Modern and simple  
p + theme_dark()      # High-contrast dark mode 
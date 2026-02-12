install.packages("ggplot2")
install.packages("ggplot2movies")
library(ggplot2) 
library(ggplot2movies) 

# Basic Histogram of Movie Ratings 
ggplot(movies, aes(x = rating)) +  
  geom_histogram() 

ggplot(movies, aes(x = rating)) +  
  geom_histogram(binwidth = 0.5, fill = "blue", color = "white", alpha = 0.5) + 
  labs(title = "Distribution of Movie Ratings", x = "Rating", y = "Count") + 
  theme_minimal() 

# Basic Scatterplot: Weight (wt) vs. Miles Per Gallon (mpg)
ggplot(data = mtcars, aes(x = wt, y = mpg)) + 
  geom_point()


# Scatterplot with Color and Size mapping 
ggplot(mtcars, aes(x = wt, y = mpg)) +  
  geom_point(aes(color = hp, size = cyl)) 

# Adjusting transparency and point shape 
ggplot(mtcars, aes(x = wt, y = mpg)) +  
  geom_point(aes(color = hp), size = 4, alpha = 0.5, shape = 18) 

# Basic Bar Chart: Counts of car classes  
ggplot(mpg, aes(x = class)) +   
  geom_bar() 

# Bar Chart colored by drivetrain (drv)  
ggplot(mpg, aes(x = class)) +   
  geom_bar(aes(fill = drv))  

# Side-by-Side (Dodge) Bar Chart  
ggplot(mpg, aes(x = class)) +   
  geom_bar(aes(fill = drv), position = "dodge") 


# Basic Boxplot: Drivetrain vs. Highway MPG  
ggplot(mpg, aes(x = drv, y = hwy)) +   
  geom_boxplot() 

# Boxplot with fill color  
ggplot(mpg, aes(x = drv, y = hwy, fill = drv)) +   
  geom_boxplot() 

# Horizontal Boxplot using coord_flip  
ggplot(mpg, aes(x = drv, y = hwy, fill = drv)) +   
  geom_boxplot() +  
  coord_flip() 
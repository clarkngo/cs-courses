library(ggplot2)

histplot <- ggplot(mtcars, aes(x = mpg)) + 
  geom_histogram(color = "black", fill = "red", bins = 12)

print(histplot)
library(ggplot2)
library(vcd)

# Number of cars in each class:
print(ggplot(data=Arthritis, aes(Improved)) + 
        geom_bar() + 
        labs(title="Simple Bar Plot", x="Improved", y="Frequency"))
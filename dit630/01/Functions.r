MyData <- c(0, 2, 5, 9)

#Get the mean value of MyData
print(mean(MyData))

# Obtain function document
print(?mean())

# Search key word "mea" in all functions
print(??"mea")

# Obtain function document from a package
print(vignette("dplyr"))


library(dplyr)
# Use pipes
print(MyData %>% median)
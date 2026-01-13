install.packages(c('ggplot2', 'dplyr', 'tidyr'))

library(ggplot2)
library(dplyr)

# Draw a ggplot diagram using ggplot2
print(ggplot(mpg, aes(displ, hwy, colour = class)) + geom_point())


# Pick cases from the starwars dataset where the species equals 'Droid'
# Using dplyr
print(starwars %>% filter(species == 'Droid'))


# Unload the ggplot2 library
detach('package:ggplot2')

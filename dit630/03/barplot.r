library(vcd)

# Create a figure that can contain two subplots
# The figure has 1 row and 2 columns, and the subplot will fill it
par(mfrow=c(1,2))

# The improved records in the Arthritis presents the patient outcome
# for individuals recieving a placebo or drug
counts <- table(Arthritis$Improved)

# Print the counts
print(counts)

# Simple Bar Plot
barplot(counts, main="Simple Bar Plot",
        xlab="Improved", ylab="Frequency")

# Horizontal Bar Plot
barplot(counts, main="Horizontal Bar Plot",
        xlab="Improved", ylab="Frequency", horiz=TRUE)

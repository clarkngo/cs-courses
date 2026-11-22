# Step 0: Install and Load R Libraries
# install.packages("arules")
# install.packages("arulesViz")
# install.packages("RColorBrewer")

# Load libraries
library(arules)
library(arulesViz)
library(RColorBrewer)

# Step 1: Load the Dataset and Explore the Data
# Load the dataset
data("Groceries")

# Explore basic dataset dimensions
Groceries

# View relative item frequency plot for the top 20 items
itemFrequencyPlot(Groceries, 
                  topN = 20, 
                  col = brewer.pal(8, 'Dark2'), 
                  main = 'Relative Item Frequency Plot', 
                  type = "relative", 
                  ylab = "Item Frequency (Relative)")

item_freq <- itemFrequency(Groceries)
names(item_freq[item_freq > 0.15])

# Step 2: Use the Apriori Library to Extract the Rules
# Extract rules
rules <- apriori(Groceries, parameter = list(supp = 0.01, conf = 0.2))

# View summary of rules
summary(rules)

# Inspect top 20 rules (Note: fix syntax typo from prompt by using square brackets)
inspect(rules[1:20])

# Step 3: Finding Redundancy and Pruning the Association Rules
# Find redundancy based on confidence
redundant <- is.redundant(rules, measure="confidence")
which(redundant)

# Prune redundant rules and sort by lift
rules.pruned <- rules[!redundant]
rules.pruned <- sort(rules.pruned, by="lift")

# Inspect the top 20 pruned rules
inspect(rules.pruned[1:20])

# Step 4: Visualizing the Association Rules
# Ensure arulesViz is loaded
library(arulesViz)

# 1. Standard scatter plot of rules
plot(rules)

# 2. Grouped matrix plot
plot(rules, method="grouped")

# 3. Interactive or static graph-based plot
plot(rules, method="graph")
# Step 0: Install and load R libraries

# 2a. Install pheatmap (run once if not already installed)
install.packages("pheatmap")

# 2b. Load pheatmap (note: library() is standard in R)
library(pheatmap)

# Step 1: Load the dataset and Explore the data

# 1. Load dataset
data <- read.csv("/cloud/project/mtcars.csv")

# 2. View contents and structure
View(data)
str(data)

# 3. Summary of dataset
summary(data)

# 3b. Create numeric-only subset (excluding column #1) and verify
cars <- data[, -1]
View(cars)
str(cars)
summary(cars)

# 4. Exploratory plots
plot(cars)

plot(mpg ~ hp, data = cars)

plot(mpg ~ hp, data = data)
with(data, text(mpg ~ hp, labels = data[, 1], pos = 4, cex = 0.6))


# Step 2: Use k-means algorithm to find clusters in the data

# 1a. Normalize the cars dataset
cars.n <- scale(cars)

# 1b. Confirm normalization
summary(cars.n)

# 2. Run k-means for k = 3, 10, and 20 with set.seed(5)
set.seed(5)
km3 <- kmeans(cars.n, 3)
km3
km3$size
km3$betweenss / km3$totss

set.seed(5)
km10 <- kmeans(cars.n, 10)
km10
km10$size
km10$betweenss / km10$totss

set.seed(5)
km20 <- kmeans(cars.n, 20)
km20
km20$size
km20$betweenss / km20$totss

# 2e & 2f. Plot color-coded clusters on mpg ~ hp
plot(mpg ~ hp, cars, col = km3$cluster, pch = 20, cex = 3, main = "k = 3 clusters")
plot(mpg ~ hp, cars, col = km10$cluster, pch = 20, cex = 3, main = "k = 10 clusters")
plot(mpg ~ hp, cars, col = km20$cluster, pch = 20, cex = 3, main = "k = 20 clusters")

# Step 3
# 1a-b. Produce k-means models for k = 1 to k = 20
set.seed(5)
km <- list()
for (i in 1:20) {
  km[[i]] <- kmeans(cars.n, i)
}

# 2a. Extract Between SS / Total SS for each of the 20 models
betweenss_totss <- list()
for (i in 1:20) {
  betweenss_totss[[i]] <- km[[i]]$betweenss / km[[i]]$totss
}

# 3a. Plot the elbow curve
plot(1:20, betweenss_totss, type = "b",
     ylab = "Between SS / Total SS", xlab = "Clusters(k)")

# 3d-e. Inspect the chosen optimal model (e.g., k = 4 or k = 5)
km[[4]]
km[[5]]


# Step 4
# Optional: assign car names as row names so heatmap & dendrogram show car models
rownames(cars) <- data[, 1]
cars.n <- scale(cars)

# 1a-b. Compute Euclidean distance matrix
distance <- dist(cars.n)
distance

# 2a. Plot scaled heatmap without row/column reordering
heatmap(as.matrix(cars), scale = "column", Rowv = NA, Colv = NA)

# 3a-c. Hierarchical clustering with Ward.D2 and plot dendrogram
hCluster <- hclust(distance, "ward.D2")
plot(hCluster, hang = -1)
rect.hclust(hCluster, k = 4, border = "red")

# Check exact cluster member counts for k = 4
table(cutree(hCluster, k = 4))
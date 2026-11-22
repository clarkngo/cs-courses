# Section 1: Package Setup & Initialization
install.packages(c("tidyverse", "plotly", "cluster", "RColorBrewer"))

# load libraries
walk(c("tidyverse",
       "cluster",
       "plotly",
       "stringr",
       "RColorBrewer",
       "ggplot2"), library, character.only = TRUE)

set.seed(42)

# Section 2: Data Loading and PreprocessingR# Load Data
load_data <- function(path) {
  read_csv(path, show_col_types = FALSE)
}

# Preprocess
preprocess_data <- function(df) {
  df <- df %>%
    mutate(
      earnings_quartiles_numeric = as.numeric(str_extract(earnings_quartiles, "\\d")),
      debt_quartiles_numeric = as.numeric(str_extract(debt_quartiles, "\\d"))
    )
  
  features <- df %>%
    filter(complete.cases(earnings_quartiles_numeric, debt_quartiles_numeric)) %>%
    select(institution_name, earnings_quartiles_numeric, debt_quartiles_numeric)
  
  X <- scale(features[, -1])
  list(df = df, features = features, X = X, keep = rownames(df) %in% rownames(features))
}

# Section 3: Metric Computation
compute_metrics <- function(X, max_k = 10, nstart = 25) {
  wss <- map_dbl(1:max_k, ~ kmeans(X, centers = .x, nstart = nstart)$tot.withinss)
  sil <- map_dbl(2:max_k, ~ mean(silhouette(kmeans(X, centers = .x, nstart = nstart)$cluster, dist(X))[, 3]))
  
  list(
    wss = tibble(k = 1:max_k, wss = wss),
    sil = tibble(k = 2:max_k, avg_silhouette = sil)
  )
}

# Section 4: Clustering
cluster_and_profile <- function(X, features, k, nstart = 50) {
  km <- kmeans(X, centers = k, nstart = nstart)
  clustered <- features %>% as_tibble() %>% mutate(cluster = factor(km$cluster))
  
  profile <- clustered %>%
    group_by(cluster) %>%
    summarise(
      n = n(),
      avg_earnings = mean(earnings_quartiles_numeric),
      avg_debt = mean(debt_quartiles_numeric),
      .groups = "drop"
    )
  
  support_cluster <- profile %>%
    mutate(score = rank(avg_earnings) + rank(-avg_debt)) %>%
    slice_min(score, n = 1) %>%
    pull(cluster) %>% as.character()
  
  list(km = km, clustered = clustered, profile = profile, support_cluster = support_cluster)
}

# Section 5: Visualization
show_plotly <- function(df, x, y, title) {
  plot_ly(df, x = ~.data[[x]], y = ~.data[[y]], type = "scatter", mode = "lines+markers",
          hovertemplate = paste0(x, "=%{x}<br>", y, "=%{y}<extra></extra>")) %>%
    layout(title = title, xaxis = list(title = x), yaxis = list(title = y))
}

show_ggplot <- function(df, x, y, title) {
  ggplot(df, aes(.data[[x]], .data[[y]])) +
    geom_line() + geom_point() +
    labs(title = title, x = x, y = y) +
    theme_minimal(base_size = 12)
}

plot_clusters_inline <- function(clustered, k) {
  pal <- brewer.pal(max(3, k), "Set1")[1:k]
  
  plot_ly(clustered,
          x = ~earnings_quartiles_numeric,
          y = ~debt_quartiles_numeric,
          color = ~cluster, colors = pal,
          type = "scatter", mode = "markers",
          marker = list(size = 6)) %>%
    layout(title = paste("K-means Clusters (k=", k, ")"),
           xaxis = list(title = "Earnings Quartile"),
           yaxis = list(title = "Debt Quartile")) %>% print()
  
  ggplot(clustered, aes(earnings_quartiles_numeric, debt_quartiles_numeric, color = cluster)) +
    geom_jitter(width = 0.1, height = 0.1, alpha = 0.8) +
    scale_color_brewer(palette = "Set1") +
    labs(title = paste("K-means Clusters (k=", k, ")"),
         x = "Earnings Quartile", y = "Debt Quartile") +
    theme_minimal(base_size = 12) %>% print()
}

# Section 6: Labeling & Evaluation (Execution)
attach_labels <- function(df, km, keep, k) {
  df$cluster <- NA
  df$cluster[keep] <- as.character(km$cluster)
  df$cluster <- factor(df$cluster, levels = as.character(1:k))
  df
}

# Execution
college_df <- load_data("/cloud/project/colleges.csv")
processed <- preprocess_data(college_df)
metrics <- compute_metrics(processed$X)

cat("Elbow Method: WSS vs k\n")
print(show_ggplot(metrics$wss, "k", "wss", "Elbow Method"))
print(show_plotly(metrics$wss, "k", "wss", "Elbow Method"))

cat("\nSilhouette Method: Avg Silhouette vs k\n")
print(show_ggplot(metrics$sil, "k", "avg_silhouette", "Silhouette Method"))
print(show_plotly(metrics$sil, "k", "avg_silhouette", "Silhouette Method"))

k <- 3
results <- cluster_and_profile(processed$X, processed$features, k)

cat("\nSupport cluster:", results$support_cluster, "\n")
print(results$profile)

plot_clusters_inline(results$clustered, k)

college_labeled <- attach_labels(processed$df, results$km, processed$keep, k)
needs_support <- college_labeled %>% filter(cluster == results$support_cluster)

cat("\nColleges Needing Support:\n")
print(needs_support %>% select(institution_name, earnings_quartiles, debt_quartiles, cluster))

set.seed(777)
km2 <- kmeans(processed$X, centers = k, nstart = 50)
cat("\nCluster agreement:", mean(results$km$cluster == km2$cluster), "\n")
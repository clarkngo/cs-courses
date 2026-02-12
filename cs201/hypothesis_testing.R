# 1. Load the sample data
salary_data <- read.csv("ztest-a.csv")
sample_mean <- mean(salary_data$salary)

# 2. Define population parameters
pop_mean <- 95000
pop_sd <- 15000  # Known population standard deviation
n <- nrow(salary_data)

# 3. Calculate the Z-Statistic
z_stat <- (sample_mean - pop_mean) / (pop_sd / sqrt(n))

# 4. Calculate the P-value (Two-tailed)
p_value <- 2 * pnorm(-abs(z_stat))
print(p_value)
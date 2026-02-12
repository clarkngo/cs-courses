# Define two independent groups 
fertilizer_A <- c(20, 22, 19, 24, 25) 
fertilizer_B <- c(28, 30, 27, 29, 31) 

# Run the Independent T-Test 
# var.equal = TRUE assumes both groups have similar spread 
t_result <- t.test(fertilizer_A, fertilizer_B, var.equal = TRUE) 
print(t_result) 

# Measurement before and after a training program 
before_training <- c(70, 75, 80, 72, 78) 
after_training  <- c(85, 88, 92, 84, 90) 

# Run the Paired T-Test 
paired_result <- t.test(before_training, after_training, paired = TRUE) 
print(paired_result) 
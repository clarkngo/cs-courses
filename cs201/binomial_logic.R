# What is the probability of getting EXACTLY 7 heads in 20 flips?
dbinom(x = 7, size = 20, prob = 0.5)

# What is the probability of getting 7 OR FEWER heads in 20 flips?
pbinom(q = 7, size = 20, prob = 0.5)

# Testing a biased die: 100 rolls, 25 sixes (We expect 1/6, or ~16) 
binom.test(x = 25, n = 100, p = 1/6, alternative = "greater") 
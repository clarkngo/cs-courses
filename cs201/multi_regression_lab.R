# 1. Data Setup 
exam_score <- c(75, 82, 78, 90, 85, 92, 88, 95) 
study_hrs  <- c(10, 15, 12, 20, 18, 25, 22, 28) 
prior_gpa  <- c(2.5, 3.1, 2.8, 3.8, 3.4, 4.0, 3.6, 3.9) 

# 2. Build the Model 
multi_model <- lm(exam_score ~ study_hrs + prior_gpa) 
summary(multi_model) 

# 3. Visualize the "Regression Plane" 
# Click 'Install' if prompted for the package 
library(scatterplot3d) 
s3d <- scatterplot3d(study_hrs, prior_gpa, exam_score,  
                     pch=16, highlight.3d=TRUE, type="h", 
                     main="3D Regression Plane") 
s3d$plane3d(multi_model, col="blue", lwd=2) 

cor(study_hrs, prior_gpa)
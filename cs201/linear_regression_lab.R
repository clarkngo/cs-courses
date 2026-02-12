# Data: Study Hours (X) and Exam Scores (Y)
study_hours <- c(2, 5, 8, 10, 12, 15, 18, 20)
exam_scores <- c(55, 60, 68, 72, 80, 85, 92, 98)

# 1. Visualize the Relationship
plot(study_hours, exam_scores, main="Study Hours vs. Exam Scores", 
     xlab="Hours Studied", ylab="Final Score", pch=19, col="blue")

# 2. Build the Linear Model
model <- lm(exam_scores ~ study_hours)

# 3. Add the Regression Line to the plot
abline(model, col="red", lwd=2)

# 4. View the Model Results
summary(model)


# Plot the residuals to check for patterns 
plot(model$residuals, main="Residual Plot",  
     ylab="Error (Actual - Predicted)", xlab="Index", pch=19, col="purple") 
abline(h = 0, col="darkgrey", lty=2) 


# Create a "new student" who plans to study for 14 hours 
new_data <- data.frame(study_hours = 14) 

# Use the model to predict their score 
predicted_score <- predict(model, newdata = new_data) 

print(paste("Predicted Exam Score for 14 hours of study:", round(predicted_score, 2))) 
# Function using default arguments
HelloStudent <- function(name = "student") {
  print(sprintf("Hello, %s!", name))
}

HelloStudent()
HelloStudent("Mary")
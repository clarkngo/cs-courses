import mysql.connector 
 
# Get user input for a login form 
username = input("Enter your username: ") 
password = input("Enter your password: ") 
 
# Create a SQL query to check the user's login credentials 
query = "SELECT * FROM dbe.users WHERE username = '" + username + "' AND password = '" + password + "';" 
print(query) 
 
# Connect to the database and execute the query 
db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dbe', port=6603) 
cursor = db.cursor() 
cursor.execute(query) 
 
# Fetch the results 
result = cursor.fetchone() 
 
# Check if the user exists and the password is correct 
if result is not None: 
    print("Login successful!") 
else: 
    print("Invalid username or password.") 
     
# Close the database connection 
db.close()
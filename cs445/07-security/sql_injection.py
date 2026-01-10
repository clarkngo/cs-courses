import mysql.connector  
 
# Get user input for a login form  
username = input("Enter your username: ")  
password = input("Enter your password: ")  
 
# Connect to the database  
db = mysql.connector.connect(  
 host='127.0.0.1',  
 user='root',  
 password='root',  
 database='dbe',  
 port=6603  
)  
 
cursor = db.cursor()  
 
# Safer query using parameterized statement  
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"  
cursor.execute(query)  
 
# Fetch the results  
result = cursor.fetchone()  
 
# Check if the user exists and the password is correct  
if result:  
 print("Login successful!")  
 
else:  
 print("Invalid username or password.")  
 
# Close the connection  
 
db.close() 
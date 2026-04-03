import mysql.connector
from sqlalchemy import create_engine, text

# Get user input for a login form
username = input("Enter your username: ")
password = input("Enter your password: ")

# Create a SQL query to check the user's login credentials
query = text("SELECT * FROM dbe.users WHERE username = :username and password = :password")

# Connect to the database and execute the query
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:6603/dbe')
with engine.connect() as conn:
    result = conn.execute(query, {"username": username, "password": password})

# Check if the user exists and the password is correct
if result.fetchone() is not None:
    print("Login successful!")
else:
    print("Invalid username or password.")
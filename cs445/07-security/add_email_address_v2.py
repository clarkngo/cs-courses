import mysql.connector 
import re 
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
 
def is_valid_email(email_address): 
    match = re.match(pattern, email_address) 
    return match 

# Get Email Address 
email = input("Enter your Email Adress: ") 
if(not is_valid_email(email)): 
    raise ValueError("Enter valid email address") 

# SQL query to Update Email address 
query = "update dbe.users set email = '" + email + "';" 
print(query) 

# Connect to the database and execute the query 
db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dbe', port=6603) 
cursor = db.cursor() 
cursor.execute(query) 

# Check the results 
if cursor.rowcount> 1: 
    print("Update successful.") 
else: 
    print("Update failed.") 

db.commit() 
cursor.close() 
db.close()
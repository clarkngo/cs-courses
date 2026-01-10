import mysql.connector 

# Get Email Address 
email = input("Enter your Email Adress: ") 

# SQL query to Update Email address 
query = "update dbe.users set email = '" + email + "';" 
print(query) 
 
# Connect to the database and execute the query 
db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dbe', port=6603) 
cursor = db.cursor() 
cursor.execute(query) 

# check the results 
if cursor.rowcount> 1: 
    print("Update successful.") 
else: 
    print("Update failed.") 

cursor.close() 
db.close()
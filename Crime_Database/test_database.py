import mysql.connector
from database import *

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sthblue0423306!',
    port='3306',
    database='crime_database'
)

cursor = mydb.cursor()

print("Test #2: database.py: dropTables() Function", "Expected Value 0", f"Actual Value {dropTables()}")
cursor.execute("SHOW TABLES;")
results = cursor.fetchall()

print("Test #2: database.py: dropTables() Function", "Expected Value No Tables in Database", f"Actual Value {results}")
mydb.cmd_reset_connection()
print("Test #3: database.py: createTables() Function", "Expected Value 0", f"Actual Value {createTables()}")

cursor.execute("SHOW TABLES;")
results = cursor.fetchall()

print("Test #3: database.py: createTables() Function", "Expected Value Tables: weapon, neighborhood, crime_types, crime", f"Actual Value {results}")

crime_data = retrieve_crime_data('sample_test_data.csv')

    # Inserts the data into each table.
    
print("Test #4: database.py: insertWeapons(crime_data) Function", "Expected Value 0", f"Actual Value {insertWeapon(crime_data)}")
mydb.cmd_reset_connection()
cursor.execute("SELECT * FROM weapon;")
results = cursor.fetchall()

print("Test #4: database.py: insertWeapons() Function", "Expected Value 11", f"Actual Value {len(results)}")

print("Test #5: database.py: insertNeighborhood(crime_data) Function", "Expected Value 0", f"Actual Value {insertNeighborhood(crime_data)}")
mydb.cmd_reset_connection()
cursor.execute("SELECT * FROM neighborhood;")
results = cursor.fetchall()

print("Test #5: database.py: insertNeighborhood(crime_data) Function", "Expected Value 170", f"Actual Value {len(results)}")

print("Test #6: database.py: insertCrime_type(crime_data) Function", "Expected Value 0", f"Actual Value {insertCrime_type(crime_data)}")
mydb.cmd_reset_connection()
cursor.execute("SELECT * FROM crime_type;")
results = cursor.fetchall()

print("Test #6: database.py: insertCrime_type(crime_data) Function", "Expected Value 33", f"Actual Value {len(results)}")

print("Test #7: database.py: insertCrime(crime_data) Function", "Expected Value 0", f"Actual Value {insertCrime(crime_data)}")
mydb.cmd_reset_connection()
cursor.execute("SELECT * FROM crime;")
results = cursor.fetchall()

print("Test #7: database.py: insertCrime(crime_data) Function", "Expected Value 462", f"Actual Value {len(results)}")


# database.py
# Execute the command "python database.py" to print out the output for the database's Black-Box Testing 
# Actual Output Results. Then, execute the command "python -m flask run" to generate the "Crime in Baltimore" Flask
# Web App Heat Map and Data Filter buttons.  
import mysql.connector
import pandas as pd
import numpy as np

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='crime_database'
)

cursor = mydb.cursor()

'''
The Function "def dropTables()" drops all the tables in the Database if they exist.
'''
def dropTables():
    cursor.execute('DROP TABLE IF EXISTS crime')
    cursor.execute('DROP TABLE IF EXISTS crime_type')
    cursor.execute('DROP TABLE IF EXISTS neighborhood')
    cursor.execute('DROP TABLE IF EXISTS weapon')
    return 0

'''
The Function "def createTables()" creates the tables in the Database.
'''
def createTables():

    cursor.execute("""CREATE TABLE weapon
            (
                weapon_id BIGINT PRIMARY KEY,
                weapon_name VARCHAR(32)
            )""")

    cursor.execute("""CREATE TABLE neighborhood
            (
                neighborhood_name VARCHAR(64) PRIMARY KEY,
                district_number INT,
                average_income FLOAT,
                food_source_quantity INT
            )""")

    cursor.execute("""CREATE TABLE crime_type
            (
                type_name VARCHAR(8) PRIMARY KEY,
                type_Description VARCHAR(128)
            )""")

    cursor.execute("""CREATE TABLE crime
           (
               crime_id BIGINT PRIMARY KEY,
               neighborhood_name VARCHAR(64),
               weapon_id BIGINT,
               type_name VARCHAR(8),
               crime_date VARCHAR(16),
               crime_time VARCHAR(16),
               latitude FLOAT,
               longitude FLOAT,
               FOREIGN KEY(weapon_id) REFERENCES weapon(weapon_id),
               FOREIGN KEY(type_name) REFERENCES crime_type(type_name),
               FOREIGN KEY(neighborhood_name) REFERENCES neighborhood(neighborhood_name)
           )""")

    return 0

'''
The Function "def insertWeapon(crime_data)" inserts data into the Weapon Table.
'''
def insertWeapon(crime_data):
    # Take the Weapon Data from the Comma-Separated Values CSV File provided.
    weapon = (crime_data["Weapon"].unique())

    # The Weapon Array contains the names of all the weapons.
    weapon_array = np.array(weapon)

    for i in range(len(weapon_array)):
        # Added a progress meter that is the number of inserted weapons compared to the total number of weapons to 
        # help with knowing how long it will take.
        print(f"Inserting Weapon: {i+1}/{len(weapon_array)}         ", end="\r")

        # Insert the Weapon ID represented as "weapon_id" in the "weapon" Table. In addition, insert the Weapon Name
        # represented as "weapon_name" in the "weapon" table.
        cursor.execute('INSERT INTO weapon (weapon_id,weapon_name) VALUES(%s, %s)', (i, weapon[i]))
        mydb.commit()

     # The Print Statement adds a line break for readability.
    print()
    return 0

'''
The Function "def insertNeighborhood(crime_data)" inserts data into the Neighborhood Table.
'''
def insertNeighborhood(crime_data):
    # Take the Neighborhood Data from the Comma-Separated Value CSV File provided.
    neighborhood = (crime_data["Neighborhood"].unique())
    #print(neighborhood)

    neighborhood_array = np.array(neighborhood)

    # Read the Median Household Income Excel Microsoft Office Open Extensible Markup Language XML Format Spreadsheet
    # File "Medium Household Income - Baltimore.xlsx" for Average Income Value.
    average_income = pd.read_excel("Median Household Income - Baltimore.xlsx")

    # Import the Comma-Separated Values CSV File "neighborhood_food.csv" into Python.
    food_sources = pd.read_csv("neighborhood_food.csv")

    # need to replace 0,0 with the correct data sheets ******
    for i in range(len(neighborhood_array)):
        # Added a progress meter that is the number of inserted neighborhoods compared to the total number of 
        # neighborhoods to help with knowing how long it will take.
        print(f"Inserting Neighborhood: {i+1}/{len(neighborhood_array)}         ", end="\r")

        # Set the default Average Income Value represented by the "income" variable.
        income = 0

        # Set the default District Number represented by the "district_num" variable.
        district_num = 0

        # Set the default Food Count represented by the "food_count" variable.
        food_count = 0

        # Iterate over the Median Household Income Excel Microsoft Office Open Extensible Markup Language XML
        # Format Spreadsheet File "Medium Household Income - Baltimore.xlsx" that is represented by the
        # Variable "average_income".
        for j in range(len(average_income)):
            try:
                # Check if the "Community Statistical Area (2020)" and the Neighborhood name are the same.
                if average_income.iloc[j]["Community Statistical Area (2020)"].lower() in neighborhood[i].lower():

                    # If the "Community Statistical Area (2020)" and the Neighborhood name are the same, then
                    # store the Average Income from 2016 to 2020 in the "income" Variable as a float.
                    income = float(average_income.iloc[j]["2016-2020"] or 0)
            except:
                pass

        # Process the Comma-Separated Values CSV File and add the District Number and Food Count to the Database.
        for j in range(len(food_sources)):
            try:
                # Check if the food source, "neighborhood_name", and the actual neighborhood name are the same.
                if food_sources.iloc[j]["neighborhood_name"].lower() in neighborhood[i].lower():

                    # If the food source, "neighborhood_name", and the actual neighborhood are the same, then
                    # store the District Number in the "district_num" Variable as an integer.
                    district_num = int(food_sources.iloc[j]["district_number"] or 0)

                    # Store the food source quantity in the "food count" Variable as an integer.
                    food_count = int(food_sources.iloc[j]["number_of_food_source_quantity_places"] or 0)
            except:
                pass
        


        # Insert all the data that was fetched from the Excel Microsoft Office Open Extensible Markup Language XML
        # Format Spreadsheet, .xlsx, and Comma-Separated Values CSV Files into a Database.
        cursor.execute('INSERT INTO neighborhood (neighborhood_name, district_number, average_income, food_source_quantity) VALUES(%s, %s, %s, %s)', (neighborhood[i], district_num, income, food_count))
        mydb.commit()

    # The Print Statement adds a line break for readability.
    print()

    # Updates all average_income of zeros to a default value of average_income of its district.
    for p in range(1, 15):
        cursor.execute("SELECT AVG(average_income) FROM crime_database.neighborhood WHERE average_income != 0 and district_number = %s", [p])
        result = cursor.fetchone()[0]

        cursor.execute('UPDATE neighborhood SET average_income = %s WHERE average_income = 0 and district_number = %s', [result, p])
        mydb.commit()
    return 0


'''
The Function "def insertCrime_type(crime_data)" inserts data into the Crime Type Table.
'''
def insertCrime_type(crime_data):
    # Take the Crime Code and Description of the Crime in the "crime_type" variable.
    crime_type = crime_data[['CrimeCode', 'Description']].drop_duplicates(subset=['CrimeCode'])
    crime_type_array = np.array(crime_type)

    # The crime_type_array contains tuples. The First Index of the tuple contains the Crime Type Name. The Second Index
    # of the tuple contains the Crime Type Description.
    for i in range(len(crime_type_array)):
        # Added a progress meter that is the number of inserted crime types compared to the total number of crime
        # types to help with knowing how long it will take.
        print(f"Inserting Crime Type: {i+1}/{len(crime_type_array)}         ", end="\r")
        # Insert the data into the "crime_type" Table.
        cursor.execute('INSERT INTO crime_type (type_name, type_Description) VALUES(%s, %s)', (crime_type_array[i][0], crime_type_array[i][1]))
        mydb.commit()
    # The Print Statement adds a line break for readability.
    print()
    return 0

'''
The Function "def insertCrime(crime_data)" inserts data into the Crime Table.
'''
def insertCrime(crime_data):


    crime_array = np.array(crime_data)

    # Get the data from weapon to find the correct weapon_id.
    query = "SELECT * FROM weapon"
    cursor.execute(query)
    result = cursor.fetchall()

    # Put "weapons" in a dictionary in order to speed up the identification.
    weapons = {}
    for weapon in result:
        weapons[weapon[1]] = weapon[0]

    inserted_count = 0
    for i in range(len(crime_array)):
        # Added a progress meter that is the number of inserted crimes compared to the total number of crimes to 
        # help with knowing how long it will take.
        print(f"Inserting Crime: {i+1}/{len(crime_array)}         ", end="\r")
        
        if crime_array[i][5] not in weapons:
            continue

        # Add Spacing between the Data and Time using Python's "split()" Function.
        datetime = crime_array[i][1].split(" ")

        # If there is no latitude or longitude for an entry, then that entire entry will be ignored.
        if crime_array[i][7] != 0 and crime_array[i][8] != 0:    
            # Fetch the time from the First Index that is Index 1 and then store it in the "time" Variable.
            cursor.execute('INSERT INTO crime (crime_id, neighborhood_name, weapon_id, type_name, crime_date, crime_time, latitude, longitude) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)',
                        (i, crime_array[i][6], weapons[crime_array[i][5]], crime_array[i][2], datetime[0], datetime[1], crime_array[i][7],crime_array[i][8]))
            inserted_count += 1
    mydb.commit()
    # The Print Statement adds a line break for readability.
    print()
    print(f"\tCrimes Inserted: {inserted_count}")
    print(f"\tCrimes with Missing Data: {len(crime_array) - inserted_count}")

    return 0
'''
The Function "def retrieve_crime_data()" loads the Comma-Separated Values CSV File and processes it for insertion 
into the database.
'''
def retrieve_crime_data(file_name):
    # Convert the Comma-Separted Values .csv File into useable "pandas" data.
    crime_data = pd.read_csv(file_name)

    # Sets any non existing values to a default one.
    crime_data['CrimeCode'] = crime_data['CrimeCode'].fillna("N/A")
    crime_data['Location'] = crime_data['Location'].fillna("N/A")
    crime_data['Description'] = crime_data['Description'].fillna("N/A")
    crime_data['Weapon'] = crime_data['Weapon'].fillna("N/A")
    crime_data['Neighborhood'] = crime_data['Neighborhood'].fillna("N/A")
    crime_data['Latitude'] = crime_data['Latitude'].fillna("-100000")
    crime_data['Longitude'] = crime_data['Longitude'].fillna("-100000")

    return crime_data
'''
The Function "def populate_database() populates the database that takes about 20 minutes with the 560,038 crimes
currently in the Comma-Separated Value CSV File "Part_1_Crime_Data.csv". 
'''
def populate_database():
    dropTables()
    createTables()
    crime_data = retrieve_crime_data('Part_1_Crime_Data.csv')

    # Inserts the data into each table.
    insertWeapon(crime_data)
    insertNeighborhood(crime_data)
    insertCrime_type(crime_data)
    insertCrime(crime_data)

if __name__ == '__main__':
    populate_database()
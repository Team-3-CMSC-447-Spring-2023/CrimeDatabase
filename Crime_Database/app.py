from flask import Flask, render_template
import mysql.connector
import pandas as pd
import numpy as np
from database import dropTables, createTables, insertWeapon, insertNeighborhood, insertCrime, insertCrime_type

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=' ',
    port='3306',
    database='crime_database'
)

cursor = mydb.cursor()

#Create and populate database before app startup
#code from database.py
dropTables()
createTables()

# Converts .csv into usable pandas data.
crime_data = pd.read_csv('Part_1_Crime_Data.csv')

# Sets any non existing values to a default one.
crime_data['CrimeCode'] = crime_data['CrimeCode'].fillna("N/A")
crime_data['Location'] = crime_data['Location'].fillna("N/A")
crime_data['Description'] = crime_data['Description'].fillna("N/A")
crime_data['Weapon'] = crime_data['Weapon'].fillna("N/A")
crime_data['Neighborhood'] = crime_data['Neighborhood'].fillna("N/A")
crime_data['Latitude'] = crime_data['Latitude'].fillna("-100000")
crime_data['Longitude'] = crime_data['Longitude'].fillna("-100000")


# Inserts the data into each table.
insertWeapon(crime_data)
insertNeighborhood(crime_data)
insertCrime_type(crime_data)
insertCrime(crime_data)


@app.route('/')
def hello_world(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime_data WHERE Latiude!=0 AND Longitude!=0')
    markers = cursor.fetchall()

    return render_template("heatmap_default.html", heatmapData=markers)


if __name__ == '__main__':
    app.run()

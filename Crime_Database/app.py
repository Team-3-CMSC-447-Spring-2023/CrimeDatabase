from flask import Flask, render_template
import mysql.connector

# Comment Out Line 6 if you do not want to see the repopulated tables as long as the "populate_database()" Function 
# in Line 24 is uncommented.
#from database import populate_database

# Added Static Folder Information and and Static URL Path so that 'css/group_proj.css' is accessible from the 
# Hypertext Markup Language HTML Page. 
app = Flask(__name__, static_url_path='', static_folder='')

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='crime_database'
)

cursor = mydb.cursor()

# Populate the Database before App Startup because it is extremely time-consuming.
# Maybe can add a check to repopulate if the tables are not there by uncommenting the "populate_database()"
# Function in line 23 of the app.py Python File. 
'''
populate_database()
'''
@app.route('/')
def hello_world(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Latitude!=0 AND Longitude!=0')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("heatmap_default.html", heatmapData=[list(x) for x in markers])


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
import mysql.connector
import json
from database import populate_database
from geopy.geocoders import MapQuest

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

# Populate the Database before App Startup because it is extremely time-consuming. Check to ensure the
# Function "populate_database()" Function is required before running.
#'''
'''
The Function "def check_database()" runs the "populate_database()" Function if the database is not ready
to be used by the Backend. In addition, when it comes to the Function "def check_database()", we do not want to
run the "populate_database()" Function every time we start the Backend Application because it is a very long
process that takes approximately 8+ minutes to finish running. 
'''
def check_database():
    # If you want to see the process for the "populate_database()" Function, then first in MySQL Workbench,
    # in "Navigator" on the left side of your SQL Editor in "MySQL Workbench" Window, under the "Filter Objects"
    # Search Bar after "SCHEMAS", double left-click on the right triangle icon before the cylinder icon that
    # shows the name of your database that is the assigned value for your database name "database=" within the
    # single quotes '' on line 10 of "database.py" Python code. Second, under the "Tables" Section,
    # Right-Click "crime" and then Left-Click "Drop Table ..." which will open the pop-up MySQL Workbench
    # Message Box Window that gives you the message "Drop Table Please confirm the permanent deletion of 
    # table 'crime' and its data" along with the options to "Review SQL" or "Drop Now". Select the
    # option "Drop Now" in the pop-up MySQL Workbench Message Box Window to drop the crime table. As a result,
    # this will help you see the process for the "populate_database()" Function because the Table Names are how it 
    # detects a prepared database. 

    # Fetch the Names of the Tables in the Database.
    cursor.execute("SHOW TABLES;")
    results = cursor.fetchall()

    # Isolate the Table Names.
    table_names = [x[0] for x in results]
    desired_table_names = {
        'crime',
        'crime_type',
        'neighborhood',
        'weapon'
    }

    # Check if the Names are in the Database Tables.
    if not all(name in table_names for name in desired_table_names):
        # If the Database is not ready, then run the "populate_database()" Function.
        populate_database()

        # Reset the connection in order to view the updated data.
        mydb.cmd_reset_connection()

@app.route('/')
def start_page(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Latitude!=0 AND Longitude!=0')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("heatmap_default.html", heatmapData=[list(x) for x in markers])

check_database()

@app.route('/crime_date')
def crime_date_all(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Latitude!=0 AND Longitude!=0')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_date.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_date_month')
def crime_date_month(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime_database.crime WHERE crime_date BETWEEN \'2023/03/08\' AND \'2023/04/08\' AND Latitude!=0 AND Longitude!=0;')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_date_month.html", heatmapData=[list(x) for x in markers])


@app.route('/crime_date_year')
def crime_date_year(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime_database.crime WHERE crime_date BETWEEN \'2022/04/08\' AND \'2023/04/08\' AND Latitude!=0 AND Longitude!=0;')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_date_year.html", heatmapData=[list(x) for x in markers])


@app.route('/crime_date_five_year')
def crime_date_five_year(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime_database.crime WHERE crime_date BETWEEN \'2018/04/08\' AND \'2023/04/08\' AND Latitude!=0 AND Longitude!=0;')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_date_five_year.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_type')
def crime_type(): #Display pie chart template and push data to chart
    #query and fetch type of crime from database
    cursor.execute('SELECT type_Description, COUNT(*) AS crime_count FROM crime_database.crime_type GROUP BY type_Description;')
    markers = cursor.fetchall()
    pieData=[list(x) for x in markers]
    pieData.insert(0, ['Weapon', 'Count of Occurence'])
    pieChartData_json = json.dumps(pieData)
    return render_template("crime_type.html", pieChartData_json=pieChartData_json)
    # return render_template("crime_type.html", pieChartData=pieData)

@app.route('/food_desert')
def food_desert(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
     # cursor.execute('SELECT Latitude, Longitude, food_source_quantity FROM crime_database.neighborhood WHERE Latitude!=0 AND Longitude!=0')
    cursor.execute('SELECT neighborhood_name, food_source_quantity FROM crime_database.neighborhood WHERE food_source_quantity !=0')
    markers = cursor.fetchall()
    # Set up the MapQuest geocoder with your API key
    geolocator = MapQuest(api_key="X7Z6sQ41SOtQYuO7GmD8jVPp8oE1iUUP")
    
    # Create a new list to store the modified data
    modified_markers = []

    for x in markers:
        neighborhood = x[0]  # Get the neighborhood name from the tuple

        # Perform geocoding to get the latitude and longitude
        location = geolocator.geocode(neighborhood)

        if location:
            latitude = location.latitude
            longitude = location.longitude
            if latitude < 39.4 and latitude > 39.2:
                x = [latitude, longitude, x[1]]  # Modify the tuple to include latitude, longitude, and food number
                modified_markers.append(list(x))  # Convert the modified tuple to a list and add it to the new list

    # Return the modified_markers list to the HTML template
    return render_template("food_desert.html", heatmapData=modified_markers)
   
@app.route('/weapon')
def weapon(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    query = """SELECT weapon.weapon_name AS weapon_name, COUNT(crime.weapon_id) AS weapon_count 
                FROM weapon
                JOIN crime ON weapon.weapon_id = crime.weapon_id GROUP BY weapon_name"""
    cursor.execute(query)
    #cursor.execute('SELECT weapon_name, occurances FROM crime_database.weapon')
    markers = cursor.fetchall()
    pieData=[list(x) for x in markers]
    pieData.insert(0, ['Weapon', 'Count of Occurences'])
    pieChartData_json = json.dumps(pieData)
    return render_template("weapon.html", pieChartData_json=pieChartData_json)

@app.route('/crime_time_noon')
def crime_time_noon(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute("SELECT Latitude, Longitude FROM crime_database.crime WHERE crime_time BETWEEN '08:00:00+00' AND '16:00:00+00'")
    markers = cursor.fetchall()
    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_time_noon.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_time_afternoon')
def crime_time_afternoon(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute("SELECT Latitude, Longitude FROM crime_database.crime WHERE crime_time BETWEEN '16:00:00+00' AND '24:00:00+00'")
    markers = cursor.fetchall()
    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_time_afternoon.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_time_morning')
def crime_time_morning(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute("SELECT Latitude, Longitude FROM crime_database.crime WHERE crime_time BETWEEN '00:00:00+00' AND '08:00:00+00'")
    markers = cursor.fetchall()
    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_time_morning.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_area')
def crime_area(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Longitude<=-76.57 AND Longitude>= -76.7 AND Latitude>=39.282 AND Latitude<=39.321')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_area.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_area_northeast')
def crime_area_northeast(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Longitude<=-76.570 AND Longitude>= -76.615 AND Latitude>=39.321')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_area_northeast.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_area_northwest')
def crime_area_northwest(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Longitude>=-76.700 AND Longitude<= -76.615 AND Latitude>=39.321')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_area_northwest.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_area_southeast')
def crime_area_southeast(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Longitude>=-76.615 AND Longitude<= -76.570 AND Latitude<=39.296')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_area_southeast.html", heatmapData=[list(x) for x in markers])

@app.route('/crime_area_southwest')
def crime_area_southwest(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Longitude>=-76.700 AND Longitude<= -76.615 AND Latitude<=39.296')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("crime_area_southwest.html", heatmapData=[list(x) for x in markers])





if __name__ == '__main__':
    app.run()

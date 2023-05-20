from flask import Flask, render_template
import mysql.connector
import json

# Comment Out Line 6 if you do not want to see the repopulated tables as long as the "populate_database()" Function 
# in Line 24 is uncommented.
# from database import populate_database

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

# populate_database()

@app.route('/')
def start_page(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Latitude!=0 AND Longitude!=0')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("heatmap_default.html", heatmapData=[list(x) for x in markers])

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
    cursor.execute('SELECT Latitude, Longitude, food_source_quantity FROM crime_database.neighborhood WHERE Latitude!=0 AND Longitude!=0')
    markers = cursor.fetchall()

    # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
    # information. 
    return render_template("food_desert.html", heatmapData=[list(x) for x in markers])

@app.route('/weapon')
def weapon(): #Display heatmap template and push data to heatmap
    #query and fetch latitudes and longitudes from database
    cursor.execute('SELECT weapon_name, occurances FROM crime_database.weapon')
    markers = cursor.fetchall()
    pieData=[list(x) for x in markers]
    pieData.insert(0, ['Weapon', 'Count of Occurences'])
    pieChartData_json = json.dumps(pieData)
    return render_template("weapon.html", pieChartData_json=pieChartData_json)

# @app.route('/neighborhood')
# def neighborhood(): #Display heatmap template and push data to heatmap
#     #query and fetch latitudes and longitudes from database
#     cursor.execute('SELECT Latitude, Longitude FROM crime WHERE Latitude!=0 AND Longitude!=0')
#     markers = cursor.fetchall()

#     # Convert the tuples in the markers variable to lists so that JavaScript can properly interpret the
#     # information. 
#     return render_template("neighborhood.html", heatmapData=[list(x) for x in markers])

if __name__ == '__main__':
    app.run()
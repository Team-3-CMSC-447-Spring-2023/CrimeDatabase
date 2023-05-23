# Deliverable 2 Administrator Manual
## **1. Introduction**

Our project was to create a heat map visualization of crime data in the city of Baltimore and provide correlation to the availability of food sources. To complete this task we used the Python server library `Flask` as well      as a `MySQL` database to hold the data on the backend and the JavaScript library `Leaflet.js` to provide the heatmap functionality on the frontend.

## **2. System Overview**
### 2.1 Background
From an administrator standpoint the system is fairly simple. It is currently set up as a python Flask app using the app.py file, which when run hosts the site locally. Instalation instructions for the statbase can be found in section 3.1. To start the app, simply run the app.py file, which should output a link that will open the site on your browser.
In terms of day to day operations there isn't much, the site can mostly be left on its own. For regular matinence, the database needs to be updated and backed up periodically. New data can be retrieved from [Open Baltimore](https://data.baltimorecity.gov/). Instructions for updating the data and backing up the database can be found in sections 3.2 and 3.3 respectivly. When the data is updated, you should also go into the app.py file and update any hardcoded dates for the filters, to ensure date ranges(past year, past 5 years, etc.) are accurate whenthe data is filtered. If the database crashes, instructions for recovery can be found in section 3.3, so long as you have periodically backed up the database. If you haven't, you will have to rebuild it using the database.py file.

### 2.2 Hardware an Software Requirements
**Required Hardware**
- **CPU:** 64 bit x86
- **RAM:** 8GB
- **Disk Space:** 100MB

**Required Software**
- Windows/MacOs/Linux operating system
- MySql 8.0 database or equivalent
- Python 3.10 or greater
- pip packages: pandas, numpy, mysql-connector-python, python-dotenv, flask

## **3. Administrative Procedures**
### 3.1 Installation

1. First, open your browser and go to the URL website https://dev.mysql.com/downloads/installer/. Download the
   latest version of MySQL Installer from the website https://dev.mysql.com/downloads/installer/ by clicking the first blue "**Download**" button in the tab "**General Availability (GA) Releases**".
   
2. Second, your browser will automatically take you to the website https://dev.mysql.com/downloads/file/?id=518834 
   where you will officially download the current version of MySQL Installer as a result of clicking on the hyperlink message "**No thanks, just start my download.**" at the bottom of the website https://dev.mysql.com/downloads/file/?id=518834. Wait for the download to finish loading as it pops up at the bottom of the web page which you will then click to begin installing the MySQL Installer.   

3. Third, within either the Microsoft Windows Command Prompt, Visual Studio Code, PyCharm, or any other possible
   source-code editor that can run Python code, type the following commands in your terminal to successfully install those commands:
   * pip install mysql-connector-python
   * py -m pip install install python-dotenv
   * pip install Flask
   * pip install pandas
   * pip install numpy
      - NOTE: Make sure that the installation commands are installed in the correct "C:\...." File Path where your  Python File will be located. 

4. In Microsoft Windows Command Prompt or Source-Code Editor that you chose, open the file "**database.py**"  
   and make edits to the values that are assigned to the configuration variables in lines 6 to 10             within the "**mydb = mysql.connector.connect()**" changing all the configuration values to match the mysql server you are running:
   - **host=** <Name of Your Host\>
   - **user=** <Your Database User Name\>
   - **password=** <The Connection Port\>
   - **database=** <Name of the Database\>

5. Next, in the Source Code Editor of your choosing, either Windows Command Prompt, Visual Studio Code, 
   PyCharm, etc., run the "**database.py**" Python code in a terminal based on the version of Python you have installed on your computer by running the command "**python database.py**".
   ```
   WARNING: Do not press "Ctrl + C" on your computer keyboard or laptop keyboard to stop the Python
   File "database.py" from running, otherwise, the data tables coded in the "database.py" Python File
   will not be generated in your MySQL Workbench.
   ```

6. Then, if you are using Microsoft Windows, click on the Windows "**Start**" menu located on the bottom left-corner
   of your computer screen and then in the Search Bar next to the Windows "**Start**" menu, type "**mysql**" to search for "**MySQL 8.0 Command Line Client**" App on your computer. The "**MySQL 8.0 Command Line Client**" Application will be used to ensure that name of the database that the user has given in line 10                  of the "**database.py**" Python Code is recognized by the "**MySQL Workbench 8.0 CE**" App. This will           be done  by first checking that the name of the database assigned to "**database_name=**" in line 10             of the "**database.py**" Python Code exists by running the command "**show DATABASES;**" in "**MySQL 8.0 Command Line Client**" to list all databases that exist for running in MySQL. If one of the listed database names matches the assigned value that you typed earlier in the single quotation marks '' after "**database_name=**" in line 10 of "**database.py**" Python code, then skip Step 7 and go onto Step 8, otherwise, continue to Step 7   if "**MySQL 8.0 Command Line Client**" did not list the name of your database that you manually typed earlier in the single quotation marks '' after "**database_name=**" in line 10 of the Python code "**database.py**".

7. In "**MySQL 8.0 Command Line Client**" type "**CREATE DATABASE**", then the name of the database that            
   you assigned to "**database_name=**" in line 10 of "**database.py**" Python code before you ran it, and then a semicolon "**;**". For example, if you assigned the value of the name of your database within the single quotation marks '' after "**database_name=**" in line 10 of the "**database.py**" Python code to the default name "**crime_database**" then the full command that you would type and then execute in "**MySQL 8.0 Command Line Client**" would be "**CREATE DATABASE crime_database;**". As a result of rerunning the                     command "**show DATABASES;**", you will now see that one of the databases listed in "**MySQL 8.0 Command Line Client**" matches up with the name of your database that you manually typed earlier within the single quotation marks '' after "**database_name=**" in line 10 of the Python Code "**database.py**".

8. Then, if you are using Microsoft Windows, click on the Windows "**Start**" menu located on the bottom
   left-corner of your computer screen and then in the Search Bar next to the Windows "**Start**" menu,             type "**mysql workbench**" to search for "**MySQL Workbench 8.0 CE**" App on your computer. The "**MySQL Workbench 8.0 CE**" Application will be the tool to use for generating all possible Structured Query Language SQL expressions after running the Python Code "**database.py**" in your terminal.

9. Click on the "**MySQL Workbench 8.0 CE**" App and it will automatically open the "**MySQL Workbench**"
   Window. When it opens, you should see the large font message saying "**Welcome to MySQL Workbench**" and then under the "**MySQL Connections**" section below "**Local instance MySQL80**", you should see the value for your MySQL User Name that should be typed between the single quotes '' in line 7 after "**user=**" in the Python  File "**database.py**" and in the second line you should see the value of your port number that should be typed between the single quotes '' in line 9 after "**port=**" in the "**database.py**" Python File. 

10. Click on "**Local instance MySQL80**" under the "**MySQL Connections**" section in the "**MySQL Workbench**" 
    Window. After you click "**Local instance MySQL80**", a small "**Connect to MySQL Server**" Window will pop up on your computer screen that will ask you for the password you created for your MySQL Account. Therefore, type your password in the rectangular entry box after "**Password:**" to successfully connect to your Local Host and then at the bottom of the "**Connnect to MySQL Server**" Window, press the "**OK**" button which will automatically open the SQL Editor in the "**MySQL Workbench**" Window.

11. Then in "**Navigator**" on the left side of your SQL Editor in "**MySQL Workbench**" Window,
    under the "**Filter objects**" Search Bar after "**SCHEMAS**", double left-click on the right            triangle icon before the cylinder icon that shows the name of the database that you typed                    before running the "**database.py**" Python File that is the assigned value for your database               name "**database=**" within the single quotes on line 10 of "**database.py**" Python code. 

12. Under the "**Tables**" section, Right-Click "**crime**" and then Left-Click "**Select Rows - Limit 1000**"
    that will display the generated output data for the "**crime**" data table. Right-Click "**crime_type**"      under the "**Tables**" section and then Left-Click "**Select Rows - Limit 1000**" that will display the generated output data for the "**crime_type**" data table. Under the "**Tables**" section,                 Right-Click "**neighborhood**" and then Left-Click "**Select Rows - Limit 1000**" that will display the generated output data for "**neighborhood**" data table. Last but not least, Right-Click "**weapon**"       under the "**Tables**" section and then Left-Click "**Select Rows - Limit 1000**" that will display the generated output data for "**weapon**" data table.

### 3.2 Routine Tasks
- **Replace Crime Data**
    1. Replace the "**Median Household Income - Baltimore.xlsx**", "**neighborhood_food.csv**",
       and "**Part_1_Crime_Data.csv**" files with the new data.

    2. Run the "**database.py**" python file with the command "**python database.py**".

### 3.3 Periodic Administration
- **System Backup**
    1. Backup Mysql Database using the mysqldump command "**mysqldump <database name\> > backup-<current date\>. sql**".

- **Restore Database from Backup**
    1. Open the Mysql terminal application, if you are using Microsoft Windows, click on the Windows "**Start**" menu located on the bottom left-corner of of your computer screen and then in the Search Bar next to the Windows "**Start**" menu, type "**mysql**" to search for "**MySQL 8.0 Command Line Client**".

    2. Once in the MySql terminal app type "**use <database name\>;**" and hit enter to select the database.

    3. Use the "**Source**" command to select a "**.sql**" file to use. For example, "**source backup-2023-05-11.sql**" and hit enter.

## **4. Troubleshooting**
### 4.1 Dealing with Error Messages and Failures
If the database fails or crashes, follow the instructions in section 3.3 to restore the database from a backup. If the database isn't backed up follow the installation instructions as nessicary to re-install the database.
If the site itself crashes or fails stop running app.py and restart it. If when you try to run app.py you get an error about not finding a file or function, check that you properly followed the installiation instructions and installed all nessicary libraries and files.

### 4.2 Known Bugs and Limitations
There are currently no known bugs in the system.
Current system limitations include hosting and the filters. Currently, the system is built using a Flask app, and can only be hosted locally. In other words, it can only be accessed from the local device. In addition, the filters are limited. You can only use one filter at a time, the app doesn't have the funconality to apply multiple filters at once. In addition, there is little customization for the filters. You can filter the data using the buttons that filter by preset values. For example, if you wanted to filter by date you can only choose to view by all time, last 5 years, last year, or last month.
The system is also limited in terms of what data you can see. The avaiable data for the crimes is limited, and you can only view the overall data. There is currently no implementation for viewing data about a specific crime, or data about specific types of crimes.

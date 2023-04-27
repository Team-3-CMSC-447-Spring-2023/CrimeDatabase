# Instructions for Installing MySQL, Running "database.py" Python File, and Generating Tables for the Crime Database in MySQL Workbench:

1. First, open your browser and go to the URL website https://dev.mysql.com/downloads/installer/. Download the latest version 
   of MySQL Installer from the website https://dev.mysql.com/downloads/installer/ by clicking the first blue "Download" button in the
   tab "General Availability (GA) Releases".
   
2. Second, your browser will automatically take you to the website https://dev.mysql.com/downloads/file/?id=518834 where you will
   officially download the current version of MySQL Installer as a result of clicking on the hyperlink message "No thanks, just start my download." at the bottom of the website https://dev.mysql.com/downloads/file/?id=518834. Wait for the download to finish loading as it pops up at the bottom of the web page which you will then click to begin installing the MySQL Installer.   

3. Third, within either the Microsoft Windows Command Prompt, Visual Studio Code, PyCharm, or any other possible source-code editor that 
   can run Python code, type the following commands in your terminal to successfully install those commands:
   pip install mysql-connector-python
   py -m pip install install python-dotenv
   pip install pandas
   pip install numpy
   NOTE: Make sure that the installation commands are installed in the correct "C:\...." File Path where your Python File will be located. 

4. In Microsoft Windows Command Prompt or Source-Code Editor that you chose, open the file "database.py" and make edits to the values
   that are assigned to the configuration variables in lines 6 to 10 within the "mydb = mysql.connector.connect()" changing all the configuration values after 'host=', 'user=', 'password=', 'port=', and 'database=' to match the mysql server you are running.

5. Next, in the Source Code Editor of your choosing, either Windows Command Prompt, Visual Studio Code, PyCharm, etc., 
   run the "database.py" Python code in a terminal based on the version of Python you have installed on your computer, that is most likely either Python 2 or Python 3, by running either the command "python database.py" if you are using Python 2 or the
   command "python3 database.py" if you are using Python 3. WARNING: Do not cancel press "Shift + C" to stop the "database.py" from running, otherwise, the data tables coded in the "database.py" Python File will not be generated in your MySQL Workbench.

6. Then, if you are using Microsoft Windows, click on the Windows "Start" menu located on the bottom left-corner of your computer screen
   and then in the Search Bar next to the Windows "Start" menu, type "mysql workbench" to search for "MySQL Workbench 8.0 CE" App
   on your computer. The "MySQL Workbench 8.0 CE" Application will be the tool to use for generating all possible Structured Query
   Language SQL expressions after running the "database.py" Python code in your terminal. 

7. Click on the "MySQL Workbench 8.0 CE" App and it will automatically open the "MySQL Workbench" Window. When it opens you should 
   see the large font message saying "Welcome to MySQL Workbench". Under the "MySQL Connections" section below "Local instance MySQL80", you should see the value for your MySQL User Name that should be typed between the single quotes '' in line 7 after "user=" in the
   Python File "database.py" and in the second line you should see the value of your port number that should be typed between the single quotes '' in line 9 after "port=" in the "database.py" Python File. 

8. Click on "Local instance MySQL80" under the "MySQL Connections" section in the "MySQL Workbench" window. After you click "Local
   instance MySQL80", a small "Connect to MySQL Server" Window will pop up on your computer screen that will ask you for the password you created for your MySQL Account. Therefore, type your password in the rectangular entry box after "Password:" to successfully connect to your Local Host and then at the bottom of the "Connnect to MySQL Server" Window, press the "OK" button which will automatically open the SQL Editor in the "MySQL Workbench" Window.

9. Then in "Navigator" on the left side of your SQL Editor in "MySQL Workbench" Window, under the "Filter objects" Search Bar
   after "SCHEMAS", double left-click on the right triangle icon before the cylinder icon that shows the name of the database that 
   you typed before running the "database.py" Python File that is the assigned value for your database name "database=" within the 
   single quotes on line 10 of "database.py" Python code. 

10. Under the "Tables" section, Right-Click "crime" and then Left-Click "Select Rows - Limit 1000" that will display the generated output
    data for the "crime" data table. Right-Click "crime_type" under the "Tables" section and then left-click "Select Rows - Limit 1000" that will display the generated output data for the "crime_type" data table. Under the "Tables" section, right-click "neighborhood" and then Left-Click "Select Rows - Limit 1000" that will display the generated output data for "neighborhood" data table. Last but not least, Right-Click "weapon" under the "Tables" section and then left-click "Select Rows - Limit 1000" that will display the generated output data for "weapon" data table.
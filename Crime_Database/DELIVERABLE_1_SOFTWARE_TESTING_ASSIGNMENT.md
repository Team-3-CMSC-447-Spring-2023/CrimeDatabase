# Deliverable 1 Software Testing Assignment
## Test Cases for `database.py`
### **Authors of All Test Cases on Database Side**: Talha Hussain, Thomas Nguyen 
### **Testers of All Test Cases on Database Side**: Talha Hussain, Thomas Nguyen 
&nbsp;
### **Database Black Box Testing for Crime Database**
| # | Description | Input Parameters | Expected Output | Actual Output | P/F Criteria | Comments |
|---|-------------|------------------|-----------------|---------------|--------------|----------|
| 1 | database.py: Run Data Entry. | Not needed. | Database to Have All Tables: crime, crime_type, weapon, neighborhood<br><br>Crime Table has 560,038 Rows.<br>Crime Inserted includes 543,335 Rows.<br>Crime with Missing Data includes 16,703 Rows.<br>Crime Type Table has 86 Rows.<br>Weapon Table has 23 Rows.<br>Neighborhood Table has 279 Rows. | Database to Have All Tables: crime, crime_type, weapon, neighborhood<br><br>Crime Table has 560,038 Rows.<br>Crime Inserted includes 543,335 Rows.<br>Crime with Missing Data includes 16,703 Rows.<br>Crime Type Table has 86 Rows.<br>Weapon Table has 23 Rows.<br>Neighborhood Table has 279 Rows. | Actual Output = Expected Output | Everything worked as expected.<br><br>Missing data includes:<br>    - Invalid Weapons<br>    - Invalid Latitude<br>    - Invalid Longitude |

### **Database White Box Testing for Crime Database**
| # | Description | Input Parameters | Expected Output | Actual Output | P/F Criteria | Comments |
|---|-------------|------------------|-----------------|---------------|--------------|----------|
| 1 | Selecting Data from Database | Id: 12 | "crime_id = 12, <br>type_name = 6G, <br>type_Description = LARCENY,<br> longtitude = -76.609948, <br>latitude = 39.354788, <br>weapon_id = 0" | "crime_id = 12, <br>type_name = 6G, <br>type_Description = LARCENY, <br>longtitude = -76.6099, <br>latitude = 39.3548, <br>weapon_id = 0" | Actual Output = Expected Output | Floating Point Values were rounded. |
| 2 | database.py: dropTables() Function | Not needed. | Return Value = 0,<br>No Tables in the Database. | Return Value = 0,<br>No Tables in the Database. | Actual Output = Expected Output | All working correctly. |
| 3 | database.py: createTables() Function | Not needed. | Return Value = 0,<br>Tables: weapon, neighborhood, crime_type, crime | Return Value = 0,<br>Tables: weapon, neighborhood, crime_type, crime | Actual Output = Expected Output | All working correctly. |
| 4 | database.py: insertWeapon(crime_data) Function | Not needed. | Return Value = 0,<br>Length of Weapon Table = 11 | Return Value = 0,<br>Length of Weapon Table = 11 | Actual Output = Expected Output | All working correctly. |
| 5 | database.py: insertNeighborhood(crime_data) Function | Not needed. | Return Value = 0,<br>Length of Neighborhood Table = 170 | Return Value = 0,<br>Length of Neighborhood Table = 170 | Actual Output = Expected Output | All working correctly. |
| 6 | database.py: insertCrime_type(crime_data) Function | Not needed. | Return Value = 0,<br>Length of Crime Type Table = 33 | Return Value = 0,<br>Length of Crime Type Table = 33 | Actual Output = Expected Output | All working correctly. |
| 7 | database.py: insertCrime(crime_data) Function | Not needed. | Return Value = 0,<br>Length of Crime Table = 462 | Return Value = 0,<br>Length of Crime Table = 462 | Actual Output = Expected Output | All working correctly. |

All tests were able to be performed without issue, for the White Box Testing, we utilized a sub-sample of the      first 500 lines from the "Part_1_Crime_Data.csv" Comma-Separated Values CSV File to ensure quick testing of the  functions. The only tests with values that were not identical was White Box Test #1 where the floating point representation that MySQL Workbench used rounded the value to 4 decimal places.

There were no defects in the code written to build the database structure or to fill it with information from the Excel Microsoft Office Open Extensible Markup Language XML Format Spreadsheet and Comma-Separated Values CSV  Files. We built the `test_database.py` file to automate testing of the individual functions and to provide data out for ease of tests.
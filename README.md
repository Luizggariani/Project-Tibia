# Project-Tibia

![Tibia icon](https://www.tibiabr.com/wp-content/uploads/2017/12/TibiaDragonLogo_HighRes.png)

## Description of the project and objectives to do:

This is a project that I'm going to do to learn more about the Python Language, SQL and a DBMS and then using PowerBI to show some of the data extracted from the API of Tibia.

1. Tibia API

2. Objective of this project

Extract the data from the API of Tibia in creatures (https://api.tibiadata.com/v4/creatures) and insert into a MySQL database.

In the MySQL you should create a database called "Tibia" and a schema called "tibia_api" and a table called "creatures" with the following columns:

- 'name'
- 'race'
- 'image_url'
- 'featured'

Here is the documentation to download MySQL: https://www.mysql.com/

The table in MySQL should have 638 rows as the API had in the moment that I wrote this README ('26/09/2024'). 

---

### Step-by-step guide for my project:

1- **Check Necessary Installations**
* Check Python Installation
* Check Python Installation
* Check Power BI Installation
* Verify Required Python Libraries

2- **Create the Database in MySQL**
*  Open MySQL and create the database and the table

3- **Connect to the Tibia API**
* Access the Tibia API and get creature data. ** Py request

4- **Insert Data into MySQL**
* Insert the extracted API data into the MySQL database. 

5- **Verify Data Insertion**
* Use SELECT * FROM tibia_api.creatures to check if the data was inserted correctly

6- **Create Visualizations in Power BI**
* Connect Power BI to your MySQL database. 
* Choose MySQL Database create the connection and import the creatures table.
* Create graphs and visualizations to explore the Tibia creatures.

***


### 🛠️ Technologies and Tools Used
* Python (3.9)
* MySQL Workbench (8.0)
* Power BI
* Python libraries: requests, mysql-connector-python, MySQLdb

### 🎯 Objectives
* Extract creature information from the Tibia API.
* Store this data in a creatures table within a MySQL database organized with a specific schema.
* Visualize and explore the data in Power BI, creating charts and analyses.
 
### 💡 Lessons learned and considerations

This data analysis project provided me with an excellent opportunity to apply and consolidate knowledge of data extraction with APIs, MySQL database management and visualization with Power BI. Throughout the process, I was able to experiment with automating data collection, processing and storing information, as well as creating visual reports that make data accessible and informative.

Each stage - from start to finish - presented challenges and valuable learnings, strengthening the mastery of the tools and techniques used.

This project is just a starting point for other data analysis applications.

# Project-Tibia

![Tibia icon](https://www.tibiawiki.com.br/images/7/76/Tibia_icon.png)


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

### Day 1 - create a step-by-step guide for my project:

1- **Check Necessary Installations** - Done.
* Check Python Installation
* Check Python Installation
* Check Power BI Installation
* Verify Required Python Libraries

2- **Create the Database in MySQL** - Done.
*  Open MySQL and create the database and the table
  
3- **Connect to the Tibia API** done.
* Access the Tibia API and get creature data. ** Py request

4- **Insert Data into MySQL** done. 
* Insert the extracted API data into the MySQL database. 

5- **Verify Data Insertion** done.
* Use SELECT * FROM tibia_api.creatures to check if the data was inserted correctly

6- **Create Visualizations in Power BI**
* Connect Power BI to your MySQL database. done
* Choose MySQL Database create the connection and import the creatures table. done
* Create graphs and visualizations to explore the Tibia creatures. All done.

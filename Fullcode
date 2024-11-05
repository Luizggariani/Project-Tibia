import requests
import MySQLdb  # mysqlclient library to connect to MySQL

# Step 1: Extracting data from the API
url = "https://api.tibiadata.com/v4/creatures"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    creatures = data['creatures']['creature_list']
    print(f"{len(creatures)} creatures successfully extracted from API.")
else:
    print(f"Erro ao acessar a API: {response.status_code}")
    creatures = []  # Ensure that the variable exists, even if the API fails

# Step 2: Database connection and insertion
if creatures:
    connection = None
    cursor = None  # Initialize the cursor as None
    try:
        # Conectando ao MySQL
        connection = MySQLdb.connect(
            host="127.0.0.1",
            user="root",        # Replace with your MySQL user
            passwd="*********",        # Replace with your MySQL password
            db="tibia"                 # Database name
        )

        print("MySQL connection was successfully established!")

        cursor = connection.cursor()

        # Inserting the data into MySQL
        for creature in creatures:
            name = creature['name']
            race = creature['race']
            image_url = creature['image_url']
            featured = creature['featured']

            query = """
            INSERT INTO tibia.creatures (name, race, image_url, featured)
            VALUES (%s, %s, %s, %s)
            """
            values = (name, race, image_url, featured)

            cursor.execute(query, values)

        connection.commit()
        print("Data entered successfully!")

    except MySQLdb.Error as e:
        print(f"Error connecting or inserting data into MySQL: {e}")

    finally:
        # Closing the cursor and the connection.
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection to MySQL has been closed.")
else:
    print("No data available to insert into the database.")
# End

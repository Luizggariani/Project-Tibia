## Full Code

import psycopg2
import requests

def create_schema_and_table():
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="user",
            password="user",
            dbname="Tibia"
        )
        cursor = conn.cursor()

        cursor.execute("CREATE SCHEMA IF NOT EXISTS tibia_api;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tibia_api.creatures (
                id SERIAL PRIMARY KEY,
                name TEXT,
                race TEXT,
                image_url TEXT,
                featured BOOLEAN
            );
        """)

        conn.commit()
        print("Schema e tabela criados (se não existiam).")
    except psycopg2.Error as e:
        print(f"Erro ao criar schema/tabela: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_creatures_data():
    url = "https://api.tibiadata.com/v4/creatures"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            creatures = data['creatures']['creature_list']
            print(f"{len(creatures)} criaturas obtidas da API.")
            return creatures
        else:
            print(f"Erro ao acessar API: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Erro na requisição da API: {e}")
        return []

def insert_data_into_postgres(creatures):
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="user",
            password="user",
            dbname="Tibia"
        )
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO tibia_api.creatures (name, race, image_url, featured) 
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """

        for creature in creatures:
            cursor.execute(insert_query, (
                creature['name'],
                creature['race'],
                creature['image_url'],
                creature['featured']
            ))

        conn.commit()
        print(f"{cursor.rowcount} registros inseridos no banco.")
    except psycopg2.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    create_schema_and_table()
    creatures_data = get_creatures_data()
    if creatures_data:
        insert_data_into_postgres(creatures_data)

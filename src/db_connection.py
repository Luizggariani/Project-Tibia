##Setup_database_structure

##Criar o banco de dados e a tabela (estrutura base)

import psycopg2

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
    except psycopg2.Error as e:
        print(f"Erro ao criar schema/tabela: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    create_schema_and_table()

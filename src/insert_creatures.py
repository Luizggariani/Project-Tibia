##Inserir os dados extraídos no banco

import psycopg2

def insert_data_into_postgres(creatures):
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
        """

        for creature in creatures:
            cursor.execute(insert_query, (
                creature['name'], 
                creature['race'], 
                creature['image_url'], 
                creature['featured']
            ))

        conn.commit()
        print(f"{cursor.rowcount} registros inseridos com sucesso!")

    except psycopg2.Error as err:
        print(f"Erro: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

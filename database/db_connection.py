import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mario0518",
            database="my_database"
        )
        if conn.is_connected():
            return conn
        else:
            print("Conexiune nereusita.")
            return None
    except mysql.connector.Error as err:
        print(f"Eroare la conectare: {err}")
        return None

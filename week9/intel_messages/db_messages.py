import mysql.connector

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "secret"
DB = "soldiers_db"
PORT = 3306

def get_connection() -> mysql.connector.connect:
    return mysql.connector.connect(
        host= HOST,
        user = USER,
        password= PASSWORD,
        database= DB,
        port= PORT
    )

def get_schema():
    conn = get_connection()
    cursor = conn.cursor()

    query =     """
            DESCRIBE messages
                """
    rows = cursor.fetchall()
    cursor.execute(query)
    conn.close()
    cursor.close()
    return rows

def get_all_messages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
                SELECT * FROM messages
            """
    rows = cursor.fetchall()
    cursor.execute(query)
    conn.close()
    cursor.close()
    return rows



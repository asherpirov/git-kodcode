import mysql.connector
import time

PORT = 3307
USER = "root"
PASSWORD = "secret"
HOST = "localhost"
DB = "soldiers_db"



def get_connection():
    time.sleep(2)
    return mysql.connector.connect(host="127.0.0.1",
                                   user="root",
                                   password="secret",
                                   port=3306,
                                   database="soldiers_db")
get_connection()
def setup():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
            CREATE TABLE IF NOT EXISTS soldiers (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            rank_ VARCHAR(50),
            unit VARCHAR(100),
            active BOOLEAN DEFAULT TRUE
            )
        """
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close()

def get_schema():
    conn = get_connection()
    cursor = conn.corsur()
    query = """ 
        DESCRIBE soldiers 
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_soldiers():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT * FROM soldiers_db
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows



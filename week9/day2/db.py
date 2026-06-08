import mysql.connector
import time

PORT = 3306
USER = "root"
PASSWORD = "secret"
HOST = "localhost"
DB = "soldiers_db"




def get_connection() -> mysql.connector:
    return mysql.connector.connect(host= HOST,
                                   user= USER,
                                   password= PASSWORD,
                                   port= PORT,
                                   database= DB)


def get_all() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    query = """
        SELECT * FROM soldiers_db
            """
    cursor.execute(query)
    soldiers = cursor.fetchall()
    conn.close()
    cursor.close()
    return soldiers

def get_by_id(soldier_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    query = """
            SELECT FROM soldiers_db WHERE id == %s
            """
    cursor.execute(query, (soldier_id,))
    soldier = cursor.fetchall()
    conn.close()
    cursor.close()
    return soldier

def create(name, rank, unit) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
               INSERT INTO soldiers_db (name, rank_, unit) VALUES (%s, %s, %s)
            """
    cursor.execute(query,(name, rank, unit))
    new_id = cursor.lastrowid()
    conn.close()
    cursor.close()
    return new_id

def update(soldier_id, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
                UPDATE soldiers_db SET rank_=%s WHERE id=%s
            """
    cursor.execute(query, (data["rank"], soldier_id))
    has_update = cursor.rowcount > 0
    conn.close()
    cursor.close()
    return has_update

def delete(soldier_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
               DELETE FROM soldiers_db WHERE id=%s
            """
    cursor.execute(query, (soldier_id,))
    has_deleted = cursor.rowcount > 0
    conn.close()
    cursor.close()
    return has_deleted


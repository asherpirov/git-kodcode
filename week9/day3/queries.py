import mysql.connector

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "secret"
DB = "soldiers_db"
PORT = 3306


def get_connection() -> mysql.connetor.connect:
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB,
        port=PORT
    )


def get_soldiers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT * FROM soldiers
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def filter_by_rank(rank: str)-> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            SELECT * FROM soldiers WHERE rank_ = %s
            """
    cursor.execute(query,(rank,))
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows


def sort_soldiers(sort:str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = f"""
                SELECT * FROM soldiers ORDER BY name {sort}
             """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_all_unit():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
                SELECT DISTINCT unit FROM soldiers
                """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_unit(unit):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            SELECT * FROM soldiers WHERE unit = %s
                """
    cursor.execute(query,(unit,))
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_name(name):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
                    SELECT * FROM soldiers WHERE name LIKE %s
                    """
    cursor.execute(query, ("%" + name + "%",))
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def missing_rank():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            SELECT * FROM soldiers WHERE rank_ IS NULL
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

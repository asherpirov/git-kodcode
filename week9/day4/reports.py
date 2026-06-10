from week9.day1.db_mangment import get_connection

def get_summary():
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    summary = {}
    total_query = """
            SELECT COUNT(*) AS "total" FROM soldiers
            """
    cursor.execute(total_query)
    total_rows = cursor.fetchone()
    summary["total"] = total_rows["total"]

    active_query = """
                SELECT COUNT(*) AS active FROM soldiers WHERE active = 1
                    """
    cursor.execute(active_query)
    active_rows = cursor.fetchone()
    summary["active"] = active_rows["active"]

    inactive_query = """
                    SELECT COUNT(*) AS inactive FROM soldiers WHERE active = 0 
                    """
    cursor.execute(inactive_query)
    inactive_rows = cursor.fetchone()
    summary["inactive"] = inactive_rows["inactive"]

    conn.close()
    cursor.close()
    return summary

def count_by_unit():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
                SELECT unit, COUNT(unit) AS total FROM soldiers GROUP BY unit
                """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_units_with_multiple_soldiers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
             SELECT unit FROM soldiers GROUP BY unit HAVING COUNT(unit) > 1
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows



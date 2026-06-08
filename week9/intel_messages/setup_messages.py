from db_messages import get_connection

SCHEMA = """
        id INT PRIMARY KEY AUTO_INCREMENT,
        unit VARCHAR(100) NOT NULL, 
        classification ENUM("unclassified", "confidential", "secret", "top_secret")
        content TEXT NOT NULL,
        source VARCHAR(100), 
        created_at DATETIME DEFAULT NOW()
        
         """

def setup_table():
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
        CREATE TABLE messages IF NOT EXISTS ({SCHEMA})
            """

    cursor.execute(query)
    conn.close()
    cursor.close()


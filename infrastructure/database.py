import mysql.connector
from mysql.connector import pooling

db_config = {
    'host': 'localhost',
    'port': '3306',
    'user': 'todo_app',
    'password': 'ra5cai7fei5U',
    'database': 'todo_app'
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="todo_pool",
    pool_size=5,
    **db_config
)

def get_connection():
    return connection_pool.get_connection()

# Run this script to initialize the database
def initialize_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos (
        id VARCHAR(36) PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        completed BOOLEAN DEFAULT FALSE,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL
    )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

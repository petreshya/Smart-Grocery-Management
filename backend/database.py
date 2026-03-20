import sqlite3

def get_connection():
    conn = sqlite3.connect("grocery.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS grocery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            category TEXT,
            price REAL,
            priority TEXT,
            purchase_frequency INTEGER
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            monthly_budget REAL
        )
    ''')

    conn.commit()
    conn.close()

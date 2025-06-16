import sqlite3

def connect():
    conn = sqlite3.connect('130625.db')  # Nombre de la base de datos
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS productos')  # Eliminar la tabla si existe
    cursor.execute('''
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

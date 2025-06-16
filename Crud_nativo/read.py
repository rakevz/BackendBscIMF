from conexion import connect

def read_items():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')  # Nombre de la tabla
    items = cursor.fetchall()
    conn.close()
    return items

if __name__ == "__main__":
    items = read_items()
    for item in items:
        print(f'ID: {item[0]}, Name: {item[1]}')

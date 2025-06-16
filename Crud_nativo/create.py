from conexion import connect

def create_item(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos (name) VALUES (?)', (name,))  # Nombre de la tabla
    conn.commit()
    conn.close()
    print(f'Producto "{name}" creado con éxito.')

if __name__ == "__main__":
    item_name = input("Ingrese el nombre del producto a crear: ")
    create_item(item_name)

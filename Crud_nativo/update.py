from conexion import connect

def update_item(item_id, new_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE productos SET name = ? WHERE id = ?', (new_name, item_id))  # Nombre de la tabla
    conn.commit()
    conn.close()
    print(f'Producto con ID {item_id} actualizado a "{new_name}".')

if __name__ == "__main__":
    item_id = int(input("Ingrese el ID del producto a actualizar: "))
    new_name = input("Ingrese el nuevo nombre del producto: ")
    update_item(item_id, new_name)

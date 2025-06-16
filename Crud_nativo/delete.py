from conexion import connect

def delete_item(item_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id = ?', (item_id,))  # Nombre de la tabla
    conn.commit()
    conn.close()
    print(f'Producto con ID {item_id} eliminado con éxito.')

if __name__ == "__main__":
    item_id = int(input("Ingrese el ID del producto a eliminar: "))
    delete_item(item_id)

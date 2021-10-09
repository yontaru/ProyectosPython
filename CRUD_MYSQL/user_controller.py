from bd import get_connection # Importar la conexión a la BD

# Insertar usuario
def insert_user(name, email, telefono, passwd):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO user(name, email, telefono, passwd) VALUES(%s, %s, %s, %s)", (name, email, telefono, passwd))
    connection.commit()
    connection.close()

#Obtener todos los usuarios
def get_user():
    connection = get_connection()
    users = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, telefono, passwd FROM user")
        users = cursor.fetchall()
    connection.close()
    return users

#Eliminar usuario
def delete_user(id):
    connection = get_connection()
    user = None
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        user=cursor.fetchone()
    connection.commit()
    connection.close()
    return user

#Obtener un usuario por su ID
def get_user_by_id(id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, telefono, passwd FROM user WHERE id = %s", (id,))
        user=cursor.fetchone()
    connection.close()
    return user

#Actualizar un usuario
def update_user(name, email, telefono, passwd, id):
    conecction = get_connection()
    with conecction.cursor() as cursor:
        cursor.execute("UPDATE user SET name = %s, email = %s, telefono = %s, passwd = %s  WHERE id = %s", (name, email, telefono, passwd, id))
    conecction.commit()
    conecction.close()


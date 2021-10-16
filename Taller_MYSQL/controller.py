from db import get_connection

cnn=get_connection()

def insert_customer(name, status, mobile):
    cnn=get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO costumer (name, status, mobile) VALUES(%s, %s, %s)", (name, status, mobile))
    cnn.commit()
    cnn.close()

def get_customer():
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer")
        users=cursor.fetchall()
    cnn.close()
    return users
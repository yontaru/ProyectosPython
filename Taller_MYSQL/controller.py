from db import get_connection


def insert_customer(name, status, mobile):
    cnn=get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO customer (name, status, mobile) VALUES(%s, %s, %s)", (name, status, mobile))
    cnn.commit()
    cnn.close()

def get_customer():
    cnn=get_connection()
    users = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer")
        users=cursor.fetchall()
    cnn.close()
    return users

def delete_customer(id):
    cnn=get_connection()
    user = None
    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM customer WHERE id = %s", (id,))
        user=cursor.fetchone()
    cnn.commit()
    cnn.close()
    return user

def get_customer_by_id(id):
    cnn=get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer WHERE id = %s", (id,))
        user=cursor.fetchone()
    cnn.close()
    return user

def update_customer(name, status, mobile, id):
    cnn=get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE customer SET name = %s, status = %s, mobile= %s WHERE id = %s",(name, status, mobile, id))
    cnn.commit()
    cnn.close()


def insert_invoice(number, date, price, balance):
    cnn=get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO invoice (number, date, price, balance) VALUES(%s, %s, %s, %s)", (number, date, price, balance))
    cnn.commit()
    cnn.close()

def get_invoice():
    cnn=get_connection()
    users = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, number, date, price, balance FROM invoice")
        users=cursor.fetchall()
    cnn.close()
    return users

def delete_invoice(id):
    cnn=get_connection()
    user = None
    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM invoice WHERE id = %s AND balance = 0", (id))
        user=cursor.fetchone()
    cnn.commit()
    cnn.close()
    return user

def get_invoice_by_id(id):
    cnn=get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, number, date, price, balance FROM invoice WHERE id = %s", (id,))
        user=cursor.fetchone()
    cnn.close()
    return user

def update_invoice(number, date, price, balance, id):
    cnn=get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE invoice SET number = %s, date = %s,  price= %s, balance = %s WHERE id = %s",(number, date, price, balance, id))
    cnn.commit()
    cnn.close()
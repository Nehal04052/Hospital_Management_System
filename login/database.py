import mysql.connector
from mysql.connector import Error
from getpass import getpass
from hashlib import pbkdf2_hmac
import binascii

def hash_password(password):
    salt = b'somesalt'  # Use a secure random salt in a real application
    return binascii.hexlify(pbkdf2_hmac('sha256', password.encode(), salt, 100000)).decode()

def create_connection(username, password, database):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database=database
        )
        return mydb
    except Error as e:
        print(e)
        return None  # Return None if an error occurred


def create_account(mydb, firstname, lastname, email, username, password, usertype):
    if mydb is not None:
        cursor = mydb.cursor()
        hashed_password = hash_password(password)
        query = "INSERT INTO users (firstname, lastname, email, username, password, usertype) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (firstname, lastname, email, username, hashed_password, usertype)
        cursor.execute(query, values)
        mydb.commit()
        return True  # Return True if the account was created successfully
    else:
        print("Could not connect to database")
        return False  # Return False if the account could not be created


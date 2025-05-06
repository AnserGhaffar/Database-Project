import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="username",  #enter your username
            password="password",  #enter your password
            database="game_store"  
        )
        if conn.is_connected():
            print("Connection established")
        return conn
    except Error as err:
        print(f"Error: {err}")
        return None

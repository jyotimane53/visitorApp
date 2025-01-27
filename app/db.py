import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',       # Replace with your MySQL username
            password='rootpassword',  # Replace with your MySQL password
            database='visitor_management'  # Replace with your MySQL database name
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except Error as e:
        print(f"Error while connecting to the database: {e}")
        return None

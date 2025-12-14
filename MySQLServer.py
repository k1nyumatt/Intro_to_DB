import mysql.connector
from mysql.connector import Error

def create_database():
    """Create alx_book_store database if it doesn't exist"""
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Remnantone1!"  # Replace with your MySQL password
        )
        
        # Create cursor
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        # Close cursor if it exists
        if cursor:
            cursor.close()
        
        # Close connection if it exists
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
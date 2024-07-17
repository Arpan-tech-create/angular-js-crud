import mysql.connector
from mysql.connector import Error

def connect_to_database():
    """
    Establish a connection to the MySQL database.
    
    Returns:
        conn: A MySQLConnection object if successful, None otherwise.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port='3305',
            user="root",
            password="mysqlinstaller@001",
            database="bi"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print("Error connecting to the database:", e)
        return None

def get_distinct_regions():

    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT region FROM entry;")
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            return results
        except Error as e:
            print("Error executing the query:", e)
            if conn.is_connected():
                cursor.close()
                conn.close()
            return None

def get_details(region):
    conn=connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            query="SELECT fname,marks,dept from entry where region=%s order by marks asc;"
            cursor.execute(query,(region,))
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            return results
        except Error as e:
            print("Error executing the query:", e)
            if conn.is_connected():
                cursor.close()
                conn.close()
            return None
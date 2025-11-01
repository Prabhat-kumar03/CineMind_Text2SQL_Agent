import os
import dotenv
import mysql.connector

dotenv.load_dotenv('.env')

def get_or_connect_db():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("HOST"),
            user=os.environ.get("USER"),  # Replace with your MySQL username
            password=os.environ.get("PASSWORD"),  # Replace with your MySQL password
            database=os.environ.get("DATABASE") # Optional: specify a database
        )
        print(connection)
        
        if connection.is_connected():
            print("Successfully connected to MySQL database.")
            return connection
        
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        
# get_or_connect_db()
def execute_sql_query(connection, sql_query : str):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print ("Error in sql execution")
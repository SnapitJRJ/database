import sqlite3
from sqlite3 import Error

def create_connection(path2):
    connection = None
    try:
        connection = sqlite3.connect(path2)
        print("Connection to SQlite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
    
    
create_connection("toDatabase")



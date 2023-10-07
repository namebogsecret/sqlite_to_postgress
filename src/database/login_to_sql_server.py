
from sqlite3 import connect, Error

#login to sql server with credentials
def login_to_sql_server(path_to_sql_file):
    # Create a connection to the database
    try:
        connection = connect(path_to_sql_file)
    except Error as _:
        connection = None
    # Return the connection
    return connection

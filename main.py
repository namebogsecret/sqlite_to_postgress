
from sys import exit as sys_exit

from src.database.copy_data_from_sqlite_to_postgres import copy_data_from_sqlite_to_postgres
from src.database.create_postgres_tables import create_postgres_tables
from src.database.get_sqlite_tables_structure import get_sqlite_tables_structure
#from src.database.get_unique_data_types import get_unique_data_types
from src.database.login_to_sql_server import login_to_sql_server
from src.configuration.pathes import DB_PATH
from src.database.login_to_postgres import login_to_postgres


sqlite_connection = login_to_sql_server(DB_PATH)
if sqlite_connection is None:
    print("Не удалось подключиться к базе данных SQLite.")
    sys_exit()

postgres_connection = login_to_postgres()
if postgres_connection is None:
    print("Не удалось подключиться к базе данных Postgres.")
    sys_exit()

sqlite_cursor = sqlite_connection.cursor()
postgres_cursor = postgres_connection.cursor()

"""unique_data_types = get_unique_data_types(sqlite_cursor)
print(unique_data_types)
"""

sqlite_structure = get_sqlite_tables_structure(sqlite_cursor)
create_postgres_tables(postgres_cursor, sqlite_structure)
postgres_connection.commit()
copy_data_from_sqlite_to_postgres(sqlite_cursor, postgres_cursor, sqlite_structure)
postgres_connection.commit()
postgres_cursor.close()
sqlite_cursor.close()

postgres_connection.close()
sqlite_connection.close()



from src.database.table_exists import table_exists


def create_postgres_tables(cursor, structure):
    for table_name, columns in structure.items():
        if table_name == "sqlite_sequence":
            continue
        if table_exists(cursor, table_name):
            print(f"Table {table_name} already exists. Skipping creation.")
            continue
        columns_definition = []
        for column in columns:
            column_name = column[1]

            # Заменяем имя столбца "do" на "ido"
            if column_name == "do":
                column_name = "ido"

            # Преобразуем типы данных SQLite в PostgreSQL
            sqlite_type = column[2].upper()
            postgres_type = {
                'INTEGER': 'INTEGER',
                'TEXT': 'TEXT',
                'REAL': 'FLOAT',
                'FLOAT': 'FLOAT'
            }.get(sqlite_type, sqlite_type)
            
            columns_definition.append(f"{column_name} {postgres_type}")
        query = f"CREATE TABLE {table_name} ({', '.join(columns_definition)});"
        cursor.execute(query)

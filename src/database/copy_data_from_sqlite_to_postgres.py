
from src.database.convert_empty_strings_to_none import convert_empty_strings_to_none

def copy_data_from_sqlite_to_postgres(sqlite_cursor, postgres_cursor, structure):
    for table_name, columns in structure.items():
        if table_name == "sqlite_sequence":
            continue
        # Получение имен столбцов из SQLite и их преобразование
        column_names = [col[1] for col in columns]
        column_names = ["ido" if name == "do" else name for name in column_names]
        
        sqlite_cursor.execute(f"SELECT * FROM {table_name};")
        rows = sqlite_cursor.fetchall()
        
        # Convert empty strings to None for integer columns
        rows = convert_empty_strings_to_none(rows, columns)
        
        placeholders = ",".join(["%s"] * len(columns))
        columns_str = ",".join(column_names)
        
        postgres_cursor.executemany(f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});", rows)

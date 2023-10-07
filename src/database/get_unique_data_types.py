
def get_unique_data_types(cursor):
    # Извлекаем имена всех таблиц из базы данных
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("В базе данных нет таблиц.")
        return set()

    data_types = set()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        if not columns:
            print(f"Таблица {table_name} не имеет столбцов.")
            continue

        for column in columns:
            data_type = column[2]
            data_types.add(data_type)

    return data_types


def table_exists(cursor, table_name):
    cursor.execute(f"SELECT EXISTS (SELECT 1 FROM pg_tables WHERE tablename='{table_name}');")
    return cursor.fetchone()[0]

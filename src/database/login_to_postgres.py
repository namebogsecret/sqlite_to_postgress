
from os import getenv
import psycopg2
#from psycopg2 import Error
#from psycopg2.extras import execute_values
import dotenv

dotenv.load_dotenv()

def create_database():
    try:
        # Подключаемся к postgres (стандартной базе данных) для создания новой базы данных
        connection = psycopg2.connect(
            dbname="cars",
            user=getenv("user"),
            password=getenv("password"),
            host=getenv("host")
        )
        connection.autocommit = True  # Включаем автокоммит, так как создание базы данных должно быть немедленным
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {getenv('dbname')};")
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print(f"Ошибка при создании базы данных: {e}")
        return False

def login_to_postgres():
    try:
        connection = psycopg2.connect(
            dbname=getenv("dbname"),
            user=getenv("user"),
            password=getenv("password"),
            host=getenv("host")
        )
        return connection
    except psycopg2.OperationalError:  # Если ошибка связана с отсутствием базы данных
        # Попытка создать базу данных
        if create_database():
            return login_to_postgres()
        else:
            print("Не удалось создать базу данных.")
            return None
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None


import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from contextlib import closing

# Подключение к базе данных PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="38836699",
            host="localhost",
            port="5433",
        )
        print("Соединение установлено")
        return conn
    except Exception as e:
        print(f"Не удалось установить соединение: {e}")
        return None

# Функция для поиска группы с фильтрами
def find_group(filters):
    with closing(get_db_connection()) as conn:
        if conn is None:
            return None
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM groups WHERE filters = %s", (filters,)
                )
                group = cursor.fetchone()
                print(f"Найдена группа: {group}")
                return group
        except Exception as e:
            print(f"Ошибка при выполнении запроса find_group: {e}")
            return None

# Функция для добавления нового пользователя в группу
def add_user_to_group(user_id, group_id):
    with closing(get_db_connection()) as conn:
        if conn is None:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO user_groups (user_id, group_id) VALUES (%s, %s)",
                    (user_id, group_id)
                )
                conn.commit()
                print(f"Пользователь с ID {user_id} был добавлен в группу с ID {group_id}")
        except Exception as e:
            print(f"Ошибка при выполнении запроса add_user_to_group: {e}")
            conn.rollback()

# Функция для создания новой группы с фильтрами
def create_group(filters):
    with closing(get_db_connection()) as conn:
        if conn is None:
            return None
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO groups (filters) VALUES (%s) RETURNING id",
                    (filters,)
                )
                group_id = cursor.fetchone()[0]
                conn.commit()
                print(f"Создана новая группа с ID {group_id}")
                return group_id
        except Exception as e:
            print(f"Ошибка при выполнении запроса create_group: {e}")
            conn.rollback()
            return None

# Функция для добавления пользователя в таблицу users, если его там нет
def add_user(telegram_id, username):
    with closing(get_db_connection()) as conn:
        if conn is None:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (telegram_id, username) VALUES (%s, %s) ON CONFLICT (telegram_id) DO NOTHING",
                    (telegram_id, username)
                )
                conn.commit()
                print(f"Пользователь с ID {telegram_id} добавлен в таблицу users")
        except Exception as e:
            print(f"Ошибка при выполнении запроса add_user: {e}")
            conn.rollback()

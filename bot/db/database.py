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


# Словарь для временного хранения данных о фильтрах пользователей
user_filters_temp = {}


# Функция для временного сохранения фильтров
def temp_save_user_filters(telegram_id, category=None, subcategory=None, level=None):
    if telegram_id not in user_filters_temp:
        user_filters_temp[telegram_id] = {}

    if category:
        user_filters_temp[telegram_id]['category'] = category
    if subcategory:
        user_filters_temp[telegram_id]['subcategory'] = subcategory
    if level:
        user_filters_temp[telegram_id]['level'] = level




def save_or_update_group(telegram_id):
    # Получаем фильтры пользователя из временного хранилища
    filters = user_filters_temp.get(telegram_id)
    if not filters:
        print(f"Фильтры для пользователя {telegram_id} не найдены.")
        return

    category = filters.get('category')
    subcategory = filters.get('subcategory')
    level = filters.get('level')

    # Проверка на существование группы с такими фильтрами
    with closing(get_db_connection()) as conn:
        if conn is None:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT id, user_ids FROM groups
                    WHERE category = %s AND subcategory = %s AND level = %s
                """, (category, subcategory, level))
                group = cursor.fetchone()

                if group:
                    # Группа существует, добавляем пользователя
                    group_id, user_ids = group
                    user_ids.append(telegram_id)
                    cursor.execute("""
                        UPDATE groups
                        SET user_ids = %s
                        WHERE id = %s
                    """, (user_ids, group_id))
                    conn.commit()
                    print(f"Пользователь {telegram_id} добавлен в существующую группу {group_id}.")
                else:
                    # Группа не существует, создаем новую
                    cursor.execute("""
                        INSERT INTO groups (category, subcategory, level, user_ids)
                        VALUES (%s, %s, %s, %s) RETURNING id
                    """, (category, subcategory, level, [telegram_id]))
                    new_group_id = cursor.fetchone()[0]
                    conn.commit()
                    print(f"Создана новая группа с ID {new_group_id} для пользователя {telegram_id}.")

        except Exception as e:
            print(f"Ошибка при сохранении группы: {e}")
            conn.rollback()


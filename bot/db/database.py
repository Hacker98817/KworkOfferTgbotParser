# Подключение к базе данных PostgreSQL
import asyncpg

async def get_db_connection():
    try:
        conn = await asyncpg.connect(
            user="postgres",
            password="38836699",
            database="postgres",
            host="localhost",
            port="5433",
        )
        print("Соединение установлено")
        return conn
    except Exception as e:
        print(f"Не удалось установить соединение: {e}")
        return None

# Функция для добавления пользователя в таблицу users, если его там нет

async def add_user(telegram_id, username):
    conn = await get_db_connection()  # Асинхронное подключение
    if conn is None:
        return

    try:
        # Выполняем SQL-запрос
        await conn.execute(
            """
            INSERT INTO users (telegram_id, username)
            VALUES ($1, $2)
            ON CONFLICT (telegram_id) DO NOTHING
            """,
            telegram_id, username
        )
        print(f"Пользователь с ID {telegram_id} добавлен в таблицу users")
    except Exception as e:
        print(f"Ошибка при выполнении запроса add_user: {e}")
    finally:
        # Закрываем соединение
        await conn.close()

# Словарь для временного хранения данных о фильтрах пользователей
user_filters_temp = {}

async def get_link(telegram_id):
    #telegram_id = list(user_filters_temp.keys())[0]
    # Извлекаем значения для конкретного пользователя
    if telegram_id not in user_filters_temp:
        return None

    # Извлекаем значение subcategory
    subcategory_link = user_filters_temp[telegram_id]['subcategory']
    link_tier = subcategory_link+user_filters_temp[telegram_id]['tier']
    link_payment = link_tier+user_filters_temp[telegram_id]['payment']
    link_location = link_payment+user_filters_temp[telegram_id]['location']+'&per_page=50'
    return link_location


# Функция для временного сохранения фильтров
def temp_save_user_filters(telegram_id, **kwargs):

    """
        Сохраняет или обновляет временные фильтры пользователя.
        """
    if telegram_id not in user_filters_temp:
        user_filters_temp[telegram_id] = {}

    # Обновляем фильтры из переданных параметров
    for key, value in kwargs.items():
        if value is not None:
            user_filters_temp[telegram_id][key] = value



async def save_or_update_group(telegram_id):
    # Получаем фильтры пользователя из временного хранилища
    filters = user_filters_temp.get(telegram_id)
    if not filters:
        print(f"Фильтры для пользователя {telegram_id} не найдены.")
        return

    # Формируем ссылку на основе фильтров
    link = await get_link(telegram_id)
    print(f'{link} создана.')
    if not link:
        print(f"Не удалось создать ссылку для пользователя {telegram_id}.")
        return


    category = filters.get('category')
    subcategory = filters.get('subcategory')
    level = filters.get('level')

    conn = await get_db_connection()  # Асинхронное подключение к базе данных
    if conn is None:
        return  # Если подключение не удалось

    try:
        # Проверка на существование группы с такими фильтрами
        group = await conn.fetchrow("""
            SELECT id, user_ids, link
            FROM groups
            WHERE category = $1 AND subcategory = $2 AND level = $3
        """, category, subcategory, level)

        if group:
            # Группа существует, добавляем пользователя
            group_id = group['id']
            user_ids = group['user_ids']
            user_ids.append(telegram_id)

            await conn.execute("""
                UPDATE groups
                SET user_ids = $1, link = $2
                WHERE id = $3
            """, user_ids, link, group_id)
            print(f"Пользователь {telegram_id} добавлен в существующую группу {group_id}.")
        else:
            # Группа не существует, создаем новую
            new_group_id = await conn.fetchval("""
                INSERT INTO groups (category, subcategory, level, user_ids, link)
                VALUES ($1, $2, $3, $4, $5)
                RETURNING id
            """, category, subcategory, level, [telegram_id], link)
            print(f"Создана новая группа с ID {new_group_id} для пользователя {telegram_id}.")
    except Exception as e:
        print(f"Ошибка при сохранении группы: {e}")
    finally:
        # Закрываем соединение
        await conn.close()


async def get_all_groups_with_links():
    conn = await asyncpg.connect(database="postgre", user="postgre", password="38836699")
    try:
        # Получаем все группы и их ссылки
        groups = await conn.fetch("""
            SELECT id, link
            FROM groups;
        """)
        return groups
    except Exception as e:
        print(f"Ошибка при получении групп: {e}")
        return []
    finally:
        await conn.close()





#DELETE_GROUP
# Получение списка групп, в которых состоит пользователь
async def get_user_groups(telegram_id: int):
    query = """
    SELECT id, category 
    FROM groups 
    WHERE $1 = ANY(user_ids)
    """
    conn = await get_db_connection()
    try:
        groups = await conn.fetch(query, telegram_id)
        return groups
    finally:
        await conn.close()


# Удаление пользователя из указанной группы
async def remove_user_from_group(telegram_id: int, group_id: int):
    query = """
    UPDATE groups 
    SET user_ids = array_remove(user_ids, $1) 
    WHERE id = $2
    """
    conn = await get_db_connection()
    try:
        await conn.execute(query, telegram_id, group_id)
        print(f"Пользователь {telegram_id} удален из группы {group_id}")
    finally:
        await conn.close()


#Попытка создать сохранение заказов в таблицу
#async def save_order_to_cache(user_id, order_id):
#    """
#    Сохраняет заказ в таблице sent_orders, чтобы избежать повторной отправки.
#    """
#    conn = await get_db_connection()
#    if conn is None:
#        return

#    try:
#        await conn.execute(
#            """
#            INSERT INTO sent_orders (telegram_id, order_id)
#            VALUES ($1, $2)
#            ON CONFLICT (telegram_id, order_id) DO NOTHING
#            """,
#            user_id, int(order_id)  # Преобразуем order_id в int
#        )
#        print(f"Заказ с ID {order_id} сохранен для пользователя {user_id}.")
#    except Exception as e:
#        print(f"Ошибка при сохранении заказа {order_id} для пользователя {user_id}: {e}")
#    finally:
#        await conn.close()



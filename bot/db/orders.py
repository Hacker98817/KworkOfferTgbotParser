import asyncpg
import asyncio

# Функция для получения асинхронного подключения к базе данных PostgreSQL
async def get_db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="38836699",
        database="postgres",
        host="localhost",
        port="5433"
    )

# Функция для вставки данных в таблицу orders
async def save_order_to_db(order_data):
    conn = await get_db_connection()

    try:
        # Обновление заказа, если его order_id уже существует
        await conn.execute(
            """
            INSERT INTO orders (order_id, title, order_url)
            VALUES ($1, $2, $3)
            ON CONFLICT (order_id) 
            DO UPDATE 
            SET title = EXCLUDED.title, order_url = EXCLUDED.order_url;
            """,
            order_data["order_id"], order_data["title"], order_data["order_url"]
        )
        print(f'Заказ {order_data["order_id"]} сохранен или обновлен.')
    except Exception as e:
        print(f"Ошибка при сохранении заказа в БД: {e}")
    finally:
        await conn.close()





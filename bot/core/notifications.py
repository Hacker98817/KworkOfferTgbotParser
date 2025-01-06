import redis.asyncio as redis
import asyncio
from aiogram import Bot
from bot.db.database import get_db_connection
from bot.core.upwork_parser import parse_upwork_async

redis_client = None


async def init_redis():
    global redis_client
    redis_client = redis.from_url("redis://localhost", decode_responses=True)
    try:
        await redis_client.ping()
        print("Redis подключен успешно.")
    except Exception as e:
        print(f"Ошибка подключения к Redis: {e}")
        redis_client = None


async def fetch_all_groups():
    conn = await get_db_connection()
    if conn is None:
        print("Не удалось подключиться к базе данных.")
        return []
    try:
        rows = await conn.fetch("SELECT id, link, user_ids FROM groups WHERE link IS NOT NULL")
        return [{"id": row['id'], "link": row['link'], "user_ids": row['user_ids']} for row in rows]
    except Exception as e:
        print(f"Ошибка при получении данных групп: {e}")
        return []
    finally:
        await conn.close()


async def is_order_cached(user_id, order_id):
    cache_key = f"order:{user_id}:{order_id}"
    return await redis_client.exists(cache_key)


async def save_order_to_cache(user_id, order_id):
    cache_key = f"order:{user_id}:{order_id}"
    await redis_client.setex(cache_key, 86400, "sent")


async def send_results_to_users(bot: Bot, user_ids, results):
    """Отправить результаты парсинга всем пользователям из списка user_ids."""
    for user_id in user_ids:
        try:
            messages = []  # Для накопления новых сообщений
            for result in results:
                # Формируем сообщение
                message = f"Название: {result['title']}\nСсылка: {result['link']}\nДата публикации: {result['date_posted']}\nИнформация о работе: {result['job_info']}"

                # Добавляем сообщение в список, если оно не дублируется
                order_id = result['link'].split("~")[-1].split("/")[0]  # Уникальный идентификатор заказа
                if not await is_order_cached(user_id, order_id):
                    await save_order_to_cache(user_id, order_id)
                    messages.append(message)
                else:
                    print(f"Заказ '{result['title']}' уже отправлен пользователю {user_id}, пропускаем.")

            # Разделение сообщений на блоки по 10 заказов
            if messages:
                # Разбиваем список сообщений на блоки по 10 сообщений
                chunks = [messages[i:i + 10] for i in range(0, len(messages), 10)]

                # Отправляем каждый блок сообщений как одно сообщение
                for chunk in chunks:
                    combined_message = "\n\n".join(chunk)
                    await bot.send_message(user_id, combined_message)
                print(f"Отправлено {len(messages)} заказов пользователю {user_id}.")
            else:
                print(f"Нет новых заказов для пользователя {user_id}.")
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")



async def process_group(bot: Bot, group):
    try:
        print(f"Начинаю парсинг для группы {group['id']}, ссылка: {group['link']}")
        results = await parse_upwork_async(group['link'])
        if results:
            await send_results_to_users(bot, group['user_ids'], results)
        print(f"Сообщения отправлены пользователям группы {group['id']}")
    except Exception as e:
        print(f"Ошибка при парсинге группы {group['id']}: {e}")


async def process_all_links(bot: Bot):
    while True:
        groups = await fetch_all_groups()
        if not groups:
            print("Нет данных для парсинга.")
        else:
            tasks = [process_group(bot, group) for group in groups]
            await asyncio.gather(*tasks)
        print("Ожидание 5 минут перед следующим парсингом...")
        await asyncio.sleep(300)



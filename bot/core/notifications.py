from aiogram import Bot
from bot.db.database import get_db_connection
from bot.core.upwork_parser import parse_upwork_async
import asyncio

async def fetch_all_groups():
    """Получить все группы и связанные с ними ссылки."""
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


async def send_results_to_users(bot: Bot, user_ids, results):
    """Отправить результаты парсинга пользователям."""
    for user_id in user_ids:
        try:
            if not results:
                await bot.send_message(user_id, "По вашему запросу новых заказов не найдено.")
            else:
                for result in results:
                    message = f"Название: {result['title']}\nСсылка: {result['link']}"
                    await bot.send_message(user_id, message)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")


async def process_all_links(bot: Bot):
    """Парсинг для всех ссылок из таблицы groups с уведомлением пользователей."""
    while True:
        groups = await fetch_all_groups()
        if not groups:
            print("Нет данных для парсинга.")
        else:
            for group in groups:
                group_id = group["id"]
                link = group["link"]
                user_ids = group["user_ids"]

                try:
                    print(f"Начинаю парсинг для группы {group_id}, ссылка: {link}")
                    results = await parse_upwork_async(link)
                    print(f"Результаты парсинга для группы {group_id}: {results}")
                    await send_results_to_users(bot, user_ids, results)
                except Exception as e:
                    print(f"Ошибка при парсинге для группы {group_id}, ссылка {link}: {e}")

        print("Ожидание 5 минут перед следующим парсингом...")
        await asyncio.sleep(300)  # Ожидание 5 минут

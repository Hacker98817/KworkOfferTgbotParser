from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router as telegram_router
from bot.core.notifications import process_all_links
from bot.core.notifications import init_redis
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.db.database import get_db_connection
import asyncio

#BOT_TOKEN = "8121447155:AAHbO67DuqTrjeGQtTYIOhEgxxldUmMHzP0"  # Замените на токен вашего бота
BOT_TOKEN = "7857122796:AAGCHTF5uIOrrANidrx3Mag3rT2RF-YBcM4"

# Асинхронная функция для удаления пустых групп
async def delete_empty_groups():
    print("Удаляем пустые группы...")
    query = """
        DELETE FROM groups
        WHERE user_ids = '{}'
        """

    conn = await get_db_connection()
    try:
        # Выполняем удаление пустых групп
        result = await conn.execute(query)

        if result:
            print("Пустые группы были успешно удалены.")
        else:
            print("Нет пустых групп для удаления.")
    except Exception as e:
        print(f"Ошибка при удалении пустых групп: {e}")
    finally:
        await conn.close()

# Создаём планировщик
scheduler = AsyncIOScheduler()

# Функция для старта планировщика
async def start_scheduler():
    # Добавляем задачу для регулярного выполнения
    scheduler.add_job(delete_empty_groups, 'interval', minutes=1)  # Удаление раз в 24 часа
    scheduler.start()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    await init_redis()
    # Подключаем обработчики
    dp.include_router(telegram_router)

    # Создаем параллельную задачу для парсинга
    asyncio.create_task(process_all_links(bot))

    # Запуск планировщика
    asyncio.create_task(start_scheduler())

    try:
        print("Бот запущен...")
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Завершение работы...")





if __name__ == "__main__":
    asyncio.run(main())


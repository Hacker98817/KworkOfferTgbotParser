from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router as telegram_router
from bot.db.database import get_db_connection
from bot.core.upwork_parser import parse_upwork_async
from bot.core.notifications import process_all_links
import asyncio

BOT_TOKEN = "8121447155:AAHbO67DuqTrjeGQtTYIOhEgxxldUmMHzP0"  # Замените на токен вашего бота
#BOT_TOKEN = '7857122796:AAGCHTF5uIOrrANidrx3Mag3rT2RF-YBcM4'


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем обработчики
    dp.include_router(telegram_router)

    # Создаем параллельную задачу для парсинга
    asyncio.create_task(process_all_links(bot))

    try:
        print("Бот запущен...")
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Завершение работы...")





if __name__ == "__main__":
    asyncio.run(main())


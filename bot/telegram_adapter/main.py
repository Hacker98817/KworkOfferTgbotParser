from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router as telegram_router
import asyncio
from bot.core.upwork_parser import parse_upwork


BOT_TOKEN = "8121447155:AAHbO67DuqTrjeGQtTYIOhEgxxldUmMHzP0"  # Замените на токен вашего бота

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем обработчики
    dp.include_router(telegram_router)

    try:
        print("Бот запущен...")
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Завершение работы...")

if __name__ == "__main__":
    asyncio.run(main())

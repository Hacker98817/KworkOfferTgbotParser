from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router as telegram_router
import asyncio

BOT_TOKEN = "8121447155:AAHbO67DuqTrjeGQtTYIOhEgxxldUmMHzP0"  # Замените на токен вашего бота

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем обработчики
    dp.include_router(telegram_router)

    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

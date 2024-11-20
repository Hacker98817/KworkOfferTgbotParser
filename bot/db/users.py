import asyncpg
import asyncpg
from database import db_pool  # Используем глобальный пул из database.py
async def add_user(telegram_id: int, filter_name: str, subfilter_name: str):
    """Добавляет пользователя в базу данных."""
    async with db_pool.acquire() as conn:
        # Проверить, существует ли пользователь
        user = await conn.fetchrow(
            "SELECT * FROM users WHERE telegram_id = $1", telegram_id
        )
        if user:
            # Если пользователь существует, обновить его фильтры
            await conn.execute(
                """
                UPDATE users
                SET selected_filter = $1, selected_subfilter = $2
                WHERE telegram_id = $3
                """,
                filter_name, subfilter_name, telegram_id
            )
        else:
            # Если пользователь не существует, добавить нового
            await conn.execute(
                """
                INSERT INTO users (telegram_id, selected_filter, selected_subfilter)
                VALUES ($1, $2, $3)
                """,
                telegram_id, filter_name, subfilter_name
            )

async def find_or_create_group(filter_name: str, subfilter_name: str):
    """Ищет существующую группу или создаёт новую."""
    async with db_pool.acquire() as conn:
        # Проверить, существует ли группа
        group = await conn.fetchrow(
            "SELECT * FROM groups WHERE filter = $1 AND subfilter = $2",
            filter_name, subfilter_name
        )
        if not group:
            # Если группы нет, создаём новую
            group_id = await conn.fetchval(
                """
                INSERT INTO groups (filter, subfilter)
                VALUES ($1, $2)
                RETURNING id
                """,
                filter_name, subfilter_name
            )
            return group_id
        return group["id"]

async def register_user_in_group(telegram_id: int, filter_name: str, subfilter_name: str):
    """Регистрирует пользователя и добавляет его в группу."""
    # Добавить или обновить пользователя
    await add_user(telegram_id, filter_name, subfilter_name)
    # Найти или создать группу
    group_id = await find_or_create_group(filter_name, subfilter_name)
    return group_id

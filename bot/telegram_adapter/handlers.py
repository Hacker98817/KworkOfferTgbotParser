from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from buttons import categories_keyboard, it_subcategory_inline_keyboard, finance_subcategory_inline_keyboard# Импортируем правильную клавиатуру


router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        text="Привет! Выберите категорию, чтобы настроить фильтры:",
        reply_markup=categories_keyboard
    )

@router.callback_query()
async def button_handler(callback: CallbackQuery):
    category_names = {
        "category_dev_it": "Разработка и IT",
        "category_ai_services": "ИИ Услуги",
        "category_design_creative": "Дизайн и Креатив",
        "category_sales_marketing": "Продажи и Маркетинг",
        "category_admin_support": "Администрирование и Поддержка",
        "category_writing_translation": "Письмо и Переводы",
        "category_finance_accounting": "Финансы и Бухгалтерия",
        "category_hr_training": "Кадры и Обучение",
        "category_legal": "Юридические Услуги",
        "category_engineering_architecture": "Инженерия и Архитектура",
    }

    if callback.data in category_names:
        selected_category = category_names[callback.data]

        if callback.data == "category_dev_it":
            # При выборе категории "Разработка и IT" показываем подтемы
            await callback.message.edit_text(
                text=f"Вы выбрали категорию: {selected_category}.\n"
                     f"Выберите подтему:",
                reply_markup=it_subcategory_inline_keyboard  # Используем импортированную клавиатуру
            )

        elif callback.data == "category_finance_accounting":
            #Категория финансов
            await  callback.message.edit_text(
                text=f"Вы выбрали категорию: {selected_category}.\n"
                     f"Выберите подтему:",
                reply_markup=finance_subcategory_inline_keyboard
            )

        else:
            await callback.message.edit_text(
                text=f"Вы выбрали категорию: {selected_category}.\n"
                     f"Настройка фильтров пока не реализована."
            )
    elif callback.data.startswith("subcategory_it_"):
        subcategory_names = {
            "subcategory_it_all_it_networking": "Все - IT и Сетевые технологии",
            "subcategory_it_database_management": "Управление базами данных и администрирование",
            "subcategory_it_erp_crm_software": "Программное обеспечение ERP/CRM",
            "subcategory_it_information_security": "Информационная безопасность и соблюдение стандартов",
            "subcategory_it_network_admin": "Сетевое и системное администрирование",
        }


        if callback.data in subcategory_names:
            selected_subcategory = subcategory_names[callback.data]
            # Отображаем информацию по выбранной подтеме
            await callback.message.edit_text(
                text=f"Вы выбрали подтему: {selected_subcategory}.\n"
                     f"Настройка фильтров для этой подтемы будет реализована в следующем шаге."
            )

    elif callback.data.startswith("subcategory_finance_"):
        subcategory_names_finance = {
            "subcategory_finance_all_finance": "Все - Бухгалтерский учет и консалтинг",
            "subcategory_finance_personal_couch": "Личный и профессиональный Коучинг",
            "subcategory_finance_consalding": "Бухгалтерский учет",
            "subcategory_finance_finance_planing": "Финансовое планирование",
            "subcategory_finance_hr": "Рекрутинг и человеческие ресурсы",
            "subcategory_finance_other_consalting": "Прочее - Бухгалтерский учет и консалтинг",
        }

        if callback.data in subcategory_names_finance:
            selected_subcategory = subcategory_names_finance[callback.data]
            await callback.message.edit_text(
                text=f"Вы выбрали подтему: {selected_subcategory}.\n"
                     f"Настройка фильтров для этой подтемы будет реализована в следующем шаге."
            )


    else:
        await callback.message.edit_text(text="Непонятное действие. Попробуйте снова.")

    await callback.answer()
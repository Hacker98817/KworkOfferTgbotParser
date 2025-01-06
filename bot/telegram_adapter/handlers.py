from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from bot.db.database import add_user
from bot.db.database import temp_save_user_filters, save_or_update_group
from buttons import (
    categories_keyboard,
    accounting_consulting_inline_keyboard,
    admin_support_inline_keyboard,
    customer_service_inline_keyboard,
    data_science_inline_keyboard,
    design_creative_inline_keyboard,
    engineering_architecture_inline_keyboard,
    it_networking_inline_keyboard,
    legal_inline_keyboard,
    sales_marketing_inline_keyboard,
    translation_inline_keyboard,
    web_mobile_software_dev_inline_keyboard,
    writing_inline_keyboard,
    choose_sold_keyboard,
)
from buttons import expirience_level_keyboard, choose_location_keyboard
from bot.telegram_adapter.buttons import menu_keyboard
from bot.db.database import get_user_groups

from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.db.database import get_db_connection

router = Router()


category_data = {
    "category_finance_accounting": {
        "name": "Accounting & Consulting",
        "keyboard": accounting_consulting_inline_keyboard,
        "subcategories": {
            "subcategory_accounting_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency",
            "subcategory_accounting_bookkeeping": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency&subcategory2_uid=1534904461833879552",
            "subcategory_accounting_coaching": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency&subcategory2_uid=531770282601639943",
            "subcategory_accounting_financial_planning": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency&subcategory2_uid=531770282601639945",
            "subcategory_accounting_hr": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency&subcategory2_uid=531770282601639946",
            "subcategory_accounting_management": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency&subcategory2_uid=531770282601639944",
            "subcategory_accounting_other": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency&subcategory2_uid=531770282601639947",
        },
    },
    "category_admin_support": {
        "name": "Admin Support",
        "keyboard": admin_support_inline_keyboard,
        "subcategories": {
            "subcategory_admin_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668416&from=find-work&sort=recency",
            "subcategory_admin_data_entry": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668416&from=find-work&sort=recency&subcategory2_uid=531770282584862724",
            "subcategory_admin_virtual_assistance": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668416&from=find-work&sort=recency&subcategory2_uid=531770282584862725",
            "subcategory_admin_project_management": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668416&from=find-work&sort=recency&subcategory2_uid=531770282584862728",
            "subcategory_admin_market_research": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668416&from=find-work&sort=recency&subcategory2_uid=531770282584862726",
        },
    },
    "category_supports": {
        "name": "Customer Service",
        "keyboard": customer_service_inline_keyboard,
        "subcategories": {
            "subcategory_customer_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668417&from=find-work&sort=recency",
            "subcategory_customer_community_management": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668417&from=find-work&sort=recency&subcategory2_uid=1484275072572772352",
            "subcategory_customer_tech_support": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668417&from=find-work&sort=recency&subcategory2_uid=531770282584862730",
        },
    },
    "category_data_science": {
        "name": "Data Science & Analytics",
        "keyboard": data_science_inline_keyboard,
        "subcategories": {
            "subcategory_data_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668420&from=find-work&sort=recency",
            "subcategory_data_analysis": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668420&from=find-work&sort=recency&subcategory2_uid=531770282593251330",
            "subcategory_data_etl": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668420&from=find-work&sort=recency&subcategory2_uid=531770282593251331",
            "subcategory_data_mining_management": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668420&from=find-work&sort=recency&subcategory2_uid=531770282589057038",
            "subcategory_data_ai_ml": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668420&from=find-work&sort=recency&subcategory2_uid=531770282593251329",
        },
    },
    "category_design_creative": {
        "name": "Design & Creative",
        "keyboard": design_creative_inline_keyboard,
        "subcategories": {
            "subcategory_design_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency",
            "subcategory_design_art": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=531770282593251335",
            "subcategory_design_audio": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=531770282593251341",
            "subcategory_design_branding": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=1044578476142100480",
            "subcategory_design_nft": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=1356688560628174848",
            "subcategory_design_graphic": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=531770282593251334",
            "subcategory_design_performing": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=1356688565288046592",
            "subcategory_design_photography": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=531770282593251340",
            "subcategory_design_product": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=531770282601639953",
            "subcategory_design_video": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668421&from=find-work&sort=recency&subcategory2_uid=1356688570056970240",
        },
    },
    "category_engineering_architecture": {
        "name": "Engineering & Architecture",
        "keyboard": engineering_architecture_inline_keyboard,
        "subcategories": {
            "subcategory_engineering_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency",
            "subcategory_engineering_building": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282601639949",
            "subcategory_engineering_chemical": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282605834240",
            "subcategory_engineering_civil": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282601639950",
            "subcategory_engineering_contract": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282605834241",
            "subcategory_engineering_electrical": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282601639951",
            "subcategory_engineering_interior": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282605834242",
            "subcategory_engineering_energy": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282601639952",
            "subcategory_engineering_physical": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=1301900647896092672",
            "subcategory_engineering_3d_modeling": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862722&from=find-work&sort=recency&subcategory2_uid=531770282601639948",
        },
    },
    "category_dev_it": {
        "name": "IT & Networking",
        "keyboard": it_networking_inline_keyboard,
        "subcategories": {
            "subcategory_it_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668419&from=find-work&sort=recency",
            "subcategory_it_database": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668419&from=find-work&sort=recency&subcategory2_uid=531770282589057033",
            "subcategory_it_erp_crm": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668419&from=find-work&sort=recency&subcategory2_uid=531770282589057034",
            "subcategory_it_security": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668419&from=find-work&sort=recency&subcategory2_uid=531770282589057036",
            "subcategory_it_networking": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668419&from=find-work&sort=recency&subcategory2_uid=531770282589057035",
            "subcategory_it_devops": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668419&from=find-work&sort=recency&subcategory2_uid=531770282589057037",
        },
    },
    "category_legal": {
        "name": "Legal",
        "keyboard": legal_inline_keyboard,
        "subcategories": {
            "subcategory_legal_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862723&from=find-work&sort=recency",
            "subcategory_legal_corporate": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862723&from=find-work&sort=recency&subcategory2_uid=531770282605834246",
            "subcategory_legal_international": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862723&from=find-work&sort=recency&subcategory2_uid=1484275156546932736",
            "subcategory_legal_finance_tax": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862723&from=find-work&sort=recency&subcategory2_uid=531770283696353280",
            "subcategory_legal_public": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862723&from=find-work&sort=recency&subcategory2_uid=1484275408410693632",
        },
    },
    "category_sales_marketing": {
        "name": "Sales & Marketing",
        "keyboard": sales_marketing_inline_keyboard,
        "subcategories": {
            "subcategory_sales_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668422&from=find-work&sort=recency",
            "subcategory_sales_digital": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668422&from=find-work&sort=recency&subcategory2_uid=531770282597445636",
            "subcategory_sales_lead_generation": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668422&from=find-work&sort=recency&subcategory2_uid=531770282597445634",
            "subcategory_sales_marketing_pr": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668422&from=find-work&sort=recency&subcategory2_uid=531770282593251343",
        },
    },
    "category_translation": {
        "name": "Translation",
        "keyboard": translation_inline_keyboard,
        "subcategories": {
            "subcategory_translation_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862720&from=find-work&sort=recency",
            "subcategory_translation_tutoring": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862720&from=find-work&sort=recency&subcategory2_uid=1534904461842268160",
            "subcategory_translation_localization": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862720&from=find-work&sort=recency&subcategory2_uid=531770282601639939",
        },
    },
    "category_web_mobile_software": {
        "name": "Web, Mobile & Software Development",
        "keyboard": web_mobile_software_dev_inline_keyboard,
        "subcategories": {
            "subcategory_dev_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency",
            "subcategory_dev_blockchain": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=1517518458442309632",
            "subcategory_dev_ai": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=1737190722360750082",
            "subcategory_dev_desktop": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057025",
            "subcategory_dev_ecommerce": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057026",
            "subcategory_dev_game": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057027",
            "subcategory_dev_mobile": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057024",
            "subcategory_dev_other": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057032",
            "subcategory_dev_product": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057030",
            "subcategory_dev_qa": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057031",
            "subcategory_dev_scripts": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057028",
            "subcategory_dev_web_mobile_design": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282589057029",
            "subcategory_dev_web": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&from=find-work&sort=recency&subcategory2_uid=531770282584862733",
        },
    },
    "category_writing": {
        "name": "Writing",
        "keyboard": writing_inline_keyboard,
        "subcategories": {
            "subcategory_writing_all": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668423&from=find-work&sort=recency",
            "subcategory_writing_sales": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668423&from=find-work&sort=recency&subcategory2_uid=1534904462131675136",
            "subcategory_writing_content": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668423&from=find-work&sort=recency&subcategory2_uid=1301900640421842944",
            "subcategory_writing_editing": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668423&from=find-work&sort=recency&subcategory2_uid=531770282597445644",
            "subcategory_writing_professional": "https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668423&from=find-work&sort=recency&subcategory2_uid=531770282597445646",
        },
    },
}


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        text="Привет! Это бот заказов. Введите /menu, что бы выбрать дальнейшие действия.")



@router.message(Command("menu"))
async def start_menu(message: Message):
    await message.answer(
        text="Что нужно сделать?",
        reply_markup=menu_keyboard,)


#УДАЛЕНИЕ ФИЛЬТРОВ

@router.callback_query(lambda callback: callback.data == "Delete_group")
async def delete_group(callback: CallbackQuery):
    telegram_id = callback.from_user.id

    groups = await get_user_groups(telegram_id)
    if not groups:
        await callback.message.answer("Вы не состоите ни в одной группе.")
        await callback.answer()
        return

    keyboard_builder = InlineKeyboardBuilder()
    for group in groups:
        keyboard_builder.button(
            text=group["category"],
            callback_data=f"delete_{group['id']}"
        )

    keyboard = keyboard_builder.as_markup()
    await callback.message.answer(
        "Выберите группу для удаления:",
        reply_markup=keyboard
    )
    await callback.answer()


@router.callback_query(lambda callback: callback.data.startswith("delete_"))
async def delete_group_from_db(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    group_id = int(callback.data.split("_")[1])  # Извлекаем ID группы из callback_data

    # Удаляем пользователя из группы
    query = """
    UPDATE groups
    SET user_ids = array_remove(user_ids, $1)
    WHERE id = $2 AND $1 = ANY(user_ids)
    """

    conn = await get_db_connection()
    try:
        result = await conn.execute(query, telegram_id, group_id)

        # Проверяем, было ли удаление
        if result:
            await callback.message.edit_text("Вы успешно удалены из группы.")
        else:
            await callback.message.edit_text("Произошла ошибка при удалении из группы.")
    except Exception as e:
        await callback.message.edit_text(f"Ошибка: {str(e)}")
    finally:
        await conn.close()

    await callback.answer()




#ДОБАВЛЕНИЕ ФИЛЬТРОВ
@router.callback_query(lambda callback: callback.data == "Add_group")
async def start_handler(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    username = callback.from_user.username

    # Добавляем пользователя в базу данных, если его там нет
    await add_user(telegram_id, username)
    await callback.message.edit_text(
        text="Привет! Выберите категорию, чтобы настроить фильтры:",
        reply_markup=categories_keyboard,

    )


#НАМ НУЖНО СДЕЛАТЬ НОРМА КОМАДНУ СТАРТ ГДЕ ИЗ КНОПОК МОЖНО ВЫБРАТЬ ДОБАВЛЕНИЕ ГРУППЫ, КНОПКА УВЕДОМЛЕНИЙ, ИЛИ УДАЛЕНИЕ ГРУППЫ


@router.callback_query()
async def button_handler(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    username = callback.from_user.username

    # Проверяем, выбрана ли категория
    if callback.data in category_data:
        selected_category = category_data[callback.data]
        await callback.message.edit_text(
            text=f"Вы выбрали категорию: {selected_category['name']}.\n"
                 f"Выберите подтему:",
            reply_markup=selected_category["keyboard"],
        )
        # Сохраняем категорию во временные данные
        temp_save_user_filters(telegram_id, category=selected_category["name"])
        return  # Прерываем дальнейшую обработку

    # Проверяем, выбрана ли подкатегория
    for category, data in category_data.items():
        if callback.data in data.get("subcategories", {}):
            subcategory_name = data["subcategories"][callback.data]
            #subcategory_url = callback.data # url страницы

            # Переходим к настройке уровня опыта
            await callback.message.edit_text(
                text=f"Теперь выберите уровень опыта:",
                reply_markup=expirience_level_keyboard,  # Показываем клавиатуру с уровнями
            )
            await callback.answer()

            # Сохраняем подкатегорию во временные данные
            temp_save_user_filters(telegram_id, subcategory=subcategory_name)
            return  # Прерываем дальнейшую обработку

    await callback.answer()






    level_mapping = {
        "category_entry": {
            'description': "Начальный уровень",
            'tier': '&contractor_tier=1'},

        "category_intermediate": {
            'description': "Средний уровень",
            'tier': '&contractor_tier=2'},

        "category_expert": {
            'description': "Экспертный уровень",
            'tier': '&contractor_tier=3'}
    }

    if callback.data in level_mapping:
        selected_level = level_mapping[callback.data]['description']
        tier = level_mapping[callback.data]["tier"]

        # Переходим к настройке оплаты
        await callback.message.edit_text(
            text=f"Вы выбрали {selected_level}.\nВыберете оплату:",
            reply_markup=choose_sold_keyboard,  # Показываем клавиатуру с уровнями
        )
        await callback.answer()

        # Сохраняем уровень во временные данные
        temp_save_user_filters(telegram_id, level=selected_level, tier=tier)

        return  # Прерываем дальнейшую обработку





    sold_mapping = {
        "category_hourly": {
            'description': "Почасовая",
            'payment': '&t=0'},

        "category_fixed_price": {
            'description': "Фиксированная",
            'payment': '&t=1'}
    }

    if callback.data in sold_mapping:
        selected_payment = sold_mapping[callback.data]['description']
        payment = sold_mapping[callback.data]['payment']

        # Переходим к настройке оплаты
        await callback.message.edit_text(
            text=f"Вы выбрали {selected_payment}.\nВыберете регион:",
            reply_markup=choose_location_keyboard,  # Показываем клавиатуру с локациями
        )
        await callback.answer()

        # Сохраняем уровень во временные данные
        temp_save_user_filters(telegram_id, selected_payment=selected_payment, payment=payment)


        await callback.answer()
        return  # Прерываем дальнейшую обработку





    location_mapping = {
        "category_america": {
            'description': "Америка",
            'location': '&location=Americas'},

        "category_europe": {
            'description': "Европа",
            'location': '&location=Europe'},

        "category_asia": {
            'description': "Азия",
            'location': '&location=Asia'},

        "category_africa": {
            'description': "Африка",
            'location': '&location=Africa'},

        "category_india": {
            'description': "Индия",
            'location': '&location=India'},
    }

    if callback.data in location_mapping:
        selected_location = location_mapping[callback.data]['description']
        location = location_mapping[callback.data]['location']
        await callback.message.edit_text(
            text=f"Вы выбрали регион: {selected_location}.\n"
                 f"Настройка завершена! В течении 5 минут поступят заказы.",
        )

        # Сохраняем уровень во временные данные
        temp_save_user_filters(telegram_id, selected_location=selected_location, location=location)

        # Сохраняем фильтры в базу данных и проверяем наличие группы
        await save_or_update_group(telegram_id)

        await callback.answer()
        return  # Прерываем дальнейшую обработку














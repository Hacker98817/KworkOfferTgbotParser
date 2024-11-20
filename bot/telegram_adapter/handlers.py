from aiogram import Router, types
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
)
from buttons import expirience_level_keyboard

router = Router()


categories_keyboard_new = {}

category_data = {
    "category_finance_accounting": {
        "name": "Accounting & Consulting",
        "keyboard": accounting_consulting_inline_keyboard,
        "subcategories": {
            "subcategory_accounting_all": "All - Accounting & Consulting",
            "subcategory_accounting_bookkeeping": "Accounting & Bookkeeping",
            "subcategory_accounting_coaching": "Personal & Professional Coaching",
            "subcategory_accounting_financial_planning": "Financial Planning",
            "subcategory_accounting_hr": "Recruiting & Human Resources",
            "subcategory_accounting_management": "Management Consulting & Analysis",
            "subcategory_accounting_other": "Other - Accounting & Consulting",
        },
    },
    "category_admin_support": {
        "name": "Admin Support",
        "keyboard": admin_support_inline_keyboard,
        "subcategories": {
            "subcategory_admin_all": "All - Admin Support",
            "subcategory_admin_data_entry": "Data Entry & Transcription Services",
            "subcategory_admin_virtual_assistance": "Virtual Assistance",
            "subcategory_admin_project_management": "Project Management",
            "subcategory_admin_market_research": "Market Research & Product Reviews",
        },
    },
    "category_supports": {
        "name": "Customer Service",
        "keyboard": customer_service_inline_keyboard,
        "subcategories": {
            "subcategory_customer_all": "All - Customer Service",
            "subcategory_customer_community_management": "Community Management & Tagging",
            "subcategory_customer_tech_support": "Customer Service & Tech Support",
        },
    },
    "category_data_science": {
        "name": "Data Science & Analytics",
        "keyboard": data_science_inline_keyboard,
        "subcategories": {
            "subcategory_data_all": "All - Data Science & Analytics",
            "subcategory_data_analysis": "Data Analysis & Testing",
            "subcategory_data_etl": "Data Extraction/ETL",
            "subcategory_data_mining_management": "Data Mining & Management",
            "subcategory_data_ai_ml": "AI & Machine Learning",
        },
    },
    "category_design_creative": {
        "name": "Design & Creative",
        "keyboard": design_creative_inline_keyboard,
        "subcategories": {
            "subcategory_design_all": "All - Design & Creative",
            "subcategory_design_art": "Art & Illustration",
            "subcategory_design_audio": "Audio & Music Production",
            "subcategory_design_branding": "Branding & Logo Design",
            "subcategory_design_nft": "NFT, AR/VR & Game Art",
            "subcategory_design_graphic": "Graphic, Editorial & Presentation Design",
            "subcategory_design_performing": "Performing Arts",
            "subcategory_design_photography": "Photography",
            "subcategory_design_product": "Product Design",
            "subcategory_design_video": "Video & Animation",
        },
    },
    "category_engineering_architecture": {
        "name": "Engineering & Architecture",
        "keyboard": engineering_architecture_inline_keyboard,
        "subcategories": {
            "subcategory_engineering_all": "All - Engineering & Architecture",
            "subcategory_engineering_building": "Building & Landscape Architecture",
            "subcategory_engineering_chemical": "Chemical Engineering",
            "subcategory_engineering_civil": "Civil & Structural Engineering",
            "subcategory_engineering_contract": "Contract Manufacturing",
            "subcategory_engineering_electrical": "Electrical & Electronic Engineering",
            "subcategory_engineering_interior": "Interior & Trade Show Design",
            "subcategory_engineering_energy": "Energy & Mechanical Engineering",
            "subcategory_engineering_physical": "Physical Sciences",
            "subcategory_engineering_3d_modeling": "3D Modeling & CAD",
        },
    },
    "category_dev_it": {
        "name": "IT & Networking",
        "keyboard": it_networking_inline_keyboard,
        "subcategories": {
            "subcategory_it_all": "All - IT & Networking",
            "subcategory_it_database": "Database Management & Administration",
            "subcategory_it_erp_crm": "ERP/CRM Software",
            "subcategory_it_security": "Information Security & Compliance",
            "subcategory_it_networking": "Network & System Administration",
            "subcategory_it_devops": "DevOps & Solution Architecture",
        },
    },
    "category_legal": {
        "name": "Legal",
        "keyboard": legal_inline_keyboard,
        "subcategories": {
            "subcategory_legal_all": "All - Legal",
            "subcategory_legal_corporate": "Corporate & Contract Law",
            "subcategory_legal_international": "International & Immigration Law",
            "subcategory_legal_finance_tax": "Finance & Tax Law",
            "subcategory_legal_public": "Public Law",
        },
    },
    "category_sales_marketing": {
        "name": "Sales & Marketing",
        "keyboard": sales_marketing_inline_keyboard,
        "subcategories": {
            "subcategory_sales_all": "All - Sales & Marketing",
            "subcategory_sales_digital": "Digital Marketing",
            "subcategory_sales_lead_generation": "Lead Generation & Telemarketing",
            "subcategory_sales_marketing_pr": "Marketing, PR & Brand Strategy",
        },
    },
    "category_translation": {
        "name": "Translation",
        "keyboard": translation_inline_keyboard,
        "subcategories": {
            "subcategory_translation_all": "All - Translation",
            "subcategory_translation_tutoring": "Language Tutoring & Interpretation",
            "subcategory_translation_localization": "Translation & Localization Services",
        },
    },
    "category_web_mobile_software": {
        "name": "Web, Mobile & Software Development",
        "keyboard": web_mobile_software_dev_inline_keyboard,
        "subcategories": {
            "subcategory_dev_all": "All - Web, Mobile & Software Development",
            "subcategory_dev_blockchain": "Blockchain, NFT & Cryptocurrency",
            "subcategory_dev_ai": "AI Apps & Integration",
            "subcategory_dev_desktop": "Desktop Application Development",
            "subcategory_dev_ecommerce": "Ecommerce Development",
            "subcategory_dev_game": "Game Design & Development",
            "subcategory_dev_mobile": "Mobile Development",
            "subcategory_dev_other": "Other - Software Development",
            "subcategory_dev_product": "Product Management & Scrum",
            "subcategory_dev_qa": "QA Testing",
            "subcategory_dev_scripts": "Scripts & Utilities",
            "subcategory_dev_web_mobile_design": "Web & Mobile Design",
            "subcategory_dev_web": "Web Development",
        },
    },
    "category_writing": {
        "name": "Writing",
        "keyboard": writing_inline_keyboard,
        "subcategories": {
            "subcategory_writing_all": "All - Writing",
            "subcategory_writing_sales": "Sales & Marketing Copywriting",
            "subcategory_writing_content": "Content Writing",
            "subcategory_writing_editing": "Editing & Proofreading Services",
            "subcategory_writing_professional": "Professional & Business Writing",
        },
    },
}



@router.message(Command("start"))
async def start_handler(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    # Добавляем пользователя в базу данных, если его там нет
    add_user(telegram_id, username)
    await message.answer(
        text="Привет! Выберите категорию, чтобы настроить фильтры:",
        reply_markup=categories_keyboard,

    )

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
        await callback.answer()
        # Сохраняем категорию во временные данные
        temp_save_user_filters(telegram_id, category=selected_category["name"])
        return  # Прерываем дальнейшую обработку

    # Проверяем, выбрана ли подкатегория
    for category, data in category_data.items():
        if callback.data in data.get("subcategories", {}):
            selected_subcategory = data["subcategories"][callback.data]
            await callback.message.edit_text(
                text=f"Вы выбрали подтему: {selected_subcategory}.\n"
                     f"Настройка фильтров для этой подтемы будет реализована в следующем шаге."
            )

            # Переходим к настройке уровня опыта
            await callback.message.edit_text(
                text=f"Теперь выберите уровень опыта:",
                reply_markup=expirience_level_keyboard,  # Показываем клавиатуру с уровнями
            )
            await callback.answer()

            # Сохраняем подкатегорию во временные данные
            temp_save_user_filters(telegram_id, subcategory=selected_subcategory)
            return  # Прерываем дальнейшую обработку

    # Если ни категория, ни подкатегория не найдены
    await callback.message.edit_text(text="Непонятное действие. Попробуйте снова.")
    await callback.answer()

    level_mapping = {
        "category_entry": "Начальный уровень",
        "category_intermediate": "Средний уровень",
        "category_expert": "Экспертный уровень",
    }

    if callback.data in level_mapping:
        selected_level = level_mapping[callback.data]
        await callback.message.edit_text(
            text=f"Вы выбрали уровень опыта: {selected_level}.\n"
                 f"Настройка завершена! Спасибо!",
        )

        # Сохраняем уровень во временные данные
        temp_save_user_filters(telegram_id, level=selected_level)

        # Сохраняем фильтры в базу данных и проверяем наличие группы
        await save_or_update_group(telegram_id)

        await callback.answer()
        return  # Прерываем дальнейшую обработку










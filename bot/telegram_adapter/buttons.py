from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

categories_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Разработка и IT", callback_data="category_dev_it")],
    [InlineKeyboardButton(text="ИИ Услуги", callback_data="category_ai_services")],
    [InlineKeyboardButton(text="Дизайн и Креатив", callback_data="category_design_creative")],
    [InlineKeyboardButton(text="Продажи и Маркетинг", callback_data="category_sales_marketing")],
    [InlineKeyboardButton(text="Администрирование и Поддержка", callback_data="category_admin_support")],
    [InlineKeyboardButton(text="Письмо и Переводы", callback_data="category_writing_translation")],
    [InlineKeyboardButton(text="Финансы и Бухгалтерия", callback_data="category_finance_accounting")],
    [InlineKeyboardButton(text="Кадры и Обучение", callback_data="category_hr_training")],
    [InlineKeyboardButton(text="Юридические Услуги", callback_data="category_legal")],
    [InlineKeyboardButton(text="Инженерия и Архитектура", callback_data="category_engineering_architecture")],
])

# Кнопки для подтем категории "Разработка и IT"
it_subcategory_buttons = [
    InlineKeyboardButton(text="Все - IT и Сетевые технологии", callback_data="subcategory_it_all_it_networking"),
    InlineKeyboardButton(text="Управление базами данных и администрирование", callback_data="subcategory_it_database_management"),
    InlineKeyboardButton(text="Программное обеспечение ERP/CRM", callback_data="subcategory_it_erp_crm_software"),
    InlineKeyboardButton(text="Информационная безопасность и соблюдение стандартов", callback_data="subcategory_it_information_security"),
    InlineKeyboardButton(text="Сетевое и системное администрирование", callback_data="subcategory_it_network_admin"),
    InlineKeyboardButton(text="DevOps & Solution Architecture", callback_data="subcategory_it_devops"),
]

it_subcategory_inline_keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=[it_subcategory_buttons])

finance_subcategory_buttons = [
    InlineKeyboardButton(text="Все - Бухгалтерский учет и консалтинг", callback_data="subcategory_finance_all_finance"),
    InlineKeyboardButton(text="Личный и профессиональный Коучинг", callback_data="subcategory_finance_personal_couch"),
    InlineKeyboardButton(text="Бухгалтерский учет", callback_data="subcategory_finance_consalding"),
    InlineKeyboardButton(text="Финансовое планирование", callback_data="subcategory_finance_finance_planing"),
    InlineKeyboardButton(text="Рекрутинг и человеческие ресурсы", callback_data="subcategory_finance_hr"),
    InlineKeyboardButton(text="Прочее - Бухгалтерский учет и консалтинг", callback_data="subcategory_finance_other_consalting"),

]

finance_subcategory_inline_keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=[finance_subcategory_buttons])



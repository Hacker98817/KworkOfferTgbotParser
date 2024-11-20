from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Основные категории
categories_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Accounting & Consulting", callback_data="category_finance_accounting")],
    [InlineKeyboardButton(text="Admin Support", callback_data="category_admin_support")],
    [InlineKeyboardButton(text="Customer Service", callback_data="category_supports")],
    [InlineKeyboardButton(text="Data Science & Analytics", callback_data="category_data_science")],
    [InlineKeyboardButton(text="Design & Creative", callback_data="category_design_creative")],
    [InlineKeyboardButton(text="Engineering & Architecture", callback_data="category_engineering_architecture")],
    [InlineKeyboardButton(text="IT & Networking", callback_data="category_dev_it")],
    [InlineKeyboardButton(text="Legal", callback_data="category_legal")],
    [InlineKeyboardButton(text="Sales & Marketing", callback_data="category_sales_marketing")],
    [InlineKeyboardButton(text="Translation", callback_data="category_translation")],
    [InlineKeyboardButton(text="Web, Mobile & Software Dev", callback_data="category_web_mobile_software")],
    [InlineKeyboardButton(text="Writing", callback_data="category_writing")],
])





# Подкатегории для "Accounting & Consulting" (Бухгалтерский учет и консалтинг)
accounting_consulting_buttons = [
    InlineKeyboardButton(text="All - Accounting & Consulting", callback_data="subcategory_accounting_all"),
    InlineKeyboardButton(text="Personal & Professional Coaching", callback_data="subcategory_accounting_coaching"),
    InlineKeyboardButton(text="Accounting & Bookkeeping", callback_data="subcategory_accounting_bookkeeping"),
    InlineKeyboardButton(text="Financial Planning", callback_data="subcategory_accounting_financial_planning"),
    InlineKeyboardButton(text="Recruiting & Human Resources", callback_data="subcategory_accounting_hr"),
    InlineKeyboardButton(text="Management Consulting & Analysis", callback_data="subcategory_accounting_management"),
    InlineKeyboardButton(text="Other - Accounting & Consulting", callback_data="subcategory_accounting_other"),
]

accounting_consulting_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[accounting_consulting_buttons]
)


# Подкатегории для "Admin Support" (Административная поддержка)
admin_support_buttons = [
    InlineKeyboardButton(text="All - Admin Support", callback_data="subcategory_admin_all"),
    InlineKeyboardButton(text="Data Entry & Transcription Services", callback_data="subcategory_admin_data_entry"),
    InlineKeyboardButton(text="Virtual Assistance", callback_data="subcategory_admin_virtual_assistance"),
    InlineKeyboardButton(text="Project Management", callback_data="subcategory_admin_project_management"),
    InlineKeyboardButton(text="Market Research & Product Reviews", callback_data="subcategory_admin_market_research"),
]

# Admin Support
admin_support_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[admin_support_buttons]
)


# Подкатегории для "Customer Service" (Обслуживание клиентов)
customer_service_buttons = [
    InlineKeyboardButton(text="All - Customer Service", callback_data="subcategory_customer_all"),
    InlineKeyboardButton(text="Community Management & Tagging", callback_data="subcategory_customer_community_management"),
    InlineKeyboardButton(text="Customer Service & Tech Support", callback_data="subcategory_customer_tech_support"),
]

# Customer Service
customer_service_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[customer_service_buttons]
)


# Подкатегории для "Data Science & Analytics" (Наука о данных и аналитика)
data_science_buttons = [
    InlineKeyboardButton(text="All - Data Science & Analytics", callback_data="subcategory_data_all"),
    InlineKeyboardButton(text="Data Analysis & Testing", callback_data="subcategory_data_analysis"),
    InlineKeyboardButton(text="Data Extraction/ETL", callback_data="subcategory_data_etl"),
    InlineKeyboardButton(text="Data Mining & Management", callback_data="subcategory_data_mining_management"),
    InlineKeyboardButton(text="AI & Machine Learning", callback_data="subcategory_data_ai_ml"),
]

# Data Science & Analytics
data_science_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[data_science_buttons]
)


# Подкатегории для "Design & Creative" (Дизайн и креатив)
design_creative_buttons = [
    InlineKeyboardButton(text="All - Design & Creative", callback_data="subcategory_design_all"),
    InlineKeyboardButton(text="Art & Illustration", callback_data="subcategory_design_art"),
    InlineKeyboardButton(text="Audio & Music Production", callback_data="subcategory_design_audio"),
    InlineKeyboardButton(text="Branding & Logo Design", callback_data="subcategory_design_branding"),
    InlineKeyboardButton(text="NFT, AR/VR & Game Art", callback_data="subcategory_design_nft"),
    InlineKeyboardButton(text="Graphic, Editorial & Presentation Design", callback_data="subcategory_design_graphic"),
    InlineKeyboardButton(text="Performing Arts", callback_data="subcategory_design_performing"),
    InlineKeyboardButton(text="Photography", callback_data="subcategory_design_photography"),
    InlineKeyboardButton(text="Product Design", callback_data="subcategory_design_product"),
    InlineKeyboardButton(text="Video & Animation", callback_data="subcategory_design_video"),
]

# Design & Creative
design_creative_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[design_creative_buttons]
)


# Подкатегории для "Engineering & Architecture" (Инженерия и архитектура)
engineering_architecture_buttons = [
    InlineKeyboardButton(text="All - Engineering & Architecture", callback_data="subcategory_engineering_all"),
    InlineKeyboardButton(text="Building & Landscape Architecture", callback_data="subcategory_engineering_building"),
    InlineKeyboardButton(text="Chemical Engineering", callback_data="subcategory_engineering_chemical"),
    InlineKeyboardButton(text="Civil & Structural Engineering", callback_data="subcategory_engineering_civil"),
    InlineKeyboardButton(text="Contract Manufacturing", callback_data="subcategory_engineering_contract"),
    InlineKeyboardButton(text="Electrical & Electronic Engineering", callback_data="subcategory_engineering_electrical"),
    InlineKeyboardButton(text="Interior & Trade Show Design", callback_data="subcategory_engineering_interior"),
    InlineKeyboardButton(text="Energy & Mechanical Engineering", callback_data="subcategory_engineering_energy"),
    InlineKeyboardButton(text="Physical Sciences", callback_data="subcategory_engineering_physical"),
    InlineKeyboardButton(text="3D Modeling & CAD", callback_data="subcategory_engineering_3d_modeling"),
]

# Engineering & Architecture
engineering_architecture_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[engineering_architecture_buttons]
)


# Подкатегории для "IT & Networking" (IT и Сетевые технологии)
it_networking_buttons = [
    InlineKeyboardButton(text="All - IT & Networking", callback_data="subcategory_it_all"),
    InlineKeyboardButton(text="Database Management & Administration", callback_data="subcategory_it_database"),
    InlineKeyboardButton(text="ERP/CRM Software", callback_data="subcategory_it_erp_crm"),
    InlineKeyboardButton(text="Information Security & Compliance", callback_data="subcategory_it_security"),
    InlineKeyboardButton(text="Network & System Administration", callback_data="subcategory_it_networking"),
    InlineKeyboardButton(text="DevOps & Solution Architecture", callback_data="subcategory_it_devops"),
]

# IT & Networking
it_networking_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[it_networking_buttons]
)


# Подкатегории для "Legal" (Юридическая информация)
legal_buttons = [
    InlineKeyboardButton(text="All - Legal", callback_data="subcategory_legal_all"),
    InlineKeyboardButton(text="Corporate & Contract Law", callback_data="subcategory_legal_corporate"),
    InlineKeyboardButton(text="International & Immigration Law", callback_data="subcategory_legal_international"),
    InlineKeyboardButton(text="Finance & Tax Law", callback_data="subcategory_legal_finance_tax"),
    InlineKeyboardButton(text="Public Law", callback_data="subcategory_legal_public"),
]

# Legal
legal_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[legal_buttons]
)


# Подкатегории для "Sales & Marketing" (Продажи и маркетинг)
sales_marketing_buttons = [
    InlineKeyboardButton(text="All - Sales & Marketing", callback_data="subcategory_sales_all"),
    InlineKeyboardButton(text="Digital Marketing", callback_data="subcategory_sales_digital"),
    InlineKeyboardButton(text="Lead Generation & Telemarketing", callback_data="subcategory_sales_lead_generation"),
    InlineKeyboardButton(text="Marketing, PR & Brand Strategy", callback_data="subcategory_sales_marketing_pr"),
]

# Sales & Marketing
sales_marketing_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[sales_marketing_buttons]
)


# Подкатегории для "Translation" (Перевод)
translation_buttons = [
    InlineKeyboardButton(text="All - Translation", callback_data="subcategory_translation_all"),
    InlineKeyboardButton(text="Language Tutoring & Interpretation", callback_data="subcategory_translation_tutoring"),
    InlineKeyboardButton(text="Translation & Localization Services", callback_data="subcategory_translation_localization"),
]

# Translation
translation_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[translation_buttons]
)

#ПРОДОЛЖИТЬ ОТСЮДА
# Подкатегории для "Web, Mobile & Software Dev" (Разработка веб-, мобильных устройств и программного обеспечения)
web_mobile_software_dev_buttons = [
    InlineKeyboardButton(text="All - Web, Mobile & Software Dev", callback_data="subcategory_dev_all"),
    InlineKeyboardButton(text="Blockchain, NFT & Cryptocurrency", callback_data="subcategory_dev_blockchain"),
    InlineKeyboardButton(text="AI Apps & Integration", callback_data="subcategory_dev_ai"),
    InlineKeyboardButton(text="Desktop Application Development", callback_data="subcategory_dev_desktop"),
    InlineKeyboardButton(text="Ecommerce Development", callback_data="subcategory_dev_ecommerce"),
    InlineKeyboardButton(text="Game Design & Development", callback_data="subcategory_game"),
    InlineKeyboardButton(text="Mobile Development", callback_data="subcategory_dev_mobile"),
    InlineKeyboardButton(text="Other - Software Development", callback_data="subcategory_dev_other"),
    InlineKeyboardButton(text="Product Management & Scrum", callback_data="subcategory_dev_product"),
    InlineKeyboardButton(text="QA Testing", callback_data="subcategory_dev_qa"),
    InlineKeyboardButton(text="Scripts & Utilities", callback_data="subcategory_dev_scripts"),
    InlineKeyboardButton(text="Web & Mobile Design", callback_data="subcategory_dev_web_mobile_design"),
    InlineKeyboardButton(text="Web Development", callback_data="subcategory_dev_web"),
]

# Web, Mobile & Software Dev
web_mobile_software_dev_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[web_mobile_software_dev_buttons]
)


# Подкатегории для "Writing" (Написание)
writing_buttons = [
    InlineKeyboardButton(text="All - Writing", callback_data="subcategory_writing_all"),
    InlineKeyboardButton(text="Sales & Marketing Copywriting", callback_data="subcategory_writing_sales"),
    InlineKeyboardButton(text="Content Writing", callback_data="subcategory_writing_content"),
    InlineKeyboardButton(text="Editing & Proofreading Services", callback_data="subcategory_writing_editing"),
    InlineKeyboardButton(text="Professional & Business Writing", callback_data="subcategory_writing_professional"),
]

# Writing
writing_inline_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[writing_buttons]
)



#Кнопки цены
expirience_level = [
    InlineKeyboardButton(text="Entry Level", callback_data="category_entry"),
    InlineKeyboardButton(text="Intermediate", callback_data="category_intermediate"),
    InlineKeyboardButton(text="Expert", callback_data="category_expert"),
]

# Writing
expirience_level_keyboard = InlineKeyboardMarkup(
    row_width=1, inline_keyboard=[expirience_level]
)
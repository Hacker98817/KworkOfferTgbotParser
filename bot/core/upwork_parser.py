from selenium import webdriver
from selenium.webdriver.common.by import By
from bot.db.database import get_link  # Замените `your_module` на правильное имя модуля
import time
import random
from bot.db.orders import save_order_to_db
import asyncpg
import asyncio




# Асинхронная обёртка для парсинга
async def parse_upwork_async(urls):
    return await asyncio.to_thread(parse_upwork, urls)





# Парсинг данных
def parse_upwork(urls):
    results = []

    # Открытие браузера
    driver = webdriver.Chrome()
    driver.get(urls)
    time.sleep(random.uniform(5, 10))  # Случайное ожидание для имитации пользователя

        # Поиск названий и ссылок
    names = driver.find_elements(By.CSS_SELECTOR, "a.up-n-link[data-test='job-tile-title-link UpLink']")

    for name in names:
        title = name.text.strip()  # Название заказа
        link = name.get_attribute("href")  # Ссылка на заказ


        print(f"Название: {title}, Ссылка: {link}")
        results.append({"title": title, "link": link})

        # Формируем данные для сохранения
        order_data = {
            "order_id": link.split("/")[-1],  # Уникальный ID заказа (из ссылки)
            "title": title,
            "order_url": link,
        }

        # Сохраняем данные в базу данных
        asyncio.run(save_order_to_db(order_data))

        # Закрытие браузера
    driver.quit()

    return results



# Асинхронная основная функция
async def main():
    urls = await get_link()
    if not urls:
        print("Нет ссылки для парсинга.")
        return

    # Запускаем парсинг
    results = await parse_upwork_async(urls)

    # Выводим результаты
    print("Результаты парсинга:")
    for result in results:
        print(result)



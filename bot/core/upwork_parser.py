# upwork_parser.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import asyncio

# Параметры для парсинга
#number_of_pages = 1  # Количество страниц для парсинга
#urls = 'https://www.upwork.com/nx/search/jobs/?category2_uid=531770282584862721&from=find-work&sort=recency&subcategory2_uid=531770282601639946'

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

        # Закрытие браузера
    driver.quit()

    return results


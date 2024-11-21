from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Параметры для парсинга
number_of_pages = 1  # Количество страниц для парсинга
urls = [f'https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668419&from=find-work&location=Kazakhstan,United%20States&sort=recency&subcategory2_uid=531770282589057034&t=1&page={page}' for page in range(1, number_of_pages + 1)]

# Парсинг данных
for url in urls:
    # Открытие браузера
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(random.uniform(5, 10))  # Случайное ожидание для имитации пользователя

    # Поиск названий и ссылок
    names = driver.find_elements(By.CSS_SELECTOR, "a.up-n-link[data-test='job-tile-title-link UpLink']")

    for name in names:
        title = name.text.strip()  # Название заказа
        link = name.get_attribute("href")  # Ссылка на заказ
        print(f"Название: {title}, Ссылка: {link}")

    # Закрытие браузера
    driver.quit()



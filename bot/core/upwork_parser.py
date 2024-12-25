from selenium import webdriver
from selenium.webdriver.common.by import By
from bot.db.database import get_link  # Замените `your_module` на правильное имя модуля
import time
import random
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
    time.sleep(random.uniform(2, 5))  # Случайное ожидание для имитации пользователя

        # Поиск названий и ссылок
    names = driver.find_elements(By.CSS_SELECTOR, "a.up-n-link[data-test='job-tile-title-link UpLink']")

    # Ищем все элементы <small> с атрибутом data-v-489be0f1 для дат
    date_elements = driver.find_elements(By.CSS_SELECTOR, 'small[data-v-489be0f1=""]')

    job_info_elements = driver.find_elements(By.CSS_SELECTOR, 'ul[data-test="JobInfo"]')

    # Проверяем, совпадает ли количество ссылок, дат и блоков с информацией о работе
    if len(names) == len(date_elements) == len(job_info_elements):
        for name, date_element, job_info_element in zip(names, date_elements, job_info_elements):
            title = name.text.strip()  # Название заказа
            link = name.get_attribute("href")  # Ссылка на заказ
            date_posted = date_element.text.strip()  # Дата публикации

            # Собираем информацию о работе из списка <ul>
            job_info_set = set()  # Используем множество, чтобы избежать дублирования

            job_info_list = job_info_element.find_elements(By.CSS_SELECTOR, 'li')

            # Собираем все данные из <li>
            for li in job_info_list:
                value = li.text.strip().replace("\n", " ")
                job_info_set.add(value)  # Добавляем только уникальные значения

            # Сохраняем все данные
            results.append({
                "title": title,
                "link": link,
                "date_posted": date_posted,
                "job_info": job_info_set  # Множество с уникальными значениями
            })

            # Выводим информацию о заказе
            print(
                f"Название: {title}\nСсылка: {link}\nДата публикации: {date_posted}\nИнформация о работе: {job_info_set}{'-' * 40}")
    else:
        print(
            f"Ошибка: Количество ссылок ({len(names)}), дат ({len(date_elements)}) и информации о работе ({len(job_info_elements)}) не совпадает!")

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



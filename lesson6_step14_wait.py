# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго
# заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет
# забронировать кто-то другой.
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить математическую задачу и отправить решение


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # указываем Selenium проверять в течение n секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print(price)

    # Объявляем кнопку
    button = browser.find_element(By.ID, "book")
    button.click()

    # Ваш код, который заполняет обязательные поля и Скроллим к полю ответа

    input_answer = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", input_answer)

    # Ваш код, в котором функция рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Добавляется этот код
    # в начало скрипта:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_answer.send_keys(y)

    # Кликаем на кнопку Submit, чтобы отправить ответ
    button_1 = browser.find_element(By.ID, "solve")
    button_1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

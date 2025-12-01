# Задание: принимаем alert
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
# 2. Нажать на кнопку
# 3. Принять confirm
# 4. На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ваш код, в котором функция рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Добавляется этот код
# в начало скрипта:


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который выполняет поиск элемента:
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    # Ваш код, который переключается на окно с alert, а затем принимает его:
    browser.switch_to.alert.accept()
    time.sleep(3)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # Ваш код, который заполняет обязательные поля
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    # Кликаем на кнопку Submit, чтобы отправить ответ
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

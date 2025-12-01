# Задание: поиск сокровища с помощью get_attribute - lesson6_step12.py
# В данной задаче вам нужно с помощью роботов решить математическую задачу.
# Значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex
# у картинки с изображением сундука.
# Ваша программа должна:

# 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
# 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
# 5. Ввести ответ в текстовое поле.
# 6. Отметить checkbox "I'm the robot".
# 7. Выбрать radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ваш код, в котором функция рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Добавляется этот код
# в начало скрипта:


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
 # Ваш код, который заполняет обязательные поля
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    input_checkbox = browser.find_element(
        By.ID, "robotCheckbox").click()
    input_radiobutton = browser.find_element(
        By.ID, "robotsRule").click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
# Ваш код, который заполняет обязательные поля


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# Ваша программа должна выполнить следующие шаги:

# 1. Открыть страницу https://suninjuly.github.io/math.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x (код для этого приведён ниже).
# 4. Ввести ответ в текстовое поле.
# 5. Отметить checkbox "I'm the robot".
# 6. Выбрать radiobutton "Robots rule!".
# 7. Нажать на кнопку Submit.
# Необходимо использовать атрибут .text для найденного элемента.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ваш код, в котором функция рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Добавляется этот код
# в начало скрипта:


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
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

# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver
# на новую вкладку и решить в ней задачу.

# Сценарий для реализации выглядит так:

# 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
# 2. Нажать на кнопку
# 3. Переключиться на новую вкладку
# 4. Пройти капчу для робота и получить число-ответ


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ваш код, в котором функция рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Добавляется этот код
# в начало скрипта:


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который выполняет поиск элемента:
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    # Ваш код, чтобы узнать имя новой вкладки
    new_window = browser.window_handles[1]
    # Ваш код, чтобы запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
    # first_window = browser.window_handles[0]
    # Ваш код, который переключает на новую вкладку
    browser.switch_to.window(new_window)

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

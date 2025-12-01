# Задание: работа с выпадающим списком
# Напишите код, который реализует следующий сценарий:

# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

 # Ваш код, который ищет элементы
    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)

# Ваш код, в котором функция рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Добавляется этот код
# в начало скрипта:

    def sum_nums(x, y):
        return str(x + y)

    find_sum = sum_nums(x, y)
    print(find_sum)
    input_checkbox = browser.find_element(
        By.ID, "dropdown").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(find_sum)


# Отправляем заполненную форму, клик на кнопку Submit
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
# Ваш код, который заполняет обязательные поля


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

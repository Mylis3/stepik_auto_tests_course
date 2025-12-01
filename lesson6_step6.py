# Задание: использование метода find_elements
# Необходимо заполнить форму (http://suninjuly.github.io/huge_form.html). Необходимо заполнить форму с 100 обязательными полями,
# ограничено время на ее заполнение.
# Используйте WebDriver, метод find_elements, нужные локатор и его значение. Введите полученный код в качестве ответа к этой задаче.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for element in elements:
        element.send_keys("many letters")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

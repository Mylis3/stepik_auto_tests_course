# Задание
# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

# 1. Добавьте в самый верх своего кода import math
# 2. Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
# 3. Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# 4. Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
# 5. Заполните скриптом форму.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, str(
        math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

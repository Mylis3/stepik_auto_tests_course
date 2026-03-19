# Задание: авторизация на сайте

# 1. Задача -  реализовать автотест со следующим набором действий:
# открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
# авторизоваться со своими логином и паролем
# дождаться того, что поп-апа с авторизацией больше нет

# 2. Задача — реализовать автотест со следующим сценарием действий:
# открыть страницу
# авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
# ввести правильный ответ (поле перед вводом должно быть пустым)
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
# Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def authorized_browser(browser):

    browser.get("https://stepik.org/lesson/236895/step/1?auth=login")

    login_button = browser.find_element(
        By.CSS_SELECTOR, "a.navbar__auth_login")
    browser.execute_script("arguments[0].click();", login_button)

    time.sleep(3)

    browser.find_element(By.ID, "id_login_email").send_keys(
        os.getenv("MY_LOGIN"))
    browser.find_element(By.ID, "id_login_password").send_keys(
        os.getenv("MY_PASS"))

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(5)

    return browser


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_send_answer(authorized_browser, link):

    browser = authorized_browser
    browser.get(link)

    time.sleep(3)

    # если задание уже решено
    try:
        again_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn"))
        )
        again_button.click()
    except:
        pass

    # вычисляем ответ максимально поздно
    answer = str(math.log(int(time.time()) + 2))

    textarea = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".string-quiz__textarea"))
    )

    textarea.clear()
    textarea.send_keys(answer)

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    submit_button.click()

    feedback = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".smart-hints__hint")
        )
    )

    assert feedback.text == "Correct!", feedback.text


if __name__ == "__main__":
    pytest.main()

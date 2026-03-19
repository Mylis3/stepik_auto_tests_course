# Задание: авторизация на сайте

# Ваша задача -- реализовать автотест со следующим набором действий:
# открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
# авторизоваться со своими логином и паролем
# дождаться того, что поп-апа с авторизацией больше нет

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
load_dotenv()

link = "https://stepik.org/lesson/236895/step/1?auth=login"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # browser.implicitly_wait(10)
    print("\nquit browser..")
    browser.quit()


def test_guest_should_see_login_link(browser):
    browser.implicitly_wait(20)
    browser.get(link)
    button = browser.find_element(
        By.CSS_SELECTOR, 'a[href="/catalog?auth=login"]')
    browser.execute_script("arguments[0].click();",  button)
# также: browser.find_element(By.LINK_TEXT, "Войти")
    # button.click()
    time.sleep(5)
    email_field = browser.find_element(By.ID, "id_login_email")
    email_field.send_keys(os.getenv("MY_LOGIN"))
    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys(os.getenv("MY_PASS"))
    time.sleep(5)
    button_submit = browser.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    time.sleep(5)
    button_submit.click()

    time.sleep(5)

    assert browser.find_element(By.CSS_SELECTOR, ".navbar__profile-img"), \
        "User icon is not displayed, login failed"

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page


def test_by_product():
    s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
    driver = webdriver.Chrome(service=s)

    print('START TEST')

    login = Login_page(driver)
    login.authorization()

    button_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    button_cart.click()
    print('Кликнули по иконке корзины')
    time.sleep(5)


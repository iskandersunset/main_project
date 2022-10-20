import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_by_product():
    s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
    driver = webdriver.Chrome(service=s)

    print('START TEST')

    login = Login_page(driver)
    login.authorization()

    # Выбираем товар и кликаем по корзине
    mp = Main_page(driver)
    mp.select_product()

    # Выбираем товар и кликаем по корзине
    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.client_information_confirm()

    time.sleep(2)

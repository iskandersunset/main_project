import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@pytest.mark.run(order=1)
def test_by_product_1(set_up):
    s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
    driver = webdriver.Chrome(service=s)

    print('START TEST 1')

    login = Login_page(driver)
    login.authorization()

    # Выбираем товар и кликаем по корзине
    mp = Main_page(driver)
    mp.select_products_1()

    # Жмем кнопку Checkout
    cp = Cart_page(driver)
    cp.product_confirmation()

    # Заполняем данные и жмем Continue
    cip = Client_information_page(driver)
    cip.input_information()

    # Жмем финиш
    p = Payment_page(driver)
    p.payment()

    s = Finish_page(driver)
    s.finish()

    print('FINISH TEST 1')
    time.sleep(2)


@pytest.mark.run(order=3)
def test_by_product_2(set_up):
    s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
    driver = webdriver.Chrome(service=s)

    print('START TEST 2')

    login = Login_page(driver)
    login.authorization()

    # Выбираем товар и кликаем по корзине
    mp = Main_page(driver)
    mp.select_products_2()

    # Жмем кнопку Checkout
    cp = Cart_page(driver)
    cp.product_confirmation()

    print('FINISH TEST 2')
    time.sleep(2)


@pytest.mark.run(order=2)
def test_by_product_3(set_up):
    s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
    driver = webdriver.Chrome(service=s)

    print('START TEST 3')

    login = Login_page(driver)
    login.authorization()

    # Выбираем товар и кликаем по корзине
    mp = Main_page(driver)
    mp.select_products_3()

    # Жмем кнопку Checkout
    cp = Cart_page(driver)
    cp.product_confirmation()

    print('FINISH TEST 3')
    time.sleep(2)

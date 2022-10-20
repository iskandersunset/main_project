import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    time.sleep(2)

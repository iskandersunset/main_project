import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    user_name = "user-name"
    password = "password"

    def authorization(self, login_name, login_password):
        # 1. Авторизация на сайте
        user_name = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.ID, "user-name")))
        user_name.send_keys(login_name)
        print("Ввели логин")
        time.sleep(1)

        user_pass = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.ID, "password")))
        user_pass.send_keys(login_password)
        print("Ввели пароль")
        time.sleep(1)

        login_button = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        print('Клик по кнопке логин\n', '--' * 20)



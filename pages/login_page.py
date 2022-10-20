from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators============================

    user_name = "user-name"
    user_pass = "password"
    login_button = "login-button"
    main_word = "title"

    # Getters=============================

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.user_name)))

    def get_user_pass(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.user_pass)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.main_word)))

    # Actions =============================

    def init_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user_name", user_name)

    def init_user_pass(self, user_pass):
        self.get_user_pass().send_keys(user_pass)
        print("Input user_pass", user_pass)

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods =============================
    def authorization(self):
        self.driver.get(self.base_url)
        self.get_current_rl()
        self.init_user_name("standard_user")
        self.init_user_pass("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'PRODUCTS')


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators============================

    first_name = "first-name"
    last_name = "last-name"
    postal_code = "postal-code"
    continue_button = "continue"

    # Getters=============================

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.continue_button)))

    # Actions =============================

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name: ", first_name)

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name: ", last_name)

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input Postal Code: ", postal_code)

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue Button")

    # Methods =============================
    def client_information_confirm(self):
        self.get_current_url()
        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_postal_code("454000")
        self.click_continue_button()



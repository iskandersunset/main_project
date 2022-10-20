class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current URL"""

    def get_current_rl(self):
        get_url = self.driver.current_url
        print("Curent URL " + get_url)

    """Method Get current URL"""


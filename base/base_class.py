class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Curent URL " + get_url)

    """Method Assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value WORD")

from unit.test.BaseTest import BaseTest


class BasePage:
    def __init__(self):
        self.wait = BaseTest.get_wait()
        self.driver = BaseTest.get_driver()

    def scrollToElement(self, web_element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", web_element)
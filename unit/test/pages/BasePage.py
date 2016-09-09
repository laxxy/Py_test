from unit.test.BaseTest import BaseTest


class BasePage:
    def __init__(self):
        self.wait = BaseTest.get_wait()
        self.driver = BaseTest.get_driver()

    def doSmth(self):
        z = None

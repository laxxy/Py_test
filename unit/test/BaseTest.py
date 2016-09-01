import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class BaseTest(unittest.TestCase):
    wait = None
    driver_var = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        BaseTest.driver_var = cls.driver
        BaseTest.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        BaseTest.driver_var.quit()

    @staticmethod
    def get_driver():
        return BaseTest.driver_var


if __name__ == "__main__":
    unittest.main()

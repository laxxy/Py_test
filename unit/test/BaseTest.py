import unittest

import allure
from allure.constants import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class BaseTest(unittest.TestCase):
    wait = None
    driver_var = None
    currentResult = unittest.TestResult()

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Firefox()
        BaseTest.wait = WebDriverWait(driver, 10)
        BaseTest.driver_var = driver

    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                allure.attach('scr', BaseTest.driver_var.get_screenshot_as_png(), type=AttachmentType.PNG)

    @classmethod
    def tearDownClass(cls):
        BaseTest.driver_var.quit()

    @staticmethod
    def get_driver():
        return BaseTest.driver_var

    @staticmethod
    def get_wait():
        return BaseTest.wait


if __name__ == "__main__":
    unittest.main()

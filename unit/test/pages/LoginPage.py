from unit.test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import allure


class LoginPage:
    def __init__(self):
        self.driver = BaseTest.BaseTest.get_driver()
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("1")
    def step_1(self):
        until = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.sign-in')))
        until.click()
        until = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#sign-up']")))
        until.click()

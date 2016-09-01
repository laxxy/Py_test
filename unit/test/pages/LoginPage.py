from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from unit.test.BaseTest import BaseTest
import allure


class LoginPage:

    def __init__(self):
        self.wait = BaseTest.wait
        self.driver = BaseTest.driver_var

    @allure.step("1")
    def step_1(self):
        self.driver.get("http://ucraft.com")
        until = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.sign-in')))
        until.click()
        until = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#sign-up']")))
        until.click()

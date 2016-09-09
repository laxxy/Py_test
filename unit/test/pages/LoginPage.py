from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from unit.test.BaseTest import BaseTest
from unit.test.pages.BasePage import BasePage
import allure


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.wait = BaseTest.get_wait()
        self.driver = BaseTest.get_driver()

    @allure.step("1")
    def step_1(self):
        self.driver.get("http://ucraft.com")
        until = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.sign-in')))
        until.click()
        until = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#sign-up']")))
        until.click()

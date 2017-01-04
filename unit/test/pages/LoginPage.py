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
        self.driver.get("http://ts5.travian.ru/login.php")
        until = self.wait.until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, '.accountNameOrEmailAddress~td input')))
        until.send_keys("laxx")
        selector = self.driver.find_element_by_css_selector('.pass td input')
        selector.send_keys("19765328")
        css_selector = self.driver.find_element_by_css_selector('.button-content')
        css_selector.click()

    @allure.step("2")
    def step_test(self):
        self.driver.get("http://ucraft.com")
        element = self.driver.find_element_by_xpath("//a[text()='All']")
        super().scrollToElement(element)

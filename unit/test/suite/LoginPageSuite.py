import unittest

from unit.test import BaseTest
from unit.test.pages import LoginPage


class LoginPageSuite(BaseTest.BaseTest):

    driver = BaseTest.BaseTest.driver_var

    ''''@staticmethod
    def test3():
        LoginPageSuite.driver.get("http://google.com")'''

    @staticmethod
    def test_4():
        main_page = LoginPage.LoginPage()
        main_page.step_1()


if __name__ == '__main__':
    unittest.main(verbosity=2)

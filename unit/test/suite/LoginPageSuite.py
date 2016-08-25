import unittest
from unit.test import BaseTest
from unit.test.pages import LoginPage


class LoginPageSuite(BaseTest.BaseTest):

    driver = None

    @staticmethod
    def runTest():
        main_page = LoginPage.LoginPage()

    @staticmethod
    def test2():
        main_page = LoginPage.LoginPage()
        main_page.step_1()

    @staticmethod
    def test3():
        LoginPageSuite.driver.get("http://google.com")


if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest

from unit.test import BaseTest
from unit.test.pages import LoginPage

Assert = BaseTest.BaseTest


class LoginPageSuite(BaseTest.BaseTest):
    def test_4(self):
        main_page = LoginPage.LoginPage()
        main_page.step_test()

    # def test_5(self):
    #     main_page = LoginPage.LoginPage()
    #     main_page.step_1()
    #     Assert.assertEqual(self, 1, 2, "NO >>>>>>>>>>>>>>>>>>>>>>>")


if __name__ == "__main__":
    unittest.main()

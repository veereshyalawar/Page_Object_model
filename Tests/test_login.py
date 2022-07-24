import time
from unittest import TestCase

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from Page.loginpage import LoginPage
from Page.homepage import homepage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        serv_obj = Service("C:\\Users\\veeresh\\page_object_model\\Driver\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")

        login = LoginPage(driver)
        login.enter_username("8867743684")
        login.enter_passsward("9535405145")
        login.click_login()

        home_page = homepage(driver)
        home_page.click_on_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test successfully done")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\veeresh\\Page_object_module\\Reports"))
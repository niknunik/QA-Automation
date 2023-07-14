import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from home.homepage import MainPage
from login.loginpage import LoginPage


class Landing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()

    def clickAppointment(self):
        menu_page = MainPage(self.driver)
        menu_page.click_sidebar()
        time.sleep(3)
        menu_page.click_sidebar_login()
        time.sleep(3)

        login_page = LoginPage(self.driver)
        login_page.txtPassword = "ThisIsNotAPassword"
        time.sleep(2)
        login_page.click_bt_login()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

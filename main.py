import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Picasso Landing #


class Landing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

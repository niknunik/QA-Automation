from os import PRIO_PROCESS, sendfile
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class LandingPageLocators(object):
    BT_LOGIN = (
        By.XPATH, '/html/body/div/div/div/div[1]/nav/div/div/div[2]/div/a[1]/button')

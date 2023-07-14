from os import PRIO_PROCESS, sendfile
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class LandingPageLocators(object):

    BT_LOGIN = (
        By.XPATH, '/html/body/div/div/div/div[1]/nav/div/div/div[2]/div/a[1]/button')
    BT_MAKE_APPOINTMENT = (By.XPATH, '/html/body/header/div/a')
    BT_HREF_EMAIL = (By.XPATH, '/html/body/footer/div/div/div/ul[1]/li[2]/a')
    BT_FACEBOOK = (By.XPATH, '/html/body/footer/div/div/div/ul[2]/li[1]/a/i')
    BT_TWITTER = (By.XPATH, '/html/body/footer/div/div/div/ul[2]/li[2]/a/i')
    BT_DRIBBLE = (By.XPATH, '/html/body/footer/div/div/div/ul[2]/li[3]/a/i')
    BT_SIDEBAR = (By.XPATH, '/html/body/a/i')

from page import BasePage
from locators import LandingPageLocators
from element import BasePageElementXPath


class MainPage(BasePage):

    def click_lb_appointment(self):
        element = self.driver.find_element(
            *LandingPageLocators.BT_MAKE_APPOINTMENT)
        element.click()

    def click_href_email(self):
        element = self.driver.find_element(*LandingPageLocators.BT_HREF_EMAIL)
        element.click()

    def click_href_fb(self):
        element = self.driver.find_element(*LandingPageLocators.BT_FACEBOOK)
        element.click()

    def click_href_twitter(self):
        element = self.driver.find_element(*LandingPageLocators.BT_TWITTER)
        element.click()

    def click_href_dribble(self):
        element = self.driver.find_element(*LandingPageLocators.BT_DRIBBLE)
        element.click()

    def click_sidebar(self):
        element = self.driver.find_element(*LandingPageLocators.BT_SIDEBAR)
        element.click()

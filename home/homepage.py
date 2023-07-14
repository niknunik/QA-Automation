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

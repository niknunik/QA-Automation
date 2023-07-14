from page import BasePage
from locators import LandingPageLocators
from element import BasePageElementXPath


class MainPage(BasePage):

    def click_lb_appointment(self):
        element = self.driver.find_element(*LandingPageLocators.LB_MENU)
        element.click()

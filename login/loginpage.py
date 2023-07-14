from page import BasePage
from locators import LandingPageLocators, Stringpath
from element import BasePageElementID


class Username(BasePageElementID):
    locator = Stringpath.USERNAME


class Password(BasePageElementID):
    locator = Stringpath.PASSWORD


class LoginPage(BasePage):
    txtUsername = Username()
    txtPassword = Password()

    def input_value(self):
        eUsernmae = self.driver.find_element(*LoginPage.txtUsername)
        ePassword = self.driver.find_element(*LoginPage.txtPassword)

    def click_bt_login(self):
        element = self.driver.find_element(
            *LoginPage.BT_LOGIN)
        element.click()

    def click_bt_to_top(self):
        element = self.driver.find_element(
            *LoginPage.click_bt_to_top)
        element.click()

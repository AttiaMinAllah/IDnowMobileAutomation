from selenium.webdriver.common.by import By
from common.base_page import BasePage

class QuitSessionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.reason_option_1 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I don’t have my document with me")')
        self.reason_option_2 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I have privacy concerns")')
        self.reason_option_3 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("The app is not responding and I cannot go further")')
        self.reason_option_4 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Not interested in the service for which this identification is required")')
        self.reason_option_5 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I will complete the identification later")')
        self.quit_button = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Quit session")')
        self.intermediate_screen = (By.ID, 'checkScreenDocumentHeader')
        self.home_screen_logo = (By.ID, 'homescreen_idnow_logo')

    def select_reason_and_quit(self, reason):
        # select reason and quit session.'
        reason_map = {
            'option_1': self.reason_option_1,
            'option_2': self.reason_option_2,
            'option_3': self.reason_option_3,
            'option_4': self.reason_option_4,
            'option_5': self.reason_option_5,
        }
        self.wait_for_element(*reason_map[reason]).click()
        self.driver.find_element(*self.quit_button).click()

    def are_reasons_displayed(self):
        return all([
            self.is_displayed(*self.reason_option_1),
            self.is_displayed(*self.reason_option_2),
            self.is_displayed(*self.reason_option_3),
            self.is_displayed(*self.reason_option_4),
            self.is_displayed(*self.reason_option_5),
        ])

    def is_intermediate_screen_displayed(self):
        return self.is_displayed(*self.intermediate_screen)

    def is_home_screen_logo_displayed(self):
        return self.is_displayed(*self.home_screen_logo)

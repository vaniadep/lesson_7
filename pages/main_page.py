from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.second_frame import SecondFrame


class MainPage(BasePage):

    ALL_IFRAMES = (By.TAG_NAME, "iframe")
    SECOND_IFRAME = (By.XPATH, "(//iframe)[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.second_frame = SecondFrame(driver)

    def switch_to_second_iframe(self):
        self.switch_to_frame(self.SECOND_IFRAME)
        return self.second_frame

    def leave_iframe(self):
        self.switch_to_default_content()

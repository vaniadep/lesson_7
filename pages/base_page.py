from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def switch_to_frame(self, frame_locator_or_element):
        return self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator_or_element))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def wait_for_success_purchase_message(self, locator):

        element = self.wait_for_element_visible(locator)
        return element.text

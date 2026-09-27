from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecondFrame(BasePage):

    DOWNLOADS_NAV = (By.XPATH, "//nav//a[contains(@href, '/downloads') or contains(text(), 'Downloads')]")
    PYTHON_STABLE_LINK = (
        By.XPATH,
        "//p[contains(., 'Python')]/following-sibling::p//a[contains(@href, 'pypi.org')] | "
        "//div[contains(@class, 'card')]//p[contains(text(), 'Python')]/..//a[contains(@href, 'pypi')] | "
        "//a[contains(@href, 'pypi.org/project/selenium')]"
    )

    def go_to_downloads(self):
        if len(self.driver.find_elements(*self.DOWNLOADS_NAV)) > 0:
            link = self.wait_for_element_clickable(self.DOWNLOADS_NAV)
            link.click()

    def get_python_stable_download_url(self) -> str:
        element = self.wait_for_element_presence(self.PYTHON_STABLE_LINK)
        return element.get_attribute("href")

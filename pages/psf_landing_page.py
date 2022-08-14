from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class PsfLandingPage(BasePage):

    @property
    def about_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/about/"]')


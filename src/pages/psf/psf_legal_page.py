from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage


class PsfLegalPage(BasePage):

    @property
    def legal_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1[@class="page-title"]')

    @property
    def psf_link(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf"]')



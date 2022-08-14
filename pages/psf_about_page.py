from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class PsfAboutPage(BasePage):

    @property
    def about_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1[@class="page-title"]')



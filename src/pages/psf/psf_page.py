from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage


class PsfPage(BasePage):

    @property
    def psf_widget_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h3[@class="widget-title"]')

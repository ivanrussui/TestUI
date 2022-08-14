from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class TutorialPage(BasePage):

    @property
    def docs_tutorial_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1')


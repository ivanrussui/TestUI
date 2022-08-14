from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class DonatePage(BasePage):

    @property
    def donation_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//h1[@class='entry-title']")

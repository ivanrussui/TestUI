from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage


class CommunityLandingPage(BasePage):

    @property
    def community_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1[@class="page-title"]')

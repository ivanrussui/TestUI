from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class DocsPage(BasePage):

    @property
    def docs_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1')

    @property
    def docs_tutorial(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="tutorial/index.html"]')

    @property
    def docs_input_search(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[2]/ul/li[9]/div/form/input[1]')

    @property
    def docs_search_go(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[2]/ul/li[9]/div/form/input[2]')

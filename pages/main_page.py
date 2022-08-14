from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def donate_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//a[@class='donate-button']")

    @property
    def search_input(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[@id='id-search-field']")

    @property
    def start_search(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@id='submit']")

    @property
    def search_result(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[@name='q'][@type='text']")

    # my decoration
    @property
    def psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@title="The Python Software Foundation"]')

    @property
    def docs_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@title="Python Documentation"]')

    @property
    def docs_nav_bottom(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//li[@id="documentation"]/a[@href="/doc/"]' or '//*[@id="documentation"]/a')

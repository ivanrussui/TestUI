import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from src.pages.base_page import BasePage


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

    @property
    def psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@title="The Python Software Foundation"]')

    @property
    def docs_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@title="Python Documentation"]')

    @property
    def docs_nav_bottom(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//li[@id="documentation"]/a[@href="/doc/"]' or '//*[@id="documentation"]/a')

    @property
    def community_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/community-landing/"]')

    def documentation_drop_menu_item(self, text) -> WebElement:
        return self.driver.find_element(By.XPATH,
                                        f"//*[@id='documentation']//*[@class='subnav menu']//*[text()='{text}']")

    @allure.step('Наводимся на Documentation подраздел')
    def open_docs_drop_bar(self):
        ActionChains(self.driver).move_to_element(self.docs_nav_bottom).perform()

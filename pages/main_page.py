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
    def about_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/about/"]')

    @property
    def about_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1[@class="page-title"]')

    @property
    def docs_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@title="Python Documentation"]')

    @property
    def docs_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1')

    @property
    def docs_tutorial(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="tutorial/index.html"]')

    @property
    def docs_tutorial_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1')

    @property
    def docs_nav_btn(self) -> WebElement:
        return self.driver.find_element(By.XPATH,
                                        '//li[@id="documentation"]/a[@href="/doc/"]' or '//*[@id="documentation"]/a')

    @property
    def python_docs_btn(self) -> WebElement:
        return self.driver.find_element(By.XPATH,
                                        '//div[@class="documentation-banner"]/p/a[@href="http://docs.python.org/3/"]')

    @property
    def docs_input_search(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[2]/ul/li[9]/div/form/input[1]')

    @property
    def docs_search_go(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[2]/ul/li[9]/div/form/input[2]')

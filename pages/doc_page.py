from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class DocPage(BasePage):

    @property
    def python_docs_btn(self) -> WebElement:
        return self.driver.find_element(By.XPATH,
                                        '//div[@class="documentation-banner"]/p/a[@href="http://docs.python.org/3/"]')



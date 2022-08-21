from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage


class PsfVendorInfoPage(BasePage):

    @property
    def vendor_info_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1[@class="page-title"]')

    @property
    def vendor_policies_link(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="https://www.python.org/psf/vendorpolicies"]')



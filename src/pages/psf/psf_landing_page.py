import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from src.pages.base_page import BasePage


class PsfLandingPage(BasePage):

    @property
    def about_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/about/"]')

    @property
    def vendor_info_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/accounts-payable"]')

    @property
    def legal_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/about/legal/"]')

    @property
    def grants_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/grants/"]')

    def grants_drop_menu_item(self, text) -> WebElement:
        return self.driver.find_element(By.XPATH, f"//*[@id='grants']//*[text()='{text}']")

    @allure.step('Наводимся на Grants подраздел')
    def open_grants_drop_bar(self):
        ActionChains(self.driver).move_to_element(self.grants_psf_nav).perform()



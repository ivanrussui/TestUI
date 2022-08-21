import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from src.steps import Steps

@pytest.mark.usefixtures("init_test_suite")
class BasicTest:
    steps_inst: Steps
    driver_inst: WebDriver

    @property
    def steps(self) -> Steps:         # метод steps возвращает объект класса Steps
        return self.steps_inst         # возвращаем экземпляр класса Steps

    @property
    def driver(self) -> WebDriver:
        return self.driver_inst
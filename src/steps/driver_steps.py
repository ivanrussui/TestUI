import os.path

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverSteps:

    @property
    def driver_path(self):
        return "C:/IT/koleso/autotests/TestUI/lib/chromedriver" # для запуска теста с командной строки, команда pytest ./tests
        # root_dir = os.path.dirname(os.path.abspath("."))
        # path = f"{root_dir}/lib/chromedriver.exe"
        # print(path)
        # return path

    def create_driver_and_open_python_page(self) -> WebDriver:
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("https://www.python.org/")
        return driver

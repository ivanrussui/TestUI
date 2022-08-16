import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.steps import Steps


@pytest.fixture
def steps() -> Steps:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('headless')  # мож закоментить а то один тест фейлется

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    driver.get("http://www.python.org")

    steps_obj = Steps(driver)

    yield steps_obj

    driver.quit()



import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.steps import Steps


@pytest.fixture(scope="function")
def init_test_suite(request) -> Steps:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument('headless')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    steps_obj = Steps(driver)

    driver.get("http://www.python.org")

    request.cls.driver_inst = driver
    request.cls.steps_inst = steps_obj

    yield steps_obj

    driver.quit()

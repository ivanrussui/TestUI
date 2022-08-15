import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def steps() -> None:

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(
            path="/IT/koleso/autotests/TestUI"
        ).install()),
        # options=None,
    )

    driver.get("https://www.python.org/")

    yield

    driver.quit()



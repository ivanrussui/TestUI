from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class MainPage:

    @property
    def donate_btn(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//a[@class='donate-button']")

    @property
    def donate_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//h1[@class='entry-title']")

    @property
    def search_input(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[@id='id-search-field']")

    @property
    def search_go(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@id='submit']")

    @property
    def search_result(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[@name='q'][@type='text']")

    # my
    @property
    def psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@title="The Python Software Foundation"]')

    @property
    def about_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/about/"]')

    @property
    def about_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//h1[@class="page-title"]')

    # 2 test
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

    # ost
    @property
    def docs_nav_bottom(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//li[@id="documentation"]/a[@href="/doc/"]' or '//*[@id="documentation"]/a')

    @property
    def python_docs_btn(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[@class="documentation-banner"]/p/a[@href="http://docs.python.org/3/"]')

    @property
    def docs_input_search(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[2]/ul/li[9]/div/form/input[1]')

    @property
    def docs_search_go(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[2]/ul/li[9]/div/form/input[2]')




def open_python_page() -> WebDriver:
    driver = webdriver.Chrome(executable_path='lib/chromedriver.exe')
    driver.get('https://www.python.org/')
    return driver

def test_donation_btn():
    driver = open_python_page()
    main_page = MainPage(driver)
    assert main_page.donate_btn.text == 'Donate', 'Text fail'
    main_page.donate_btn.click()
    assert main_page.donate_title.is_displayed(), "Title fail"
    assert main_page.donate_title.text == 'Donation for the PSF', 'Donation title text is not valid'


def test_search_input():
    driver = open_python_page()
    main_page = MainPage(driver)
    input_text = 'Hello World!'
    assert main_page.search_input.is_displayed()
    main_page.search_input.clear()
    main_page.search_input.send_keys(input_text)
    assert main_page.search_input.get_property('value') == input_text
    main_page.search_go.click()
    assert main_page.search_result.get_property('value') == input_text

# my_tests этот тест переписал
def test_psf_nav():
    driver = open_python_page()
    main_page = MainPage(driver)
    assert main_page.psf_nav.text == 'PSF', 'Text is not correct'
    main_page.psf_nav.click()
    assert main_page.about_psf_nav.text == 'About', 'Text is not correct'
    main_page.about_psf_nav.click()
    assert main_page.about_title.is_displayed(), 'No title'
    assert main_page.about_title.text == 'About the Python Software Foundation', 'Text is not correct'
    pass

def test_dosc_nav():
    driver = open_python_page()
    main_page = MainPage(driver)
    assert main_page.docs_nav.text == 'Docs', 'Text is not correct'
    main_page.docs_nav.click()
    assert main_page.docs_title.is_displayed(), 'No title'
    assert main_page.docs_title.text == 'Python 3.10.6 documentation', 'Text is not correct'
    assert main_page.docs_tutorial.is_displayed(), 'No text'
    assert main_page.docs_tutorial.text == 'Tutorial', 'Text is not correct'
    main_page.docs_tutorial.click()
    # ost
    assert main_page.docs_tutorial_title.is_displayed(), 'No text'
    assert main_page.docs_tutorial_title.text == 'The Python Tutorial', 'Text is not correct'
    pass

def test_docs_search_input():
    driver = open_python_page()
    main_page = MainPage(driver)
    assert main_page.docs_nav_bottom.text == 'Documentation', 'Text is not correct'
    main_page.docs_nav_bottom.click()
    assert main_page.python_docs_btn.is_displayed(), 'No button'
    assert main_page.python_docs_btn.text == 'Python Docs', 'Text is not correct'
    main_page.python_docs_btn.click()
    input_text = 'Python/C API'
    assert main_page.docs_input_search.is_displayed()
    main_page.docs_input_search.clear()
    main_page.docs_input_search.send_keys(input_text)
    main_page.docs_input_search.get_property('value') == input_text
    main_page.docs_input_search.click()
    main_page.search_result.get_property('value') == input_text
    pass


if __name__ == '__main__':
    test_donation_btn()

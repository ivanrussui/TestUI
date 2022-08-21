import allure

from src.pages.main_page import MainPage
from src.steps.base_steps import BaseSteps


class MainPageSteps(BaseSteps):

    @property
    def main_page(self) -> MainPage:
        return MainPage(self.driver)

    def search(self, search_text):
        assert self.main_page.search_input.is_displayed(), "Поле Search не на экране"
        self.main_page.search_input.clear()
        self.main_page.search_input.send_keys(search_text)
        assert self.main_page.search_input.get_property("value") == search_text, "Описание ошибки"
        self.main_page.start_search.click()

    def open_donate_page(self):
        assert self.main_page.donate_button.text == "Donate", "Donation button text is not Donate"
        self.main_page.donate_button.click()

    def check_search_result(self, search_text):
        assert self.main_page.search_result.get_property('value') == search_text, "Описание ошибки"

    def psf_landing_open(self):
        assert self.main_page.psf_nav.text == 'PSF', 'Text is not correct'
        self.main_page.psf_nav.click()

    def docs_open(self):
        assert self.main_page.docs_nav.text == 'Docs', 'Text is not correct'
        self.main_page.docs_nav.click()

    def docs_nav_bottom(self):
        assert self.main_page.docs_nav_bottom.text == 'Documentation', 'Text is not correct'
        self.main_page.docs_nav_bottom.click()

    def community_landing_open(self):
        assert self.main_page.community_nav.text == 'Community', 'Text is not correct'
        self.main_page.community_nav.click()

    @allure.step('Открываем Documentation -> FAQ раздел')
    def open_news_drop_bar_item(self, item: str):
        self.main_page.open_docs_drop_bar()
        assert self.main_page.documentation_drop_menu_item(item).is_displayed()
        self.main_page.documentation_drop_menu_item(item).click()


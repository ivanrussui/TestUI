from src.pages.docs_page import DocsPage
from src.steps.base_steps import BaseSteps


class DocsPageSteps(BaseSteps):

    @property
    def docs_page(self) -> DocsPage:
        return DocsPage(self.driver)

    def check_docs_page_is_open(self):
        assert self.docs_page.docs_title.is_displayed(), 'No title'
        assert self.docs_page.docs_title.text == 'Python 3.10.6 documentation', 'Text is not correct'

    def check_tutorial(self):
        assert self.docs_page.docs_tutorial.is_displayed(), 'No text'
        assert self.docs_page.docs_tutorial.text == 'Tutorial', 'Text is not correct'
        self.docs_page.docs_tutorial.click()
        pass

    def docs_search(self, search_text):
        assert self.docs_page.docs_input_search.is_displayed(), "Поле Search не на экране"
        self.docs_page.docs_input_search.clear()
        self.docs_page.docs_input_search.send_keys(search_text)
        assert self.docs_page.docs_input_search.get_property('value') == search_text, "Описание ошибки"
        self.docs_page.docs_search_go.click()


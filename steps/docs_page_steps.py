from pages.docs_page import DocsPage
from steps.base_steps import BaseSteps


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

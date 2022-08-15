from src.pages.doc_page import DocPage
from src.steps.base_steps import BaseSteps


class DocPageSteps(BaseSteps):

    @property
    def doc_page(self) -> DocPage:
        return DocPage(self.driver)

    def docs_page_open(self):
        assert self.doc_page.python_docs_btn.is_displayed(), 'No button'
        assert self.doc_page.python_docs_btn.text == 'Python Docs', 'Text is not correct'
        self.doc_page.python_docs_btn.click()


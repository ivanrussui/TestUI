from pages.docs_page import DocsPage
from pages.tutorial_page import TutorialPage
from steps.base_steps import BaseSteps


class TutorialPageSteps(BaseSteps):

    @property
    def tutorial_page(self) -> TutorialPage:
        return TutorialPage(self.driver)

    def check_tutorial_page_is_open(self):
        assert self.tutorial_page.docs_tutorial_title.is_displayed(), 'No text'
        assert self.tutorial_page.docs_tutorial_title.text == 'The Python Tutorial', 'Text is not correct'
        pass

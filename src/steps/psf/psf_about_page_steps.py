from src.pages.psf.psf_about_page import PsfAboutPage
from src.steps.base_steps import BaseSteps


class PsfAboutPageSteps(BaseSteps):
    @property
    def psf_about_page(self) -> PsfAboutPage:
        return PsfAboutPage(self.driver)

    def check_psf_about_page_is_open(self):
        assert self.psf_about_page.about_title.is_displayed(), 'No title'
        assert self.psf_about_page.about_title.text == 'About the Python Software Foundation', 'Text is not correct'
        pass


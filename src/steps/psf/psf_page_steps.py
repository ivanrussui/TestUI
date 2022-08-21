from src.pages.psf.psf_page import PsfPage
from src.steps.base_steps import BaseSteps


class PsfPageSteps(BaseSteps):
    @property
    def psf_page(self) -> PsfPage:
        return PsfPage(self.driver)

    def check_psf_page_is_open(self):
        assert self.psf_page.psf_widget_title.is_displayed(), 'No title'
        assert self.psf_page.psf_widget_title.text == 'The PSF', 'Text is not correct'


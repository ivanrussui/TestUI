from src.pages.psf.psf_grants_page import PsfGrantsPage
from src.steps.base_steps import BaseSteps


class PsfGrantsPageSteps(BaseSteps):
    @property
    def psf_grants_page(self) -> PsfGrantsPage:
        return PsfGrantsPage(self.driver)

    def check_psf_grants_page_is_open(self):
        assert self.psf_grants_page.grants_title.is_displayed(), 'No title'
        assert self.psf_grants_page.grants_title.text == 'PSF Grants Program', 'Text is not correct'


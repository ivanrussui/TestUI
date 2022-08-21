from src.pages.psf.psf_legal_page import PsfLegalPage
from src.steps.base_steps import BaseSteps


class PsfLegalPageSteps(BaseSteps):
    @property
    def psf_legal_page(self) -> PsfLegalPage:
        return PsfLegalPage(self.driver)

    def check_psf_legal_page_is_open(self):
        assert self.psf_legal_page.legal_title.is_displayed(), 'No title'
        assert self.psf_legal_page.legal_title.text == 'Legal Statements', 'Text is not correct'
        self.psf_legal_page.legal_title.get_dom_attribute('Bylaws')

    def check_psf(self):
        assert self.psf_legal_page.psf_link.is_displayed(), 'No link'
        assert self.psf_legal_page.psf_link.text == 'Python Software Foundation', 'Link is not correct'
        self.psf_legal_page.psf_link.click()


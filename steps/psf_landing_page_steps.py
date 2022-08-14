from pages.psf_landing_page import PsfLandingPage
from steps.base_steps import BaseSteps


class PsfLandingPageSteps(BaseSteps):
    @property
    def psf_landing_page(self) -> PsfLandingPage:
        return PsfLandingPage(self.driver)

    def psf_about_open(self):
        assert self.psf_landing_page.about_psf_nav.text == 'About', 'Text is not correct'
        self.psf_landing_page.about_psf_nav.click()
        pass


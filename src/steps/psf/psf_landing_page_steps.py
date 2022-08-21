import allure

from src.pages.psf.psf_landing_page import PsfLandingPage
from src.steps.base_steps import BaseSteps


class PsfLandingPageSteps(BaseSteps):

    @property
    def psf_landing_page(self) -> PsfLandingPage:
        return PsfLandingPage(self.driver)

    def psf_about_open(self):
        assert self.psf_landing_page.about_psf_nav.text == 'About', 'Text is not correct'
        self.psf_landing_page.about_psf_nav.click()

    def psf_grants_open(self):
        assert self.psf_landing_page.grants_psf_nav.text == 'Grants', 'Text is not correct'
        self.psf_landing_page.grants_psf_nav.click()

    def psf_vendor_info_open(self):
        assert self.psf_landing_page.vendor_info_psf_nav.text == 'Vendor Info', 'Text is not correct'
        self.psf_landing_page.vendor_info_psf_nav.click()

    def psf_legal_open(self):
        assert self.psf_landing_page.legal_psf_nav.text == 'Legal', 'Text is not correct'
        self.psf_landing_page.legal_psf_nav.click()

    @allure.step('Открываем Grants -> Grants Program FAQ раздел')
    def open_grants_drop_bar_item(self, item: str):
        self.psf_landing_page.open_grants_drop_bar()
        assert self.psf_landing_page.grants_drop_menu_item(item).is_displayed(), 'No text'
        self.psf_landing_page.grants_drop_menu_item(item).click()

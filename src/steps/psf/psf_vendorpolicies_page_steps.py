from src.pages.psf.psf_vendorpolicies_page import PsfVendorpoliciesPage
from src.steps.base_steps import BaseSteps


class PsfVendorpoliciesPageSteps(BaseSteps):
    @property
    def psf_vendorpolicies_page(self) -> PsfVendorpoliciesPage:
        return PsfVendorpoliciesPage(self.driver)

    def check_psf_vendorpolicies_page_is_open(self):
        assert self.psf_vendorpolicies_page.vendorpolicies_title.is_displayed(), 'No title'
        assert self.psf_vendorpolicies_page.vendorpolicies_title.text == 'Python Software Foundation: Vendor Policies', 'Text is not correct'



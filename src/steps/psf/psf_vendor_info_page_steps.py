from src.pages.psf.psf_vendor_info_page import PsfVendorInfoPage
from src.steps.base_steps import BaseSteps


class PsfVendorInfoPageSteps(BaseSteps):
    @property
    def psf_vendor_info_page(self) -> PsfVendorInfoPage:
        return PsfVendorInfoPage(self.driver)

    def check_psf_vendor_info_page_is_open(self):
        assert self.psf_vendor_info_page.vendor_info_title.is_displayed(), 'No title'
        assert self.psf_vendor_info_page.vendor_info_title.text == 'Python Software Foundation: Accounts Payable', 'Text is not correct'

    def check_vendor_policies(self):
        assert self.psf_vendor_info_page.vendor_policies_link.is_displayed(), 'No link'
        assert self.psf_vendor_info_page.vendor_policies_link.text == 'VENDOR POLICIES', 'Link is not correct'
        self.psf_vendor_info_page.vendor_policies_link.click()


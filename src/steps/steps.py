from src.steps.community_landing_page_steps import CommunityLandingPageSteps
from src.steps.doc_page_steps import DocPageSteps
from src.steps.docs_page_steps import DocsPageSteps
from src.steps.donate_page_steps import DonatePageSteps
from src.steps.main_page_steps import MainPageSteps
from src.steps.tutorial_page_steps import TutorialPageSteps
from src.steps.psf.psf_about_page_steps import PsfAboutPageSteps
from src.steps.psf.psf_landing_page_steps import PsfLandingPageSteps
from src.steps.psf.psf_grants_page_steps import PsfGrantsPageSteps
from src.steps.psf.psf_vendor_info_page_steps import PsfVendorInfoPageSteps
from src.steps.psf.psf_vendorpolicies_page_steps import PsfVendorpoliciesPageSteps
from src.steps.psf.psf_legal_page_steps import PsfLegalPageSteps
from src.steps.psf.psf_page_steps import PsfPageSteps


class Steps:
    def __init__(self, driver):
        self.driver = driver

    @property
    def main_page(self) -> MainPageSteps:
        return MainPageSteps(driver=self.driver)

    @property
    def donate_page(self) -> DonatePageSteps:
        return DonatePageSteps(driver=self.driver)

    @property
    def psf_landing_page(self) -> PsfLandingPageSteps:
        return PsfLandingPageSteps(driver=self.driver)

    @property
    def psf_about_page(self) -> PsfAboutPageSteps:
        return PsfAboutPageSteps(self.driver)

    @property
    def docs_page(self) -> DocsPageSteps:
        return DocsPageSteps(self.driver)

    @property
    def tutorial_page(self) -> TutorialPageSteps:
        return TutorialPageSteps(self.driver)

    @property
    def doc_page(self) -> DocPageSteps:
        return DocPageSteps(self.driver)

    @property
    def community_landing_page(self) -> CommunityLandingPageSteps:
        return CommunityLandingPageSteps(driver=self.driver)

    @property
    def psf_grants_page(self) -> PsfGrantsPageSteps:
        return PsfGrantsPageSteps(self.driver)

    @property
    def psf_vendor_info_page(self) -> PsfVendorInfoPageSteps:
        return PsfVendorInfoPageSteps(self.driver)

    @property
    def psf_vendorpolicies_page(self) -> PsfVendorpoliciesPageSteps:
        return PsfVendorpoliciesPageSteps(self.driver)

    @property
    def psf_legal_page(self) -> PsfLegalPageSteps:
        return PsfLegalPageSteps(self.driver)

    @property
    def psf_page(self) -> PsfPageSteps:
        return PsfPageSteps(self.driver)


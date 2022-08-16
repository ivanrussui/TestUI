from src.steps.community_landing_page_steps import CommunityLandingPageSteps
from src.steps.doc_page_steps import DocPageSteps
from src.steps.docs_page_steps import DocsPageSteps
from src.steps.donate_page_steps import DonatePageSteps
from src.steps.main_page_steps import MainPageSteps
from src.steps.psf_about_page_steps import PsfAboutPageSteps
from src.steps.psf_landing_page_steps import PsfLandingPageSteps
from src.steps.tutorial_page_steps import TutorialPageSteps


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
        return PsfAboutPageSteps(self.driver)  # можно писать просто driver

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
        return CommunityLandingPageSteps(self.driver)

from steps.doc_page_steps import DocPageSteps
from steps.docs_page_steps import DocsPageSteps
from steps.donate_page_steps import DonatePageSteps
from steps.driver_steps import DriverSteps
from steps.main_page_steps import MainPageSteps
from steps.psf_about_page_steps import PsfAboutPageSteps
from steps.psf_landing_page_steps import PsfLandingPageSteps
from steps.tutorial_page_steps import TutorialPageSteps


def main_page(driver) -> MainPageSteps:
    return MainPageSteps(driver=driver)


def donate_page(driver) -> DonatePageSteps:
    return DonatePageSteps(driver=driver)


def psf_landing_page(driver) -> PsfLandingPageSteps:
    return PsfLandingPageSteps(driver=driver)


def psf_about_page(driver) -> PsfAboutPageSteps:
    return PsfAboutPageSteps(driver)   # можно писать просто driver


def docs_page(driver) -> DocsPageSteps:
    return DocsPageSteps(driver)


def tutorial_page(driver) -> TutorialPageSteps:
    return TutorialPageSteps(driver)


def doc_page(driver) -> DocPageSteps:
    return DocPageSteps(driver)


def driver_steps() -> DriverSteps:
    return DriverSteps()

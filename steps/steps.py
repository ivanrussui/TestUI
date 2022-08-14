from steps.donate_page_steps import DonatePageSteps
from steps.driver_steps import DriverSteps
from steps.main_page_steps import MainPageSteps
from steps.psf_about_page_steps import PsfAboutPageSteps
from steps.psf_landing_page_steps import PsfLandingPageSteps


def main_page(driver) -> MainPageSteps:
    return MainPageSteps(driver=driver)


def donate_page(driver) -> DonatePageSteps:
    return DonatePageSteps(driver=driver)


def psf_landing_page(driver) -> PsfLandingPageSteps:
    return PsfLandingPageSteps(driver=driver)


def psf_about_page(driver) -> PsfAboutPageSteps:
    return PsfAboutPageSteps(driver=driver)


def driver_steps() -> DriverSteps:
    return DriverSteps()

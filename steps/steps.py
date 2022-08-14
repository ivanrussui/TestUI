from steps.donate_page_steps import DonatePageSteps
from steps.driver_steps import DriverSteps
from steps.main_page_steps import MainPageSteps


def main_page(driver) -> MainPageSteps:
    return MainPageSteps(driver=driver)


def donate_page(driver) -> DonatePageSteps:
    return DonatePageSteps(driver=driver)


def driver_steps() -> DriverSteps:
    return DriverSteps()

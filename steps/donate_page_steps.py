from pages.donate_page import DonatePage
from steps.base_steps import BaseSteps


class DonatePageSteps(BaseSteps):
    @property
    def donate_page(self) -> DonatePage:
        return DonatePage(self.driver)

    def check_donate_page_is_open(self):
        assert self.donate_page.donation_title.is_displayed(), "Title fail"
        assert self.donate_page.donation_title.text == 'Donation for the PSF', 'Donation title text is not valid'
        pass


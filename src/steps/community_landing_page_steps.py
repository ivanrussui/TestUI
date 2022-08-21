import allure

from src.pages.community_landing_page import CommunityLandingPage
from src.steps.base_steps import BaseSteps


class CommunityLandingPageSteps(BaseSteps):
    @property
    def community_landing_page(self) -> CommunityLandingPage:
        return CommunityLandingPage(self.driver)

    @allure.step('Проеряем title Community')
    def check_community_landing_page_is_open(self):
        assert self.community_landing_page.community_title.is_displayed(), 'No title'
        assert self.community_landing_page.community_title.text == 'Community', 'Text is not correct'
        pass


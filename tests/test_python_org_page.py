import pytest
import allure

from .basic_test import BasicTest


@allure.suite("UI тесты")
@allure.sub_suite("Главная страница Python org")
class TestMainPage(BasicTest):

    def test_donation_button(self):
        self.steps.main_page.open_donate_page()
        self.steps.donate_page.check_donate_page_is_open()


    @pytest.mark.parametrize("search_text", ["hello", "bye", "world"])
    def test_search_input(self, search_text):
        self.steps.main_page.search(search_text=search_text)
        self.steps.main_page.check_search_result(search_text=search_text)


    def test_psf_nav(self):
        self.steps.main_page.psf_landing_open()
        self.steps.psf_landing_page.psf_about_open()
        self.steps.psf_about_page.check_psf_about_page_is_open()


    def test_docs_nav(self):
        self.steps.main_page.docs_open()
        self.steps.docs_page.check_docs_page_is_open()
        self.steps.docs_page.check_tutorial()
        self.steps.tutorial_page.check_tutorial_page_is_open()


    # todo этот тест падает headless моде
    # @pytest.mark.parametrize("search_text", ["Python/C API", "JavaScript", "Test"])
    # def test_docs_search_input(self, search_text):
    #     self.steps.main_page.docs_nav_bottom()
    #     self.steps.doc_page.docs_page_open()
    #     self.steps.docs_page.docs_search(search_text=search_text)
    #     self.steps.main_page.check_search_result(search_text=search_text)

    @allure.title('Проверка открытия Community-Landing')
    def test_community_nav(self):
        self.steps.main_page.community_landing_open()
        self.steps.community_landing_page.check_community_landing_page_is_open()


    def test_psf_vendorpolicies_link(self):
        self.steps.main_page.psf_landing_open()
        self.steps.psf_landing_page.psf_vendor_info_open()
        self.steps.psf_vendor_info_page.check_psf_vendor_info_page_is_open()
        self.steps.psf_vendor_info_page.check_vendor_policies()
        self.steps.psf_vendorpolicies_page.check_psf_vendorpolicies_page_is_open()


    def test_psf_link(self):
        self.steps.main_page.psf_landing_open()
        self.steps.psf_landing_page.psf_legal_open()
        self.steps.psf_legal_page.check_psf_legal_page_is_open()
        self.steps.psf_legal_page.check_psf()
        self.steps.psf_page.check_psf_page_is_open()


    def test_psf_grants(self):
        self.steps.main_page.psf_landing_open()
        self.steps.psf_landing_page.psf_grants_open()
        self.steps.psf_grants_page.check_psf_grants_page_is_open()


    @allure.title('Проверка нажатия на Grants Program FAQ кнопку')
    def test_psf_grants_program_faq(self):
        self.steps.main_page.psf_landing_open()
        self.steps.psf_landing_page.open_grants_drop_bar_item('Grants Program FAQ')


    @allure.title('Проверка нажатия на FAQ кнопку')
    def test_documentation_faq(self):
        self.steps.main_page.open_news_drop_bar_item("FAQ")


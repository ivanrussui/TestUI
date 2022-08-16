# noinspection PyUnresolvedReferences
import pytest

# noinspection PyUnresolvedReferences
from src.fixtures import steps


def test_donation_button(steps):
    steps.main_page.open_donate_page()
    steps.donate_page.check_donate_page_is_open()


def test_search_input(steps):
    search_text = 'hello'
    steps.main_page.search(search_text=search_text)
    steps.main_page.check_search_result(search_text)  # можно так search_text


def test_psf_nav(steps):
    steps.main_page.psf_landing_open()
    steps.psf_landing_page.psf_about_open()
    steps.psf_about_page.check_psf_about_page_is_open()


def test_docs_nav(steps):
    steps.main_page.docs_open()
    steps.docs_page.check_docs_page_is_open()
    steps.docs_page.check_tutorial()
    steps.tutorial_page.check_tutorial_page_is_open()


def test_docs_search_input(steps):
    search_text = "Python/C API"
    steps.main_page.docs_nav_bottom()
    steps.doc_page.docs_page_open()
    steps.docs_page.docs_search(search_text)
    steps.main_page.check_search_result(search_text)


def test_community_nav(steps):
    steps.main_page.community_landing_open()
    steps.community_landing_page.check_community_landing_page_is_open()

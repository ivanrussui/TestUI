import steps


def test_donation_button():
    driver = steps.driver_steps().create_driver_and_open_python_page()
    steps.main_page(driver).open_donate_page()
    steps.donate_page(driver).check_donate_page_is_open()


def test_search_input():
    driver = steps.driver_steps().create_driver_and_open_python_page()
    steps.main_page(driver).search(search_text="hello")
    steps.main_page(driver).check_search_result(search_text="hello")


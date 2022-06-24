import pytest

from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

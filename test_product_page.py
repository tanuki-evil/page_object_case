import pytest
import time

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)

        page.should_be_authorized_user()

    def test_user_can_add_product_to_bucket(self, browser):
        link = f'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_bucket()
        product_page.solve_quiz_and_get_code()
        product_page.should_name_equal()
        product_page.should_cost_equal()

    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()


@pytest.mark.parametrize('num', [i if i != 7 else pytest.param(7, marks=pytest.mark.xfail) for i in range(10)])
def test_user_can_add_product_to_bucket(browser, num):
    link = f'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_bucket()
    product_page.solve_quiz_and_get_code()
    product_page.should_name_equal()
    product_page.should_cost_equal()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogues/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_bucket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_bucket()
    product_page.should_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_product()
    page.should_not_be_basket_empty_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_product()
    page.should_not_be_basket_empty_message()

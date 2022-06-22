import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('num', [i if i != 7 else pytest.param(7, marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_in_bucket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_bucket()
    product_page.solve_quiz_and_get_code()
    product_page.should_name_equal()
    product_page.should_cost_equal()

import allure
import pytest

from locators.order_page_locators import OrderPageLocators as OrderLoc
from pages.order_page import OrderPage
from data.TestData import Urls


class TestMakeOrder:

    @pytest.mark.parametrize('locator,',
                             [OrderLoc.ORDER_BUTTON_HEADER,
                              OrderLoc.ORDER_BUTTON_MIDDLE_PAGE])
    @allure.title('Тест заказа самоката')
    def test_fill_order_form(self, driver, locator):
        order_page = OrderPage(driver)
        order_page.start_of_order(locator)
        order_page.fill_form_first_page()
        order_page.fill_form_second_page()
        order_page.submit_order()
        assert 'Заказ оформлен' in order_page.modal_window_text

    @pytest.mark.parametrize('button, index, url, TruePage',
                             [(OrderLoc.LOGO_SCOOTER_BUTTON, 0, Urls.HOME_PAGE_URL, OrderLoc.ORDER_BUTTON_HEADER ),
                              (OrderLoc.LOGO_YANDEX_BUTTON, 1, Urls.DZEN_PAGE_URL, OrderLoc.DZEN)])
    @allure.title('Переход по логотипам')
    def test_go_to_logo(self, driver, button, index, url,TruePage):
        order_page = OrderPage(driver)
        order_page.go_to_logo(button, index)
        order_page.wait_for_true_page(TruePage)
        assert url in driver.current_url
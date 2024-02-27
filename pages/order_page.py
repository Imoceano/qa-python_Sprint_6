import allure
from data.TestData import Urls

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as OrderLoc
from data.TestData import OrderData


class OrderPage(BasePage):
    @allure.step("Клик на кнопку 'Да все привыкли'")
    def start_of_order(self, locator):
        self.click_on_element(OrderLoc.COOKIE_BUTTON)
        self.click_on_element(locator)

    @allure.step("Заполнить поля для заказа: Имя, Фамилия, Адрес, Метро, Телеофон, и перейти на вторую страницу оформления заказа")
    def fill_form_first_page(self):
        self.find_element_with_wait(OrderLoc.INPUT_FIRST_NAME).send_keys(OrderData.NAME)
        self.find_element_with_wait(OrderLoc.INPUT_SECOND_NAME).send_keys(OrderData.LAST_NAME)
        self.find_element_with_wait(OrderLoc.INPUT_ADDRESS).send_keys(OrderData.ADDRESS)
        self.find_element_with_wait(OrderLoc.INPUT_METRO_STATION).send_keys(OrderData.METRO_STATION)
        self.click_on_element(OrderLoc.CHOOSE_METRO_STATION)
        self.find_element_with_wait(OrderLoc.INPUT_PHONE_NUMBER).send_keys(OrderData.PHONE_NUMBER)
        self.click_on_element(OrderLoc.NEXT_BUTTON)

    @allure.step("Заполнить поля для заказа: Дата, Время аренды, Выбор цвета ")
    def fill_form_second_page(self):
        self.find_element_with_wait(OrderLoc.INPUT_DATE).send_keys(str(OrderData.DATA))
        self.click_on_element(OrderLoc.ORDER_HEADER)
        self.click_on_element(OrderLoc.INPUT_TIME_OF_RENT)
        self.click_on_element(OrderData.TIME_OF_RENT)
        self.click_on_element(OrderData.COLOR_OF_SCOOTER)
        self.find_element_with_wait(OrderLoc.INPUT_COMMENT).send_keys(OrderData.COMMENT)

    @allure.step("Переход к логотипам")
    def go_to_logo(self, button, index):
        self.get_url(Urls.ORDER_PAGE_URL)
        self.click_on_element(button)
        self.switch_window(index)
    
    @allure.step("Ожидание появления элемента на странице")
    def wait_for_true_page(self,locator):
        self.find_element_with_wait(locator)
    
    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.click_on_element(OrderLoc.ORDER_BUTTON)
        self.click_on_element(OrderLoc.CONFIRM_BUTTON)
        self.modal_window_text = self.find_element_with_wait(OrderLoc.MODAL_WINDOW_SUCCESSFUL_ORDER).text
    
    
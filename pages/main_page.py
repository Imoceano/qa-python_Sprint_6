import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Клик на вопрос и найти локтор текста ответа")
    def click_to_question_and_get_answer_text(self,question_locator,answer_locator):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)
        self.click_on_element(question_locator)
        return self.get_text_from_element(answer_locator)
    
        

    @allure.step("Сравнить текст ожидаемого локатора и результата")
    def check_answer(self,result,expected_result):
        return result == expected_result
    
    



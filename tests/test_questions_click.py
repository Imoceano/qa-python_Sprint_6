import allure
import pytest
from data.TestData import TextOfQuestion
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestClickQuestion:

    @pytest.mark.parametrize(
            "question_locator, answer_locator, expected_result",
              [
                  (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, TextOfQuestion.question_answer1),
                  (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, TextOfQuestion.question_answer2),
                  (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, TextOfQuestion.question_answer3),
                  (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, TextOfQuestion.question_answer4),
                  (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, TextOfQuestion.question_answer5),
                  (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, TextOfQuestion.question_answer6),
                  (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, TextOfQuestion.question_answer7),
                  (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, TextOfQuestion.question_answer8),
])
    @allure.title('Клик по вопросу и проверка отображаемого ответа')
    def test_click_question_check_answer(self,driver,question_locator,answer_locator,expected_result):
        main_page = MainPage(driver)
        result = main_page.click_to_question_and_get_answer_text(question_locator,answer_locator)
        assert main_page.check_answer(result,expected_result)
    
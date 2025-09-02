import pytest
import allure
from pages.main_page import MainPage
from data import FAQ_TEST_DATA


@allure.feature('FAQ Section')
@allure.story('Проверка ответов на частые вопросы')
class TestFAQ:

    @allure.title('Проверка ответов FAQ')
    @allure.description('Проверка, что при клике на вопрос отображается правильный ответ')
    @pytest.mark.parametrize('question_index, expected_answer', FAQ_TEST_DATA)
    def test_faq_question_answer(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_to_bottom()
        main_page.click_faq_question(question_index)
        answer_text = main_page.get_faq_answer_text(question_index)
        assert expected_answer == answer_text

import pytest
import allure
from pages.main_page import MainPage
from tests.data import FAQ_TEST_DATA


@allure.feature('FAQ Section')
@allure.story('Проверка ответов на частые вопросы')
class TestFAQ:

    @allure.step('Открыть главную страницу и прокрутить к FAQ')
    def setup_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_to_bottom()
        return main_page

    @allure.step('Кликнуть на вопрос FAQ #{question_index + 1}')
    def click_faq_question(self, main_page, question_index):
        main_page.click_faq_question(question_index)

    @allure.step('Получить текст ответа на вопрос #{question_index + 1}')
    def get_faq_answer_text(self, main_page, question_index):
        return main_page.get_faq_answer_text(question_index)

    @allure.step('Проверить, что ответ содержит текст: {expected_text}')
    def verify_answer_contains_text(self, answer_text, expected_text, question_index):
        assert answer_text is not None, f"Ответ на вопрос #{question_index + 1} не найден"
        assert expected_text in answer_text, \
            f"Ожидаемый фрагмент '{expected_text}' не найден в ответе: {answer_text}"

    @allure.title('Проверка ответа на вопрос FAQ #{question_index + 1}')
    @allure.description('Проверка, что при клике на вопрос отображается правильный ответ')
    @pytest.mark.parametrize('question_index, expected_answer', FAQ_TEST_DATA)
    def test_faq_question_answer(self, driver, question_index, expected_answer):
        main_page = self.setup_page(driver)
        self.click_faq_question(main_page, question_index)
        answer_text = self.get_faq_answer_text(main_page, question_index)
        self.verify_answer_contains_text(answer_text, expected_answer, question_index)
